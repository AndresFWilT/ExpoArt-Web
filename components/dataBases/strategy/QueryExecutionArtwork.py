# imports
import psycopg2
from components.dataBases.Connection import Connection
from components.dataBases.strategy.QueryExecution import QueryExecution

class QueryExecutionArtwork(QueryExecution):
    # global
    __data = []

    """
    Concrete Strategy that implements the algorithms to save an artwork
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
            cur.execute(f"""INSERT INTO artwork (title_artwork, descriptrion_artwork,date_published,image)
                             VALUES ('{data[0]}','{data[1]}',NOW(),'{data[3]}')""")
            # saving
            conn.commit()
            # closing cursor
            cur.close()
            # closing connection
            conn.close()
            return "Obra guardado con exito"
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def get(self,data):
        """
        Method that gets the data from the DB
        """
        # getting the data from the template
        self.data = data
        # try catch, if it's an error with the query or with the connection
        try:
            # connecting DB
            conn = self.__get_connection()
            # create a cursor
            cur = conn.cursor()
            # executing query
            cur.execute('SELECT * FROM artwork')
            # displaying the select
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def save_artwork_artist(self,artwork,artist):
        """
        Method that saves data into the DB
        """
        # try catch, if it's an error with the query or with the connection
        try:
            print(artwork)
            # connecting DB
            conn = self.__get_connection()
            # create a cursor
            cur = conn.cursor()
            # executing query
            cur.execute(f"""INSERT INTO artwork_artist (id_artist_fk,id_artwork_fk) 
            VALUES ({artist},{artwork})""")
            # saving
            conn.commit()
            # closing cursor
            cur.close()
            # closing connection
            conn.close()
            return "Obra-artista guardado con exito"
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def save_artwork_technic(self,artwork,technic):
        """
        Method that saves data into the DB
        """
        # try catch, if it's an error with the query or with the connection
        try:
            # connecting DB
            conn = self.__get_connection()
            # create a cursor
            cur = conn.cursor()
            # executing query
            cur.execute(f"""INSERT INTO artwork_technic (id_at_fk,id_artwork_fk) 
            VALUES ({technic},{artwork});""")
            # saving
            conn.commit()
            # closing cursor
            cur.close()
            # closing connection
            conn.close()
            return "Obra-artista guardado con exito"
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def get_artwork_by_title(self,title):
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
            cur.execute(f"""SELECT id_artwork FROM artwork WHERE title_artwork LIKE '{title}'""")
            # displaying the select
            data = cur.fetchone()
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