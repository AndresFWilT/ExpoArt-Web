from abc import ABC, abstractmethod

class IHandler(ABC):
    @abstractmethod
    def setSiguiente(self, siguiente):
        """Define al sucesor en la cadena"""
        pass

    @abstractmethod
    def handle(self, rol):
        pass
        
