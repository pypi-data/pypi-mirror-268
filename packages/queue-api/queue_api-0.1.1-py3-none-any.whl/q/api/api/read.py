from typing import Generic, Never, TypeVar, Callable, Awaitable, overload, AsyncIterable, AsyncIterator, TypeGuard
from haskellian.asyn.iter import AsyncIter
from haskellian.asyn.promises import of
from abc import ABC, abstractmethod

A = TypeVar('A', covariant=True)
B = TypeVar('B', covariant=True)

class ReadQueue(ABC, AsyncIterator[tuple[str, A]], Generic[A]):
  
  @abstractmethod
  async def _read(self, id: str | None, remove: bool) -> None | tuple[str, A]:
    ...

  @overload
  async def pop(self) -> tuple[str, A]:
    ...
  @overload
  async def pop(self, id: str) -> None | A:
    ...

  async def pop(self, id: str | None = None) -> None | A | tuple[str, A]:
    match await self._read(id, remove=True):
      case k, v:
        return (k, v) if id is None else v
  
  @overload
  async def read(self) -> tuple[str, A]:
    ...
  @overload
  async def read(self, id: str) -> None | A:
    ...
  
  async def read(self, id: str | None = None) -> None | A | tuple[str, A]:
    match await self._read(id, remove=False):
      case k, v:
        return (k, v) if id is None else v
      
  @abstractmethod
  def _items(self) -> AsyncIterable[tuple[str, A]]:
    ...

  def items(self) -> AsyncIter[tuple[str, A]]:
    return AsyncIter(self._items())
  
  def keys(self) -> AsyncIter[str]:
    return AsyncIter(k async for k, _ in self._items())
  
  def values(self) -> AsyncIter[A]:
    return AsyncIter(v async for _, v in self._items())
  
  async def __anext__(self) -> tuple[str, A]:
    return await self.pop()
  
  def iter(self):
    async def iterate():
      while (x := await self.pop()):
        yield x
    return AsyncIter(iterate())
  
  __aiter__ = iter
  
  def map(self, f: Callable[[A], B]) -> 'ReadQueue[B]':
    """Maps `f` over self. Returns a new queue, but `self` is still mutated when popping from the new queue"""
    return MappedQueue(self, lambda kv: of((kv[0], f(kv[1]))))
  
  def map_kv(self, f: Callable[[str, A], B]) -> 'ReadQueue[B]':
    """Map but `f` receives both key and value"""
    return MappedQueue(self, lambda kv: of((kv[0], f(*kv))))
  
  def map_k(self, f: Callable[[str], B]) -> 'ReadQueue[B]':
    """Map but `f` receives the key"""
    return MappedQueue(self, lambda kv: of((kv[0], f(kv[0]))))
  
  def map_kvt(self, f: Callable[[tuple[str, A]], B]) -> 'ReadQueue[B]':
    """Map but `f` receives both key and value as a tuple"""
    return MappedQueue(self, lambda kv: of((kv[0], f(kv))))
  
  def amap(self, f: Callable[[A], Awaitable[B]]) -> 'ReadQueue[B]':
    """Map but `f` is asynchronous"""
    async def mapper(kv: tuple[str, A]):
      return kv[0], await f(kv[1])
    return MappedQueue(self, mapper)
  
  def amap_kv(self, f: Callable[[str, A], Awaitable[B]]) -> 'ReadQueue[B]':
    """Map but `f` is asynchronous and receives both key and value"""
    async def mapper(kv: tuple[str, A]):
      return kv[0], await f(*kv)
    return MappedQueue(self, mapper)
  
  def amap_k(self, f: Callable[[str], Awaitable[B]]) -> 'ReadQueue[B]':
    """Map but `f` is asynchronous and receives the key"""
    async def mapper(kv: tuple[str, A]):
      return kv[0], await f(kv[0])
    return MappedQueue(self, mapper)
  
  def amap_kvt(self, f: Callable[[tuple[str, A]], Awaitable[B]]) -> 'ReadQueue[B]':
    """Map but `f` is asynchronous and receives both key and value as a tuple"""
    async def mapper(kv: tuple[str, A]):
      return kv[0], await f(kv)
    return MappedQueue(self, mapper)

  @overload
  def filter(self, pred: Callable[[A], TypeGuard[B]]) -> 'ReadQueue[B]': ...
  @overload
  def filter(self, pred: Callable[[A], bool]) -> 'ReadQueue[A]': ...
  def filter(self, pred):
    return FilteredQueue(self, lambda _, v: pred(v))
  
  @overload
  def filter(self, pred: Callable[[str, A], TypeGuard[B]]) -> 'ReadQueue[B]': ...
  @overload
  def filter(self, pred: Callable[[str, A], bool]) -> 'ReadQueue[A]': ...
  def filter_kv(self, pred):
    return FilteredQueue(self, pred)
  
  def partition(self, pred: Callable[[A], bool]) -> 'tuple[ReadQueue[A], ReadQueue[A]]':
    """Returns `self.filter(pred), self.filter(!pred)`"""
    return self.filter(pred), self.filter(lambda x: not pred(x))
  
  def partition_kv(self, pred: Callable[[str, A], bool]) -> 'tuple[ReadQueue[A], ReadQueue[A]]':
    """Returns `self.filter_kv(pred), self.filter_kv(!pred)`"""
    return self.filter_kv(pred), self.filter_kv(lambda x: not pred(x))
  
  
class MappedQueue(ReadQueue[B], Generic[A, B]):
  
  def __init__(self, q: ReadQueue[A], f: Callable[[tuple[str, A]], Awaitable[tuple[str, B]]]):
    self._wrapped = q
    self._mapper = f
    __name__ = f'Mapped{repr(self)}'

  def _items(self) -> AsyncIterable[tuple[str, B]]:
    return (await self._mapper(x) async for x in self._wrapped._items())
  
  async def _read(self, id: str | None = None, remove: bool = False) -> tuple[str, B] | None:
    match await self._wrapped._read(id, remove):
      case k, v:
        return await self._mapper((k, v))
      
class FilteredQueue(ReadQueue[A], Generic[A]):

  def __init__(self, queue: ReadQueue[A], pred: Callable[[str, A], bool]):
    self._pred = pred
    self._queue = queue

  async def _point_read(self, id: str, remove: bool) -> None | tuple[str, A]:
    item = await self._queue.read(id)
    if item is None or not self._pred(id, item):
      return None
    if remove:
      await self._queue.pop(id)
    return id, item

  async def _read_any(self, remove: bool) -> tuple[str, A]:
    async for id, item in self._items():
      if remove:
        await self._queue.pop(id)
      return id, item
    return Never

  async def _read(self, id: str | None, remove: bool) -> None | tuple[str, A]:
    return await (self._read_any(remove) if id is None else self._point_read(id, remove))
  
  async def _items(self) -> AsyncIterable[tuple[str, A]]:
    async for item in self._queue._items():
      if self._pred(*item):
        yield item