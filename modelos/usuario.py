class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str = ""):
        if not identificacion or not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()
        self.correo = correo.strip() if correo else ""

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @staticmethod
    def from_dict(data: dict):
        if not isinstance(data, dict):
            raise TypeError("Se esperaba un diccionario.")
        required_keys = ("identificacion", "nombre")
        if not all(k in data for k in required_keys):
            raise KeyError("Claves faltantes para reconstruir el Usuario.")
        return Usuario(
            identificacion=data["identificacion"],
            nombre=data["nombre"],
            correo=data.get("correo", "")
        )