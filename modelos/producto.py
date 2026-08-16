# modelos/producto.py

class Producto:
    """Clase que representa un producto del restaurante."""
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.__codigo: str = codigo
        self.__nombre: str = nombre
        self.__categoria: str = categoria
        self.__precio: float = precio

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str) -> None:
        self.__categoria = nueva_categoria

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        self.__precio = nuevo_precio

    def __str__(self) -> str:
        return f"[{self.__codigo}] {self.__nombre} | Categoría: {self.__categoria} | Precio: ${self.__precio:.2f}"