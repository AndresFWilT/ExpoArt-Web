from components.divulgation.technicBuilder.TechnicBuilder import TechnicBuilder
from components.divulgation.technicBuilder.Technic import Technic

class ConcreteBuilder(TechnicBuilder):
    """
    ConcreteBuilder follow the builder interface and
    provide specific implementations of the building steps
    """
    def __init__(self) -> None:
        """
        constructor
        """
        self.reset()

    def reset(self) -> None:
        self._technic = Technic()

    @property
    def technic(self) -> Technic:
        """
        Concrete builder provide their own methods for
        retrieving results. A builder instance is expected
        to be ready to start producing another product
        """
        technic = self._technic
        self.reset
        return technic

    def produce_title(self,title) -> None:
        self._technic.add(title)

    def produce_description(self,desc) -> None:
        self._technic.add(desc)