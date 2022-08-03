from components.divulgation.artistBuilder.ArtistDirector import ArtistDirector
from components.divulgation.artistBuilder.ConcreteBuilder import ConcreteBuilder

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

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
