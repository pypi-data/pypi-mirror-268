from typing import TypeVar, Generic, overload, Literal
from abc import ABC, abstractmethod
from haskellian.either import Either
from haskellian.asyn.promises import Promise
from haskellian.asyn.iter import AsyncIter
from .errors import ExistentItem, InexistentItem, DBError, InvalidData, ReadError

T = TypeVar('T')

class KV(ABC, Generic[T]):
  @overload
  @abstractmethod
  def insert(self, key: str, value: T, *, replace: Literal[True]) -> Promise[Either[DBError, None]]: ...
  @overload
  @abstractmethod
  def insert(self, key: str, value: T, *, replace: bool = False) -> Promise[Either[DBError | ExistentItem, None]]: ...

  @abstractmethod
  def update(self, key: str, value: T) -> Promise[Either[DBError | InexistentItem, None]]: ...

  @abstractmethod
  def read(self, key: str) -> Promise[Either[ReadError, T]]: ...

  @abstractmethod
  def delete(self, key: str) -> Promise[Either[DBError | InexistentItem, None]]: ...

  @abstractmethod
  def items(self, batch_size: int | None = None) -> AsyncIter[Either[DBError | InvalidData, tuple[str, T]]]: ...

  @abstractmethod
  def keys(self, batch_size: int | None = None) -> AsyncIter[Either[DBError, str]]: ...

  @abstractmethod
  def commit(self) -> Promise[Either[DBError, None]]: ...
  
  @abstractmethod
  def rollback(self) -> Promise[Either[DBError, None]]: ...
