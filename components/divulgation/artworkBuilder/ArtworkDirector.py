from components.divulgation.artworkBuilder.ArtworkBuilder import ArtworkBuilder

class ArtworkDirector():
    # global
    __data = {}
    """
    The ArtworkDirector is only responsible for executing the building steps
    in a particular sequence, helpful to produce Artwork according to an order
    """

    def __init__(self, data) -> None:
        self._artwork_builder = None
        self.data = data

    @property
    def artwork_builder(self) -> ArtworkBuilder:
        return self._artwork_builder

    @artwork_builder.setter
    def artwork_builder(self, artwork_builder: ArtworkBuilder) -> None:
        """
        Director works with any builder instance that the client code passes
        to it.
        """
        self._artwork_builder = artwork_builder

    """
    Director, build totally product variations using the same building steps
    """

    def build_artwork_full(self) -> None:
        self.artwork_builder.produce_title(self.data["title"])
        self.artwork_builder.produce_description(self.data["desc"])
        self.artwork_builder.produce_date("")
        self.artwork_builder.produce_image(self.data["img"])

    # variable getters / setters

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data = data