# modelos/producto.py

class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Al asignar usando self.nombre, self.categoria, etc., 
        # se disparan automáticamente las validaciones del @setter desde el constructor
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # --- ENCAPSULAMIENTO Y PROPIEDADES (@property) ---

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = valor

    # --- MÉTODO DE PRESENTACIÓN (POLIMORFISMO) ---
    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Estado: {estado}"