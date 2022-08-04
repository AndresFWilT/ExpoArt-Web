# module imports
## Divulgation
from components.divulgation.artistBuilder.ArtistDirector import ArtistDirector
from components.divulgation.artistBuilder.ConcreteBuilder import ConcreteBuilder
## Databases
from components.dataBases.context.Operations import Operations
from components.dataBases.strategy.QueryExecutionArtist import QueryExecutionArtist

class ArtistCreation():
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

    def createArtist(self):
        director = ArtistDirector(self.data)
        builder = ConcreteBuilder()
        director.artist_builder = builder
        print("creating full artist: ")
        director.build_full_artist()
        return builder.artist.get_parts()

    def saveArtist(self, artist):
        # Parameters (strategy class, data)
        execute_query = Operations(QueryExecutionArtist(),artist)
        # Data from the query executed
        return execute_query.save()

    def getArtistNames(self):
        # Parameters (strategy class, data)
        execute_query = QueryExecutionArtist()
        # Data from the query executed
        return execute_query.get_names()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
