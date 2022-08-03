# imports
import psycopg2
import json

class Connection():
    #global
    __credentials = {}

    """
    Class that connects to the Database
    """
    def __init__(self):
        """
        Constructor set credentials
        """
        self.credentials = self.__get_credentials_db()

    def get_connection(self):
        """
        Connect to the PostgreSQL database server
        """
        return psycopg2.connect(f'dbname={self.credentials["database"]} user={self.credentials["user"]} password={self.credentials["password"]}')
                


    # private function that get the credentials from a JSON file
    def __get_credentials_db(self):
        # Opening JSON fil
        f = open('components/dataBases/credentials.json')
        # return JSON object as a dicctionary
        db = json.load(f)
        f.close
        return db

    @property
    def credentials(self):
        """
        getter of credentials
        """
        return self.__credentials

    @credentials.setter
    def credentials(self,credentials):
        """
        setter of credentials
        """
        self.__credentials = credentials