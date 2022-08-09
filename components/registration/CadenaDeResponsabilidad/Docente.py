from Decorador.Decorator import Decorator
from IHandler import IHandler

class Docente(Decorator, IHandler):
    def operaciones(self):
        return f"Puede agregrar ideas, acceder al modulo comunicación({self.usuario.operaciones()})"

    def __intir__(self):
        self.siguiente = None

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def handle(self, rol):
        if "Docente" == rol:
            self.rol = "Docente"
            print("Es un docente")
        else:
            self.siguiente.handle(rol)
