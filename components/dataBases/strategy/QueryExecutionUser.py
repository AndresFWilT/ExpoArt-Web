# imports
import psycopg2
from components.dataBases.Connection import Connection
from components.dataBases.strategy.QueryExecution import QueryExecution

class QueryExecutionUser(QueryExecution):
    # global
    __data = []

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


    def get_user(self,data):
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
            cur.execute('SELECT * FROM users')
            # displaying the select
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def get_user_by_name(self,user):
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
            cur.execute(f"""SELECT id_user FROM users WHERE name_user LIKE '%{user['name']}%' AND lastname_user LIKE '%{user['surname']}%'""")
            # displaying the select
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def get_user_by_Id(self,id):
        print(id)  
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
            cur.execute(f"""SELECT id_user, (name_user||' '||lastname_user), email_user FROM users WHERE id_user = {id}""")
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