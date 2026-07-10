# main.py
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n=======================================")
    print("        SISTEMA DE RESTAURANTE        ")
    print("=======================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("---------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("---------------------------------------")
    print("7. Salir")

def ejecutar_sistema():
    # Instanciamos la clase de servicio principal
    mi_restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-7): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR NUEVO PRODUCTO ---")
            try:
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))
                
                # Se crea el objeto (aquí se disparan las validaciones de los setters)
                nuevo_prod = Producto(nombre, categoria, precio)
                mi_restaurante.registrar_producto(nuevo_prod)
            except ValueError as e:
                # Captura el error si el precio es <= 0 o si los textos están vacíos
                print(f"❌ Error de validación: {e}")

        elif opcion == "2":
            mi_restaurante.listar_productos()

        elif opcion == "3":
            print("\n--- BUSCAR PRODUCTO ---")
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            producto = mi_restaurante.buscar_producto(nombre_buscar)
            if producto:
                print(f"🔍 Encontrado: {producto.mostrar_informacion()}")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "4":
            print("\n--- REGISTRAR NUEVO CLIENTE ---")
            nombre_cli = input("Nombre del cliente: ").strip()
            correo_cli = input("Correo electrónico: ").strip()
            id_cli = input("Identificador único (ID): ").strip()

            if not nombre_cli or not correo_cli or not id_cli:
                print("❌ Error: Ninguno de los campos del cliente puede estar vacío.")
            else:
                # Se crea usando el esquema de dataclass
                nuevo_cliente = Cliente(nombre_cli, correo_cli, id_cli)
                mi_restaurante.registrar_cliente(nuevo_cliente)

        elif opcion == "5":
            mi_restaurante.listar_clientes()

        elif opcion == "6":
            print("\n--- BUSCAR CLIENTE ---")
            id_buscar = input("Ingrese el ID del cliente a buscar: ")
            cliente = mi_restaurante.buscar_cliente(id_buscar)
            if cliente:
                print(f"🔍 Encontrado: {cliente.mostrar_informacion()}")
            else:
                print("❌ Cliente no encontrado.")

        elif opcion == "7":
            print("\nSaliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Por favor, seleccione un número del 1 al 7.")

if __name__ == "__main__":
    ejecutar_sistema()