class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        if not usuario_id or not usuario_id.strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")
        if not producto_codigo or not producto_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        self.usuario_id = usuario_id.strip()
        self.producto_codigo = producto_codigo.strip()
        self.cantidad = int(cantidad)

    def to_dict(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @staticmethod
    def from_dict(data: dict):
        if not isinstance(data, dict):
            raise TypeError("Se esperaba un diccionario.")
        required_keys = ("usuario_id", "producto_codigo", "cantidad")
        if not all(k in data for k in required_keys):
            raise KeyError("Claves faltantes para reconstruir la Venta.")
        return Venta(
            usuario_id=data["usuario_id"],
            producto_codigo=data["producto_codigo"],
            cantidad=data["cantidad"]
        )