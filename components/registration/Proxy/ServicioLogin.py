from abc import ABC, abstractmethod

class ServicioLogin(ABC):
    @abstractmethod
    def request(self, id_user, password, rol) -> None:
        pass

    
