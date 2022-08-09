from UserGeneral import Usuario
from IHandler import IHandler

class Estudiante(Usuario, IHandler):
    nombre = ""
    apellido = ""

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def operaciones(self):
        return("Puede visualizar obras y agregar ideas")

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def handle(self, rol):
        if "Estudiante" == rol:
            self.rol = "Estudiante"
            print("Es un estudiante")
        else:
            print("Digito un rol no existente")
    
        
