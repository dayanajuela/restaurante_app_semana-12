class Usuario:
    def __init__(self, id_usuario, nombre, usuario, contrasena, rol="Cliente"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol  # 'Administrador', 'Empleado', 'Cliente'

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            id_usuario=data.get("id_usuario"),
            nombre=data.get("nombre"),
            usuario=data.get("usuario"),
            contrasena=data.get("contrasena"),
            rol=data.get("rol", "Cliente")
        )

    