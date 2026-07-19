# modelos/bebida.py
from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, precio: float, tamano: str, tipo_envase: str) -> None:
        # Enviamos los datos comunes a la clase padre (Producto)
        # y fijamos la categoría automáticamente como "Bebida"
        super().__init__(codigo, nombre, "Bebida", precio)
        self._tamano: str = tamano
        self._tipo_envase: str = tipo_envase

    # Sobrescribimos para aplicar Polimorfismo
    def mostrar_informacion(self) -> str:
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tamaño: {self._tamano} | Envase: {self._tipo_envase}"