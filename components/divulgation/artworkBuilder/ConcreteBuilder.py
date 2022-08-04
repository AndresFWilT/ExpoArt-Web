from components.divulgation.artworkBuilder.ArtworkBuilder import ArtworkBuilder
from components.divulgation.artworkBuilder.Artwork import Artwork

class ConcreteBuilder(ArtworkBuilder):
    """
    ConcreteBuilder follow the builder interface and
    provide specific implementations of the building steps
    """
    def __init__(self) -> None:
        """
        constructor
        """
        self.reset()

    def reset(self) -> None:
        self._artwork = Artwork()

    @property
    def artwork(self) -> Artwork:
        """
        Concrete builder provide their own methods for
        retrieving results. A builder instance is expected
        to be ready to start producing another product
        """
        artwork = self._artwork
        self.reset
        return artwork

    def produce_title(self,title) -> None:
        self._artwork.add(title)

    def produce_description(self,desc) -> None:
        self._artwork.add(desc)

    def produce_date(self,date) -> None:
        self._artwork.add(date)
    
    def produce_image(self,image) -> None:
        self._artwork.add(image)