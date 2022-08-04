from components.divulgation.artistBuilder.ArtistBuilder import ArtistBuilder
from components.divulgation.artistBuilder.Artist import Artist

class ConcreteBuilder(ArtistBuilder):
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
        self._artist = Artist()

    @property
    def artist(self) -> Artist:
        """
        Concrete builder provide their own methods for
        retrieving results. A builder instance is expected
        to be ready to start producing another product
        """
        artist = self._artist
        self.reset
        return artist

    def produce_name(self,name) -> None:
        self._artist.add(name)

    def produce_surname(self,surname) -> None:
        self._artist.add(surname)

    def produce_email(self,email) -> None:
        self._artist.add(email)

    def produce_phone(self,phone) -> None:
        self._artist.add(phone)