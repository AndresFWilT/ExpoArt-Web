# imports
import psycopg2
from components.dataBases.Connection import Connection
from components.dataBases.strategy.QueryExecution import QueryExecution

class QueryExecutionGallery(QueryExecution):
    # global
    __data = None

    """
    Concrete Strategy that implements the algorithms to save an artist
    into the DB, following ExecuteQuery 
    """
    def save(self,data):
        """
        Method that saves data into the DB
        """
        # getting the data, in lists from the template
        self.data = data
        # try catch, if it's an error with the query or with the connection
        try:
            # connecting DB
            conn = self.__get_connection()
            # create a cursor
            cur = conn.cursor()
            # executing query
            cur.execute(f"""SELECT art.title_artwork, art.id_artwork, art.image, art.descriptrion_artwork, art.date_published, at.title, ar.name_artist||' '||ar.lastname_artist
                            FROM Artwork art, artwork_technic aatt, Artistic_Technic at, artwork_artist aart, Artist ar
                            WHERE art.id_artwork = {data} AND art.id_artwork = aatt.id_artwork_fk AND aatt.id_at_fk = at.id_at AND art.id_artwork = aart.id_artwork_fk AND aart.id_artist_fk = ar.id_artist""")
            # saving
            conn.commit()
            # closing cursor
            cur.close()
            # closing connection
            conn.close()
            return "Artista guardado con exito"
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def get(self,somethign):
        """
        Method that gets the data from the DB
        """
        # try catch, if it's an error with the query or with the connection
        try:
            # connecting DB
            conn = self.__get_connection()
            # create a cursor
            cur = conn.cursor()
            # executing query
            cur.execute("""SELECT art.title_artwork, art.id_artwork, art.image, at.title, ar.name_artist||' '||ar.lastname_artist
                            FROM Artwork art, artwork_technic aatt, Artistic_Technic at, artwork_artist aart, Artist ar
                            WHERE art.id_artwork = aatt.id_artwork_fk AND aatt.id_at_fk = at.id_at AND art.id_artwork = aart.id_artwork_fk AND aart.id_artist_fk = ar.id_artist""")
            # displaying the select
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def __get_connection(self):
        c = Connection()
        return c.get_connection()

    # variable getters / setters
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data = data