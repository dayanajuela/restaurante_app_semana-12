from typing import List, Optional, Set
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    """Clase servicio que administra la lógica de negocio y colecciones del restaurante."""
    
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = nombre
        # Uso obligatorio de listas para colecciones dinámicas de objetos
        self.__productos: List[Producto] = []
        self.__usuarios: List[Usuario] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    # ---------------- OPERACIONES DE PRODUCTOS ----------------

    def registrar_producto(self, producto: Producto) -> bool:
        """Agrega un nuevo producto verificando que el código no esté duplicado."""
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self.__productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su código único."""
        for p in self.__productos:
            if p.codigo.lower() == codigo.lower():
                return p
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        """Actualiza los datos de un producto existente."""
        prod = self.buscar_producto(codigo)
        if prod:
            prod.nombre = nuevo_nombre
            prod.categoria = nueva_categoria
            prod.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por su código único."""
        prod = self.buscar_producto(codigo)
        if prod:
            self.__productos.remove(prod)
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        """Retorna la lista de productos registrados."""
        return self.__productos

    # ---------------- OPERACIONES DE USUARIOS ----------------

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Agrega un nuevo usuario verificando que la identificación no esté duplicada."""
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False
        self.__usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario por su identificación única."""
        for u in self.__usuarios:
            if u.identificacion.lower() == identificacion.lower():
                return u
        return None

    def listar_usuarios(self) -> List[Usuario]:
        """Retorna la lista de usuarios registrados."""
        return self.__usuarios

    # ---------------- USO DE CONJUNTOS (SET) ----------------

    def obtener_categorias_unicas(self) -> Set[str]:
        """Uso de conjunto (set) para obtener categorías sin elementos duplicados."""
        return {prod.categoria for prod in self.__productos}