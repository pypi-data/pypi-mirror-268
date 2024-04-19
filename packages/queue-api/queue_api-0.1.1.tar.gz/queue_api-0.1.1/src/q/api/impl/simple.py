from typing import Generic, TypeVar, AsyncIterable
from collections import OrderedDict
from ..api import ReadQueue, WriteQueue
from haskellian.asyn.promises import ManagedAwaitable

A = TypeVar('A')
B = TypeVar('B')

class SimpleQueue(WriteQueue[A], ReadQueue[A], Generic[A]):
  """Dead simple in-memory implementation backed by an `OrderedDict`"""

  def __init__(self):
    self.xs: OrderedDict[str, A] = OrderedDict()
    self._next = ManagedAwaitable()

  def __len__(self):
    return len(self.xs) # type: ignore

  async def _read(self, id: str | None = None, remove: bool = False) -> None | tuple[str, A]:
    if id is None:
      if len(self.xs) == 0:
        await self._next
        self._next = ManagedAwaitable()
        return await self._read(id, remove)
      elif remove:
        return self.xs.popitem()
      else:
        return next(iter(self.xs.items()))
    elif id in self.xs:
      v = self.xs.pop(id) if remove else self.xs[id]
      return id, v
    
  async def push(self, k: str, v: A):
    self.xs[k] = v
    if not self._next.resolved:
      self._next.resolve()
  
  async def _items(self) -> AsyncIterable[tuple[str, A]]:
    for x in self.xs.items():
      yield x
  