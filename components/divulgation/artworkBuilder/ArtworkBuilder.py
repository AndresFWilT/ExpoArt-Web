from __future__ import annotations
from abc import ABC, abstractmethod

class ArtworkBuilder(ABC):
    """
    This builder interface specifies methods for creating different parts of
    The artist object DB
    """

    @property
    @abstractmethod
    def artwork(self) -> None:
        pass

    @abstractmethod
    def produce_title(self,title) -> None:
        pass

    @abstractmethod
    def produce_description(self,desc) -> None:
        pass

    @abstractmethod
    def produce_date(self,date) -> None:
        pass

    @abstractmethod
    def produce_image(self,img) -> None:
        pass
    