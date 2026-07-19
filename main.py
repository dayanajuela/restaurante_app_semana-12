# main.py
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

def mostrar_menu() -> None:
    print("\n========================================")
    print("         SISTEMA DE RESTAURANTE         ")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")

def menu_registrar_producto(servicio: Restaurante) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Ingrese el código único: ").strip()
    nombre = input("Ingrese el nombre del plato: ").strip()
    categoria = input("Ingrese la categoría (Platillo/Entrada/Postre): ").strip()
    try:
        precio = float(input("Ingrese el precio: "))
        if codigo and nombre and categoria:
            nuevo_prod = Producto(codigo, nombre, categoria, precio)
            servicio.registrar_producto(nuevo_prod)
        else:
            print("⚠️ Error: Todos los campos de texto son obligatorios.")
    except ValueError:
        print("⚠️ Error: El precio debe ser un número decimal válido.")

def menu_registrar_bebida(servicio: Restaurante) -> None:
    print("\n--- REGISTRAR BEBIDA ---")
    codigo = input("Ingrese el código único: ").strip()
    nombre = input("Ingrese el nombre de la bebida: ").strip()
    try:
        precio = float(input("Ingrese el precio: "))
        tamano = input("Ingrese el tamaño (ej. 500ml / 1L): ").strip()
        tipo_envase = input("Ingrese el tipo de envase (ej. Vidrio / Plástico): ").strip()
        
        if codigo and nombre and tamano and tipo_envase:
            nueva_bebida = Bebida(codigo, nombre, precio, tamano, tipo_envase)
            servicio.registrar_producto(nueva_bebida)
        else:
            print("⚠️ Error: Todos los campos son obligatorios.")
    except ValueError:
        print("⚠️ Error: El precio debe ser un número decimal válido.")

def menu_registrar_cliente(servicio: Restaurante) -> None:
    print("\n--- REGISTRAR CLIENTE ---")
    identificacion = input("Ingrese la Identificación (Cédula/RUC): ").strip()
    nombre = input("Ingrese el nombre completo: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()
    
    if identificacion and nombre and correo:
        nuevo_cliente = Cliente(identificacion, nombre, correo)
        servicio.registrar_cliente(nuevo_cliente)
    else:
        print("⚠️ Error: Todos los campos son obligatorios.")

def ejecutar_sistema() -> None:
    servicio_restaurante = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            menu_registrar_producto(servicio_restaurante)
        elif opcion == "2":
            menu_registrar_bebida(servicio_restaurante)
        elif opcion == "3":
            menu_registrar_cliente(servicio_restaurante)
        elif opcion == "4":
            servicio_restaurante.listar_productos()
        elif opcion == "5":
            servicio_restaurante.listar_clientes()
        elif opcion == "6":
            print("\n👋 ¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("❌ Opción inválida. Intente del 1 al 6.")

if __name__ == "__main__":
    ejecutar_sistema()