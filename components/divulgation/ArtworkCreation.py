# module imports
## Divulgation
from components.divulgation.artworkBuilder.ArtworkDirector import ArtworkDirector
from components.divulgation.artworkBuilder.ConcreteBuilder import ConcreteBuilder
from components.divulgation.ArtistCreation import ArtistCreation
from components.divulgation.TechnicCreation import TechnicCreation
## Databases
from components.dataBases.context.Operations import Operations
from components.dataBases.strategy.QueryExecutionArtwork import QueryExecutionArtwork

class ArtworkCreation():
    # global
    __data = None
    __technic = None
    __artist = None
    __artwork = None
    __artwork_id = 0
    __image = None
    """
    Class that creates an artist using the builder pattern
    """
    def __init__(self, data,file) -> None:
        """
        constructor
        """
        self.data = data
        self.image = file

    def createArtwork(self):
        self.artwork = self.__create_data_artwork()
        director = ArtworkDirector(self.artwork)
        builder = ConcreteBuilder()
        director.artwork_builder = builder
        print("creating full artistic technic: ")
        director.build_artwork_full()
        self.artist = int(self.__get_artist_from_names()[0][0])
        self.technic = int(self.__get_technic_from_title()[0][0])
        return builder.artwork.get_parts()

    def save_all_tables_artwork(self, artwork):
        message = self.saveArtwork(artwork)
        self.artwork_id = int(self.getArtworkbyTitle()[0])
        return  message + self.saveArtworkArtist() + self.saveArtworkTechnic()
        
    def saveArtwork(self, artwork):

        # Parameters (strategy class, data)
        execute_query = Operations(QueryExecutionArtwork(),artwork)
        # Data from the query executed
        return execute_query.save()

    def saveArtworkArtist(self):
        # Parameters (strategy class, data)
        execute_query = QueryExecutionArtwork()
        # Data from the query executed
        return execute_query.save_artwork_artist(self.artwork_id,self.artist)

    def saveArtworkTechnic(self):
        # Parameters (strategy class, data)
        execute_query = QueryExecutionArtwork()
        # Data from the query executed
        return execute_query.save_artwork_technic(self.artwork_id,self.technic)

    def getArtworkbyTitle(self):
        # Parameters (strategy class, data)
        execute_query = QueryExecutionArtwork()
        # Data from the query executed
        return execute_query.get_artwork_by_title(self.artwork['title'])

    def __create_data_artwork(self):
        print(self.data['title'])
        artwork = {
            "title":self.data['title'],
            "desc":self.data['description'],
            "img":("/static/images/"+self.image)
        }
        return artwork

    def __get_artist_from_names(self):
        data = self.data['artist']
        names = data.split(", ")
        artist = {
            "name" : names[0],
            "surname": names[1]
            }
        createArtist = ArtistCreation(artist)
        return createArtist.getArtistbyName()

    def __get_technic_from_title(self):
        at = {
            "title" : self.data['technic']
        }
        createTechnic = TechnicCreation(at)
        return createTechnic.getTechnicbyTitle()

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

    @property
    def artwork_id(self):
        return self.__artwork_id

    @artwork_id.setter
    def artwork_id(self, artwork_id):
        self.__artwork_id = artwork_id

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image
