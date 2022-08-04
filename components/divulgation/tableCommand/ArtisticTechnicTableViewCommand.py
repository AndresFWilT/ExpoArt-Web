from components.divulgation.tableCommand.Command import Command

class ArtisticTechnicTableViewCommand(Command):
    # global
    __template = ""
    """
    Command that returns the template for artwork view table
    """
    def __init__(self):
        self.template = "viewArtisticTechnicTable.html"

    def execute(self) -> None:
        return self.template

    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self,template):
        self.__template = template