from typing import TypeVar, Generic
import asyncio
import haskellian.asyn.promises as P
from ..appendable import AppendableQueue
from ...ops.bounding import Bounded

T = TypeVar('T')

class AppendBounded(AppendableQueue[T], Bounded[list[T]], Generic[T]):
  def __init__(self, queue: AppendableQueue[T], max_items: int):
    super().__init__(queue, max_items)
    self._queue = queue
    self._append_buffer = asyncio.Queue[tuple[str, list[T], bool]]()

  async def _append_advance(self):
    k, vs, create = await self._append_buffer.get()
    await self._queue.append(k, vs, create=create)

  async def append(self, id: str, values: list[T], *, create = True):
    if create:
      await self._append_buffer.put((id, values, create))
      while self.num_items >= self.max_items:
        if self._promise.resolved:
          self._promise = P.ManagedAwaitable()
      self.num_items += 1
      await self._append_advance()
    else:
      return await self._queue.append(id, values, create=False)
    
def bounded(queue: AppendableQueue[T], max_items: int) -> AppendableQueue[T]:
  return AppendBounded(queue, max_items)