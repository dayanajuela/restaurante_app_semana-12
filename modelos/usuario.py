class Usuario:
    def __init__(self, identificacion, nombre, rol, clave):
        self.identificacion = identificacion
        self.nombre = nombre
        self.rol = rol
        self.clave = clave

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "rol": self.rol,
            "clave": self.clave
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            identificacion=datos.get("identificacion"),
            nombre=datos.get("nombre"),
            rol=datos.get("rol"),
            clave=datos.get("clave")
        )

    