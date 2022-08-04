from __future__ import annotations
from abc import ABC, abstractmethod

class TechnicBuilder(ABC):
    """
    This builder interface specifies methods for creating different parts of
    The artist object DB
    """

    @property
    @abstractmethod
    def technic(self) -> None:
        pass

    @abstractmethod
    def produce_title(self,title) -> None:
        pass

    @abstractmethod
    def produce_description(self,desc) -> None:
        pass
    