class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int = 0):
        if not codigo or not codigo.strip():
            raise ValueError("El código no puede estar vacío.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.stock = int(stock)

    def reducir_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente.")
        self.stock -= cantidad

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data: dict):
        if not isinstance(data, dict):
            raise TypeError("Se esperaba un diccionario.")
        required_keys = ("codigo", "nombre", "precio", "stock")
        if not all(k in data for k in required_keys):
            raise KeyError("Claves faltantes para reconstruir el Producto.")
        return Producto(
            codigo=data["codigo"],
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data["stock"]
        )