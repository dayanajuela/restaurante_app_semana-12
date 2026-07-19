# modelos/producto.py

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def precio(self) -> float:
        return self._precio

    def mostrar_informacion(self) -> str:
        return f"[{self._categoria.upper()}] Código: {self._codigo} | Nombre: {self._nombre} | Precio: ${self._precio:.2f}"
    