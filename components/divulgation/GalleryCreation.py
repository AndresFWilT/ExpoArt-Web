# module imports
## Divulgation
from components.divulgation.galleryFactory.GalleryCreator import GalleryCreator
from components.divulgation.galleryFactory.ConcreteCreatorArtist import ConcreteCreatorArtist
from components.divulgation.galleryFactory.ConcreteCreatorArtwork import ConcreteCreatorArtwork
from components.divulgation.galleryFactory.ConcreteCreatorAT import ConcreteCreatorAT
## Databases
from components.dataBases.context.Operations import Operations
from components.dataBases.strategy.QueryExecutionGallery import QueryExecutionGallery

class GalleryCreation():
    # global
    __artwork = None
    __technic = None
    __artist = None
    __data = None
    """
    Class that creates an artist using the builder pattern
    """
    def __init__(self, data) -> None:
        """
        constructor
        """
        self.data = data

    def create_specific_artwork(self):
        x = 1

    def create_gallery(self):
        execute_query = Operations(QueryExecutionGallery(),"")
        # Data from the query executed
        self.data = execute_query.get()
        # we create with factory method the gallery
        self.artist = self.creator(ConcreteCreatorArtist())
        self.artwork = self.creator(ConcreteCreatorArtwork())
        self.technic = self.creator(ConcreteCreatorAT())
        return self.data

    def creator(self,creator: GalleryCreator) -> None:
        """
        instance of a concrete creator, albeit through
        its base interface. As long as the client keeps working with the creator via
        the base interface, you can pass it any creator's subclass.
        """
        print("data created")
        creator.some_operation(self.data)
    # variable getter / setter

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def artwork(self):
        return self.__artwork

    @artwork.setter
    def artwork(self, artwork):
        self.__artwork = artwork

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, artist):
        self.__artist = artist
    
    @property
    def technic(self):
        return self.__technic

    @technic.setter
    def technic(self, technic):
        self.__technic = technic