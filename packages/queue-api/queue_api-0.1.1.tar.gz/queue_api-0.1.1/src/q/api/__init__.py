"""
### Queue Api
> Abstract Async R/W Queue APIs
"""
from .api import ReadQueue, WriteQueue, Queue, connect
from .impl import SimpleQueue, EmptyQueue