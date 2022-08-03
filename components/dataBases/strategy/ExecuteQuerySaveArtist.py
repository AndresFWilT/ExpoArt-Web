# imports
from components.dataBases.Connection import Connection
from components.dataBases.strategy.ExecuteQuery import ExecuteQuery

class ExecuteQuerySaveArtist(ExecuteQuery):
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
        # connecting DB
        conn = self.__get_connection()
        # create a cursor
        cur = conn.cursor()
        # executing query
        cur.execute('SELECT version()')
        # displaying the select
        db_version = cur.fetchone()
        cur.close()

    def get(self,data):
        """
        Method that gets the data from the DB
        """
        # getting the data from the template
        self.data = data
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