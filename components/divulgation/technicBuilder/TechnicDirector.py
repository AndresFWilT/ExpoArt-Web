from components.divulgation.technicBuilder.TechnicBuilder import TechnicBuilder

class TechnicDirector():
    # global
    __data = {}
    """
    The TechnicDirector is only responsible for executing the building steps
    in a particular sequence, helpful to produce technic according to an order
    """

    def __init__(self, data) -> None:
        self._technic_builder = None
        self.data = data

    @property
    def technic_builder(self) -> TechnicBuilder:
        return self._technic_builder

    @technic_builder.setter
    def technic_builder(self, technic_builder: TechnicBuilder) -> None:
        """
        Director works with any builder instance that the client code passes
        to it.
        """
        self._technic_builder = technic_builder

    """
    Director, build totally product variations using the same building steps
    """

    def build_technic_full(self) -> None:
        self.technic_builder.produce_title(self.data["title"])
        self.technic_builder.produce_description(self.data["description"])

    # variable getters / setters

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data = data