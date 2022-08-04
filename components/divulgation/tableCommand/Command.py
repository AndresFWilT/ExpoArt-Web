from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    """
    Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(sekf) -> None:
        pass