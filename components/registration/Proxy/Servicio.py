from ServicioLogin import ServicioLogin

class Servicio(ServicioLogin):
    
    def request(self, id_user, password, rol) -> None:
        self.id_user = id_user
        self.password = password
        self.rol = rol
