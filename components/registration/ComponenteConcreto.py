from UserGeneral import Usuario

class Docente(Usuario):
    nombre=""
    apellido=""

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def operaciones(self):
        return("Puede agregrar ideas, acceder al modulo comunicación")