from Decorador.Administrador import Administrador
from Decorador.Estudiante import Estudiante
from Decorador.UserGeneral import Usuario
from Decorador.Docente import Docente
from ServicioLogin import ServicioLogin
from Servicio import Servicio

class Proxy(ServicioLogin):
    def __init__(self, usuario: Usuario)-> None:
        self.servicio = Servicio()
        self.usuario = usuario

    def request(self, db, id_user, password)-> Usuario:
        self.usuario = Estudiante(id_user, password)
        
        if(self.verificarLogin(db, id_user, password)):
            return self.accesoDeLogueo(db, id_user, password)
        else:
            return self.usuario

    def verificarLogin(self, db, id_user, password)-> bool:

        try:
            conn = db.connect("expoart.db")
            cur = conn.cursor()
            # Realizamos el Query. 
            check = cur.execute('select * from users where email_user=? and password=?', (id_user, password))
            if check.fetchone():
                return True
            else:
                return False
        finally:
            cur.close()
            conn.close()

    def accesoDeLogueo(self, db, id_user, password)-> None:

        conn = db.connect("users.db")
        cur = conn.cursor()
        user = cur.execute('select * from users where email_user=? and password=?', (id_user, password))
        cur.close()
        conn.close()
        
        if user.Rol == "Docente":
            return Docente(self.usuario)
        elif user.Rol == "Administrador":
            return Administrador(self.usuario)
        
