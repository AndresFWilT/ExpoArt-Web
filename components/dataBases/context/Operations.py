from __future__ import annotations
from abc import ABC
from components.dataBases.strategy.ExecuteQuery import ExecuteQuery

class Operations():
    # global
    __data = {}
    """
    The context that de fines the interface of interes to user
    """

    def __init__(self, executeQuery: ExecuteQuery, data) -> None:
        """
        Strategy trough context (executeQuery, operation)
        """
        self._executeQuery = executeQuery
        self.data = data

    @property
    def executeQuery(self) -> executeQuery:
        """
        The context mantains a reference to one of the Strategy objects
        """
        return self._executeQuery
    
    @executeQuery.setter
    def executeQuery(self, executeQuery: ExecuteQuery) -> None:
        """
        setter to replace a executeQuery object at runtime
        """
        self._executeQuery = executeQuery
        

    def save(self) -> None:
        """
        The context delegates some work to the Strategy (ExecuteQuery) objet instead
        of implementing multiple versions of the algorithm on it's own
        """
        print("saving...")
        self._executeQuery.save(self.data)

    def get(self) -> None:
        """
        The context delegates some work to the Strategy (ExecuteQuery) objet instead
        of implementing multiple versions of the algorithm on it's own
        """
        print("getting data...")
        return self._executeQuery.get(self.data)

    ## global variables getter / setter
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data = data
