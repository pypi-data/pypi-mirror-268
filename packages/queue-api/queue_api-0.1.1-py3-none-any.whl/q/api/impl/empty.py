from typing import AsyncIterable, Generic, TypeVar
from ..api import ReadQueue, WriteQueue

A = TypeVar('A')

class EmptyQueue(ReadQueue[A], WriteQueue[A], Generic[A]):

  async def _read(self, id: str | None) -> None | tuple[str, A]:
    ...
  
  async def _items(self) -> AsyncIterable[tuple[str, A]]:
    if False:
      yield
  
  async def push(self, key: str, value: A):
    ...
