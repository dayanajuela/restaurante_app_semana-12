class Venta:
    def __init__(self, id_venta, id_usuario, productos, total):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.productos = productos
        self.total = total

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "productos": self.productos,
            "total": self.total
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            id_venta=datos.get("id_venta"),
            id_usuario=datos.get("id_usuario"),
            productos=datos.get("productos", []),
            total=datos.get("total", 0.0)
        )