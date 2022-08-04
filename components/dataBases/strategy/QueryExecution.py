from abc import ABC, abstractmethod

class QueryExecution(ABC):
    """
    Interface that declares the methods to all suported versions
    of the executeQuery context

    The context (Operations), use this interface to call the algorithm defined by
    the concrete strategies
    """

    @abstractmethod
    def save(self,data):
        pass

    @abstractmethod
    def get(self,data):
        pass