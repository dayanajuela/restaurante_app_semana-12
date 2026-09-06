from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:

    RUTA_PRODUCTOS = "datos/productos.json"
    RUTA_USUARIOS = "datos/usuarios.json"
    RUTA_VENTAS = "datos/ventas.json"

    def __init__(self):
        # Estructuras principales en memoria (optimización O(1) con diccionarios)
        self.productos = {}  # {codigo: objeto Producto}
        self.usuarios = {}   # {identificacion: objeto Usuario}
        self.ventas = []     # Listado histórico de ventas
        self.cargar_colecciones()

    def cargar_colecciones(self):
        """Carga los datos desde JSON e indexa las listas a diccionarios."""
        # Cargar Productos
        datos_p = ArchivoServicio.cargar_datos(self.RUTA_PRODUCTOS)
        self.productos = {
            item["codigo"]: Producto.from_dict(item) for item in datos_p
        }

        # Cargar Usuarios
        datos_u = ArchivoServicio.cargar_datos(self.RUTA_USUARIOS)
        self.usuarios = {
            item["identificacion"]: Usuario.from_dict(item) for item in datos_u
        }

        # Cargar Ventas
        datos_v = ArchivoServicio.cargar_datos(self.RUTA_VENTAS)
        self.ventas = [Venta.from_dict(item) for item in datos_v]

    def guardar_colecciones(self):
        """Sincroniza el estado actual de memoria con los archivos JSON."""
        lista_p = [p.to_dict() for p in self.productos.values()]
        lista_u = [u.to_dict() for u in self.usuarios.values()]
        lista_v = [v.to_dict() for v in self.ventas]

        ArchivoServicio.guardar_datos(self.RUTA_PRODUCTOS, lista_p)
        ArchivoServicio.guardar_datos(self.RUTA_USUARIOS, lista_u)
        ArchivoServicio.guardar_datos(self.RUTA_VENTAS, lista_v)

    def registrar_usuario(self, identificacion: str, nombre: str, correo: str = ""):
        identificacion = identificacion.strip()
        if identificacion in self.usuarios:
            raise ValueError(
                f"El usuario con identificación '{identificacion}' ya existe."
            )

        nuevo_usuario = Usuario(identificacion, nombre, correo)
        self.usuarios[identificacion] = nuevo_usuario
        self.guardar_colecciones()
        return nuevo_usuario

    def registrar_producto(
        self, codigo: str, nombre: str, precio: float, stock: int
    ):
        codigo = codigo.strip()
        if codigo in self.productos:
            raise ValueError(f"El producto con código '{codigo}' ya existe.")

        nuevo_producto = Producto(codigo, nombre, precio, stock)
        self.productos[codigo] = nuevo_producto
        self.guardar_colecciones()
        return nuevo_producto

    def vender_producto(
        self, identificacion_usuario: str, codigo_producto: str, cantidad: int
    ):
        identificacion_usuario = identificacion_usuario.strip()
        codigo_producto = codigo_producto.strip()

        # Búsqueda O(1) directa en diccionario de usuarios
        if identificacion_usuario not in self.usuarios:
            raise ValueError(
                f"El usuario '{identificacion_usuario}' no está registrado."
            )

        # Búsqueda O(1) directa en diccionario de productos
        if codigo_producto not in self.productos:
            raise ValueError(f"El producto '{codigo_producto}' no existe.")

        producto = self.productos[codigo_producto]

        # Validar stock y actualizar
        producto.reducir_stock(cantidad)

        # Crear transacción de venta
        nueva_venta = Venta(identificacion_usuario, codigo_producto, cantidad)
        self.ventas.append(nueva_venta)

        # Guardar cambios
        self.guardar_colecciones()
        return nueva_venta

    def obtener_ventas_usuario(self, identificacion_usuario: str) -> list:
        identificacion_usuario = identificacion_usuario.strip()
        if identificacion_usuario not in self.usuarios:
            raise ValueError(
                f"El usuario '{identificacion_usuario}' no está registrado."
            )

        return [
            v for v in self.ventas
            if v.identificacion_usuario == identificacion_usuario
        ]

    def obtener_productos(self) -> list:
        return list(self.productos.values())

    def obtener_usuarios(self) -> list:
        return list(self.usuarios.values())