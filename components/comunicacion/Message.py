from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass