# module imports
## Divulgation
from components.divulgation.technicBuilder.TechnicDirector import TechnicDirector
from components.divulgation.technicBuilder.ConcreteBuilder import ConcreteBuilder
## Databases
from components.dataBases.context.Operations import Operations
from components.dataBases.strategy.QueryExecutionTechnic import QueryExecutionTechnic

class TechnicCreation():
    # global
    __data = {}
    """
    Class that creates an artist using the builder pattern
    """
    def __init__(self, data) -> None:
        """
        constructor
        """
        self.data = data

    def createTechnic(self):
        director = TechnicDirector(self.data)
        builder = ConcreteBuilder()
        director.technic_builder = builder
        print("creating full artistic technic: ")
        director.build_technic_full()
        return builder.technic.get_parts()

    def saveTechnic(self, technic):
        # Parameters (strategy class, data)
        execute_query = Operations(QueryExecutionTechnic(),technic)
        # Data from the query executed
        return execute_query.save()

    def getTechnicTitles(self):
        # Parameters (strategy class, data)
        execute_query = QueryExecutionTechnic()
        # Data from the query executed
        return execute_query.get_titles()

    def getTechnicbyTitle(self):
        # Parameters (strategy class, data)
        execute_query = QueryExecutionTechnic()
        # Data from the query executed
        return execute_query.get_technic_by_title(self.data)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
