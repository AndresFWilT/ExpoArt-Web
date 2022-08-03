from __future__ import annotations
from abc import ABC, abstractmethod

class ArtistBuilder(ABC):
    """
    This builder interface specifies methods for creating different parts of
    The artist object DB
    """

    @property
    @abstractmethod
    def artist(self) -> None:
        pass

    @abstractmethod
    def produce_name(self,name) -> None:
        pass

    @abstractmethod
    def produce_surname(self,surname) -> None:
        pass

    @abstractmethod
    def produce_email(self,email) -> None:
        pass

    @abstractmethod
    def produce_phone(self,phone) -> None:
        pass
    