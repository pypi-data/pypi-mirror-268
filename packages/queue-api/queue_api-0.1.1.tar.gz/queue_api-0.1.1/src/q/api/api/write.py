from typing import Generic, TypeVar, Callable, Awaitable
from haskellian.asyn.promises import of
from abc import ABC, abstractmethod

A = TypeVar('A', contravariant=True)
B = TypeVar('B', contravariant=True)

class WriteQueue(ABC, Generic[A]):

  @abstractmethod
  async def push(self, key: str, value: A):
    ...

  def pusher(self, key: str) -> Callable[[A], Awaitable[None]]:
    """Partially applied `push`"""
    return lambda value: self.push(key, value)
  
  def premap(self, f: Callable[[B], A]) -> 'WriteQueue[B]':
    return PremappedQueue(self, lambda kv: of((kv[0], f(kv[1]))))
  
  def premap_kv(self, f: Callable[[str, B], A]) -> 'WriteQueue[B]':
    """Map but `f` receives both key and value"""
    return PremappedQueue(self, lambda kv: of((kv[0], f(*kv))))
  
  def premap_k(self, f: Callable[[str], A]) -> 'WriteQueue':
    """Map but `f` receives the key"""
    return PremappedQueue(self, lambda kv: of((kv[0], f(kv[0]))))
  
  def premap_kvt(self, f: Callable[[tuple[str, B]], A]) -> 'WriteQueue[B]':
    """Map but `f` receives both key and value as a tuple"""
    return PremappedQueue(self, lambda kv: of((kv[0], f(kv))))
  
  def apremap(self, f: Callable[[B], Awaitable[A]]) -> 'WriteQueue[B]':
    """Map but `f` is asynchronous"""
    async def mapper(kv: tuple[str, B]):
      return kv[0], await f(kv[1])
    return PremappedQueue(self, mapper)
  
  def apremap_kv(self, f: Callable[[str, B], Awaitable[A]]) -> 'WriteQueue[B]':
    """Map but `f` is asynchronous and receives both key and value"""
    async def mapper(kv: tuple[str, B]):
      return kv[0], await f(*kv)
    return PremappedQueue(self, mapper)
  
  def apremap_k(self, f: Callable[[str], Awaitable[A]]) -> 'WriteQueue':
    """Map but `f` is asynchronous and receives the key"""
    async def mapper(kv: tuple[str, B]):
      return kv[0], await f(kv[0])
    return PremappedQueue(self, mapper)
  
  def apremap_kvt(self, f: Callable[[tuple[str, B]], Awaitable[A]]) -> 'WriteQueue[B]':
    """Map but `f` is asynchronous and receives both key and value as a tuple"""
    async def mapper(kv: tuple[str, B]):
      return kv[0], await f(kv)
    return PremappedQueue(self, mapper)


class PremappedQueue(WriteQueue[B], Generic[A, B]):
  
  def __init__(self, q: WriteQueue[A], f: Callable[[tuple[str, B]], Awaitable[tuple[str, A]]]):
    self._wrapped = q
    self._mapper = f
    __name__ = f'Mapped{repr(self)}'

  async def push(self, key: str, value: B):
    k, v = await self._mapper((key, value))
    return await self._wrapped.push(k, v)