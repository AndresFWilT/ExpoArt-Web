from Decorador.Estudiante import Estudiante
from UserGeneral import Usuario
from Decorador.Administrador import Administrador
from Decorador.Docente import Docente

def estudiante_code(usuario: Usuario) -> None:
    print(f"{usuario.operaciones()}", end="")


if __name__=="__main__":

    usuarioSimple = Estudiante("Juan", "Perez")
    print("Estudiante")
    estudiante_code(usuarioSimple)

    decoradorDocente = Docente(usuarioSimple)
    print("Docente")
    estudiante_code(decoradorDocente)

    print("\n")

    decoradorAdministrador = Administrador (decoradorVendedor)
    print("Administardor")
    estudiante_code(decoradorAdministrador)