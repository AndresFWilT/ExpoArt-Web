from CadenaDeResponsabilidad.Administrador import Administrador
from CadenaDeResponsabilidad.Docente import Docente
from CadenaDeResponsabilidad.Estudiante import Estudiante

if __name__ == "__main__":
    estudiante = Estudiante("Juan", "Perez")
    docente = Docente(estudiante)
    administrador = Administrador(docente)

    administrador.setSiguiente(docente)
    docente.setSiguiente(estudiante)

    rol = input('Digite el rol que desea asignar: ')

    administrador.handle(rol)
