from abc import ABC,abstractmethod

class Product(ABC):
    """
    Interface that declares the operations that all concrete products (artist,artwork,artistic_technic)
    must implement
    """

    @abstractmethod
    def operation(self,data):
        pass