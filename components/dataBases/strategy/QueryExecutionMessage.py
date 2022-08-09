# imports
import psycopg2
from components.dataBases.Connection import Connection
from components.dataBases.strategy.QueryExecution import QueryExecution

class QueryExecutionMessage(QueryExecution):
    # global
    __data = []

    """
    Concrete Strategy that implements the algorithms to save a message
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
            cur.execute(f"""INSERT INTO message (subject,sender,message)
             VALUES ('{data[0]}','{data[1]}','{data[2]}')""")
            # saving
            conn.commit()
            # closing cursor
            cur.close()
            # closing connection
            conn.close()
            return "Mensaje enviado con exito"
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
            cur.execute('SELECT * FROM message')
            # displaying the select
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def get_names(self):
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
            cur.execute('SELECT subject,sender,message FROM message')
            # displaying the select
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."

    def get_artist_by_id_message(self,message):
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
            cur.execute(f"""SELECT id_message FROM message WHERE sender LIKE '%{message['sender']}%'""")
            # displaying the select
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except psycopg2.Error as error:
            print("something happened..."+str(error))
            return "Algo paso y no se puso realizar la transaccion.."