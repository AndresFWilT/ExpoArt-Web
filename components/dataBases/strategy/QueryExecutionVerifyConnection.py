# imports
import psycopg2
from components.dataBases.Connection import Connection
from components.dataBases.strategy.QueryExecution import QueryExecution

class QueryExecutionVerifyConnection(QueryExecution):
    # global
    __data = {}

    """
    Concrete Strategy that implements the algorithms to save an artist
    into the DB, following ExecuteQuery 
    """
    def save(self,data):
        """
        Method that saves data into the DB
        """
        # getting the data from the template
        self.data = data
        # try catch, it it's an error with the query or with the connection
        try:
            # connecting DB
            conn = self.__get_connection()
            # create a cursor
            cur = conn.cursor()
            # executing query
            cur.execute('SELECT version()')
            # displaying the select
            db_version = cur.fetchone()
            cur.close()
            return "Conexion exitosa "+str(db_version)
        except psycopg2.Error as error:
            print("something happened..."+error)
            return "Algo paso y no se puso realizar la transaccion.."

    def get(self,data):
        """
        Method that gets the data from the DB
        """
        # getting the data from the template
        self.data = data
        # try catch, it it's an error with the query or with the connection
        try:
            # connecting DB
            conn = self.__get_connection()
            # create a cursor
            cur = conn.cursor()
            # executing query
            cur.execute('SELECT version()')
            # displaying the select
            db_version = cur.fetchone()
            cur.close()
            return db_version
        except psycopg2.Error as error:
            print("something happened..."+error)
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