from email.message import Message


## Databases
from components.dataBases.context.Operations import Operations
from components.dataBases.strategy.QueryExecutionMessage import QueryExecutionMessage

class ConcreteMessageArtistB(Message):
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
        
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."
