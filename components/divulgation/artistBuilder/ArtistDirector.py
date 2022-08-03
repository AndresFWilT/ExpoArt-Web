from components.divulgation.artistBuilder.ArtistBuilder import ArtistBuilder

class ArtistDirector():
    # global
    __data = {}
    """
    The ArtistDirector is only responsible for executing the building steps
    in a particular sequence, helpful to produce artist according to an order
    """

    def __init__(self, data) -> None:
        self._artist_builder = None
        self.data = data

    @property
    def artist_builder(self) -> ArtistBuilder:
        return self._artist_builder

    @artist_builder.setter
    def artist_builder(self, artist_builder: ArtistBuilder) -> None:
        """
        Director works with any builder instance that the client code passes
        to it.
        """
        self._artist_builder = artist_builder

    """
    Director, build totally product variations using the same building steps
    """

    def build_artist_with_full_name(self) -> None:
        self.artist_builder.produce_name(self.data["name"])
        self.artist_builder.produce_surname(self.data["surname"])

    def build_full_artist(self) -> None:
        self.artist_builder.produce_name(self.data["name"])
        self.artist_builder.produce_surname(self.data["surname"])
        self.artist_builder.produce_email(self.data["email"])
        self.artist_builder.produce_phone(self.data["phone"])
        print("created")

    # variable getters / setters

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data = data