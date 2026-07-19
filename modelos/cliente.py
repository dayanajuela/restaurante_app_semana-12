# modelos/cliente.py

class Cliente:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self._identificacion = identificacion
        self._nombre = nombre
        self._correo = correo

    @property
    def identificacion(self) -> str:
        return self._identificacion

    def mostrar_informacion(self) -> str:
        return f"[CLIENTE] ID: {self._identificacion} | Nombre: {self._nombre} | Correo: {self._correo}"