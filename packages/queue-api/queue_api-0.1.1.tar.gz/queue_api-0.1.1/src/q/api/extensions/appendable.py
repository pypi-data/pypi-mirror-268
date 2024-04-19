from typing import Generic, TypeVar, overload, Literal
from abc import abstractmethod
from ..api import WriteQueue, Queue

T = TypeVar('T')

class AppendQueue(WriteQueue[list[T]], Generic[T]):
  @overload
  @abstractmethod
  async def append(self, id: str, values: list[T], *, create: Literal[False]) -> bool:
    """Appends `values` if it already existed. Otherwise doesn't append, and returns `False`"""
  @overload
  @abstractmethod
  async def append(self, id: str, values: list[T], *, create: bool = True):
    """Appends `values` to `id`, creating the item if needed"""
    
class AppendableQueue(AppendQueue[T], Queue[list[T]], Generic[T]):
  ...