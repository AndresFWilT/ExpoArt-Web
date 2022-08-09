from UserGeneral import Usuario

class Decorator(Usuario):
    usuario: Usuario = None

    def __init__(self, usuario:Usuario) -> None:
        self.usuario = usuario

    def getUsuario(self) -> Usuario:
        return self.usuario

    def operaciones(self):
        return self.usuario.operaciones()
