from __future__ import annotations
from abc import ABC
from components.dataBases.strategy.QueryExecution import QueryExecution

class Operations():
    # global
    __data = {}
    """
    The context that de fines the interface of interes to user
    """

    def __init__(self, queryExecution: QueryExecution, data) -> None:
        """
        Strategy trough context (queryExecution, operation)
        """
        self._queryExecution = queryExecution
        self.data = data

    @property
    def queryExecution(self) -> queryExecution:
        """
        The context mantains a reference to one of the Strategy objects
        """
        return self._queryExecution
    
    @queryExecution.setter
    def executeQuery(self, queryExecution: QueryExecution) -> None:
        """
        setter to replace a executeQuery object at runtime
        """
        self._queryExecution = queryExecution
        

    def save(self) -> None:
        """
        The context delegates some work to the Strategy (ExecuteQuery) objet instead
        of implementing multiple versions of the algorithm on it's own
        """
        print("saving...")
        return self._queryExecution.save(self.data)

    def get(self) -> None:
        """
        The context delegates some work to the Strategy (ExecuteQuery) objet instead
        of implementing multiple versions of the algorithm on it's own
        """
        print("getting data...")
        return self._queryExecution.get(self.data)

    ## global variables getter / setter
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data = data
