from abc import ABC, abstractmethod

class Locatable(ABC):
  @abstractmethod
  def url(self, id: str) -> str:
    ...
