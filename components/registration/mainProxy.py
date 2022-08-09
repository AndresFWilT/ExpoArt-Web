from Proxy.Servicio import Servicio
from Proxy.Proxy import Proxy
from Decorador.Estudiante import Estudiante
from UserGeneral import Usuario
from Decorador.Administrador import Administrador
from Decorador.Docente import Decente
from components.registration.Decorador.Docente import Docente

if __name__ == "__main__":
    """
    Decorator
    """
    
    usuario = Estudiante("Juan", "Perez")

    docente = Docente(usuario)

    admin = Administrador(docente)

    """
    Cadena de mando
    """

    admin.setSiguiente(docente)
    docente.setSiguiente(usuario)

    rol = input('Digite el rol que desea asignar: ')

    admin.handle(rol)
    
    """
    Patron Proxy
    """
    servicio = Servicio()
    
    servicio.request(usuario.name_user, usuario.password, admin.type)
    
    proxy = Proxy(servicio)

    proxy.request(servicio.name_user, servicio.password, servicio.type)

