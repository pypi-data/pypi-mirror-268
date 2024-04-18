from typing import Generic, TypeVar, overload, Literal
from abc import ABC, abstractmethod
from haskellian.either import Either
from ..errors import DBError, InexistentItem
from ..api import KV

T = TypeVar('T')

class Appendable(ABC, Generic[T]):
  @overload
  @abstractmethod
  async def append(self, id: str, values: list[T], *, create: Literal[False]) -> Either[DBError|InexistentItem, None]:
    """Appends `values` if it already existed. Otherwise doesn't append, and returns `Left[ExistentItem]`"""
  @overload
  @abstractmethod
  async def append(self, id: str, values: list[T], *, create: bool = True) -> Either[DBError, None]:
    """Appends `values` to `id`, creating the item if needed"""

class AppendableAPI(KV[T], Appendable, Generic[T]):
  ...
  