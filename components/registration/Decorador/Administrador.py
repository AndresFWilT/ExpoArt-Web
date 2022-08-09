from Decorator import Decorator
from IHandler import IHandler

class Administrador(Decorator, IHandler):
    def operaciones(self):
        return f"Puede ver el CRUD de Usuarios y Obra({self.usuario.operaciones()})"

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def handle(self, rol):
        if "Administrador" == rol:
            self.rol = "Administrador"
            print("Es un admninistrador")
        else:
            self.siguiente.handle(rol)
