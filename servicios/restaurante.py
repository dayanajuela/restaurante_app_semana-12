from modelos.producto import Producto

class Restaurante:
    def __init__(self, nombre: str = "Mi Restaurante"):
        self.nombre = nombre
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> bool:
        for p in self.productos:
            if p.codigo == producto.codigo:
                print("Error: Ya existe un producto con este código.")
                return False
        self.productos.append(producto)
        return True

    def registrar_producto(self, producto: Producto) -> bool:
        return self.agregar_producto(producto)

    def obtener_productos(self) -> list[Producto]:
        return self.productos

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def buscar_producto(self, codigo: str) -> Producto | None:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float) -> bool:
        prod = self.buscar_producto(codigo)
        if prod:
            prod.nombre = nombre
            prod.categoria = categoria
            prod.precio = precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        prod = self.buscar_producto(codigo)
        if prod:
            self.productos.remove(prod)
            return True
        return False