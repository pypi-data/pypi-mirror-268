from typing import TypeVar
from .read import ReadQueue
from .write import WriteQueue

A = TypeVar('A')

async def connect(here: ReadQueue[A], there: WriteQueue[A]):
  async for k, v in here:
    await there.push(k, v)