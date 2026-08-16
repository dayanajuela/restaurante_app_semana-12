class Usuario:
    """Clase general que representa un usuario registrado en el sistema."""
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.__identificacion: str = identificacion
        self.__nombre: str = nombre
        self.__correo: str = correo

    @property
    def identificacion(self) -> str:
        return self.__identificacion

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo: str) -> None:
        self.__correo = nuevo_correo

    def __str__(self) -> str:
        return f"ID: {self.__identificacion} | Nombre: {self.__nombre} | Correo: {self.__correo}"