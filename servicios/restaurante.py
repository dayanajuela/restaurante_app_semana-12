# servicios/restaurante.py
from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self) -> None:
        # Una sola lista común para Producto y Bebida (Polimorfismo / Liskov)
        self._productos = []
        self._clientes = []

    def registrar_producto(self, producto: Producto) -> bool:
        # Validación estricta de no repetición de códigos
        for p in self._productos:
            if p.codigo == producto.codigo:
                print("❌ Error: Ya existe un producto o bebida con este código.")
                return False
        self._productos.append(producto)
        print("✅ Registrado en el sistema de manera exitosa.")
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        # Validación de no repetición de identificaciones
        for c in self._clientes:
            if c.identificacion == cliente.identificacion:
                print("❌ Error: Ya existe un cliente con esta identificación.")
                return False
        self._clientes.append(cliente)
        print("✅ Cliente registrado de manera exitosa.")
        return True

    def listar_productos(self) -> None:
        if not self._productos:
            print("🫙 No hay productos ni bebidas registrados.")
            return
        print("\n--- LISTADO DE PRODUCTOS Y BEBIDAS ---")
        for p in self._productos:
            # Polimorfismo puro: sin usar condicionales "isinstance" para distinguir tipos
            print(p.mostrar_informacion())

    def listar_clientes(self) -> None:
        if not self._clientes:
            print("👤 No hay clientes registrados.")
            return
        print("\n--- LISTADO DE CLIENTES ---")
        for c in self._clientes:
            print(c.mostrar_informacion())