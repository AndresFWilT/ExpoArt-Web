from __future__ import annotations
from abc import ABC, abstractmethod
from email import message
from tkinter import N


# module imports
## Communication
from components.comunicacion.Message import Message
from components.comunicacion.ConcreteMessageArtistA import ConcreteMessageArtistA
from components.comunicacion.ConcreteMessageArtistB import ConcreteMessageArtistB
## Databases

from components.dataBases.context.Operations import Operations

from components.dataBases.strategy.QueryExecutionArtist import QueryExecutionArtist
from components.dataBases.strategy.QueryExecutionMessage import QueryExecutionMessage
from components.dataBases.strategy.QueryExecutionUser import QueryExecutionUser

class ArtistCommunication():
    # global
    __data = {}
    __message = None
    """
    Class that creates an artist using the builder pattern
    """
    def __init__(self, data) -> None:
        """
        constructor
        """
        self.data = data
        

       
    def getArtistbyId(self, data):        
        # Parameters (strategy class, data)
        execute_query = QueryExecutionArtist()
        # Data from the query executed
        return execute_query.get_artist_by_Id(data[0][0])

    def getArtistbyName(self):
        names = self.data['artist'].split(", ")
        artist = {
            "name" : names[0],
            "surname": names[1]
        }
        # Parameters (strategy class, data)
        execute_query = QueryExecutionArtist()
        # Data from the query executed
        return execute_query.get_artist_by_name(artist)

    def getUserbyId(self):
                 
        # Parameters (strategy class, data)
        execute_query = QueryExecutionUser()
        # Data from the query executed
        return execute_query.get_user_by_Id(self.data)

    def getUserbyName(self):
        names = self.data['user'].split(", ")
        user = {
            "name" : names[0],
            "surname": names[1]
        }
        # Parameters (strategy class, data)
        execute_query = QueryExecutionUser()
        # Data from the query executed
        return execute_query.get_user_by_name(user)
    
    def sendMessage(self,user,app):
        m = ConcreteMessageArtistA(self.data)
        message= m.operation_implementation(app)
        message+=" y "+self.saveMessage(user)
        return message

    def saveMessage(self,user):
        id = self.getArtistbyName()
        # Parameters (strategy class, data)
        execute_query = QueryExecutionMessage()
        # Data from the query executed
        return execute_query.save(self.data,id,user)

    

        
      

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def message(self):
            return self.__message

    @message.setter
    def message(self, message):
            self.__message = message
