# imports
# component divulgation
from components.dataBases.strategy.QueryExecutionArtwork import QueryExecutionArtwork
from components.divulgation.tableCommand.Invoker import Invoker
from components.divulgation.tableCommand.ArtisticTechnicTableViewCommand import ArtisticTechnicTableViewCommand
from components.divulgation.tableCommand.ArtistTableViewCommand import ArtistTableViewCommand
from components.divulgation.tableCommand.ArtworkTableViewCommand import ArtworkTableViewCommand
# component Databases
from components.dataBases.context.Operations import Operations
from components.dataBases.strategy.QueryExecutionArtist import QueryExecutionArtist
from components.dataBases.strategy.QueryExecutionTechnic import QueryExecutionTechnic
from components.dataBases.strategy.QueryExecutionArtwork import QueryExecutionArtwork
class tableTemplateRender():
    """
    class that invokes the invoker to render succesfully the table views
    """
    
    # global
    __template = ""
    __data = []
    __command = {}

    def __init__(self,command):
        self.command = command

    def render_template(self):
        """
        FROM POST, we bring a dicc, who takes in the key value (template),
        different values, who tells to the next estructure, how to proccede
        with the command pattern, using it to take the template.
        Then, from module DataBases, we bring the data with all the values
        """
        if (self.command['template'] == "ARTISTAS"):
            print("renderizando tabla artistas")
            print("obteniendo el template")
            invoker = Invoker()
            invoker.set_template(ArtistTableViewCommand())
            self.template = invoker.getting_template()
            print("obteniendo datos")
            # Parameters (strategy class, data)
            execute_query = Operations(QueryExecutionArtist(),"")
            # Data from the query executed
            self.data = execute_query.get()
            return self.template, self.data
        elif (self.command['template'] == "OBRAS"):
            print("renderizando tabla obras")
            print("obteniendo el template")
            invoker = Invoker()
            invoker.set_template(ArtworkTableViewCommand())
            self.template = invoker.getting_template()
            print("obteniendo datos")
            # Parameters (strategy class, data)
            execute_query = Operations(QueryExecutionArtwork(),"")
            # Data from the query executed
            self.data = execute_query.get()
            return self.template, self.data
        elif (self.command['template'] == "TECNICAS"):
            print("renderizando tabla tecnicas")
            print("obteniendo el template")
            invoker = Invoker()
            invoker.set_template(ArtisticTechnicTableViewCommand())
            self.template = invoker.getting_template()
            print("obteniendo datos")
            # Parameters (strategy class, data)
            execute_query = Operations(QueryExecutionTechnic(),"")
            # Data from the query executed
            self.data = execute_query.get()
            return self.template, self.data
            

    # variable getters / setters
    
    @property 
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property 
    def template(self):
        return self.__template

    @template.setter
    def template(self, template):
        self.__template = template
    
    @property 
    def command(self):
        return self.__command

    @command.setter
    def command(self, command):
        self.__command = command