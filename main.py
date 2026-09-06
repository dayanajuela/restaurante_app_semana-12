from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n" + "="*45)
    print("   SISTEMA DE GESTIÓN DE RESTAURANTE - SEMANA 11")
    print("="*45)
    print("1. Registrar Usuario")
    print("2. Registrar Producto")
    print("3. Realizar Venta (vender_producto)")
    print("4. Consultar Ventas de un Usuario")
    print("5. Listar Productos y Stock Disponible")
    print("6. Listar Usuarios Registrados")
    print("7. Salir")
    print("="*45)

def ejecutar_aplicacion():
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            print("\n--- Registrar Nuevo Usuario ---")
            identificacion = input("Identificación/ID del usuario: ").strip()
            nombre = input("Nombre completo del usuario: ").strip()
            try:
                restaurante.registrar_usuario(identificacion, nombre)
                print(">> Usuario registrado exitosamente.")
            except ValueError as e:
                print(f">> [ERROR]: {e}")

        elif opcion == "2":
            print("\n--- Registrar Nuevo Producto ---")
            codigo = input("Código del producto: ").strip()
            nombre = input("Nombre del producto: ").strip()
            try:
                precio = float(input("Precio unitario: "))
                stock = int(input("Stock disponible: "))
                restaurante.registrar_producto(codigo, nombre, precio, stock)
                print(">> Producto registrado exitosamente.")
            except ValueError as e:
                print(f">> [ERROR de Ingreso/Validación]: {e}")

        elif opcion == "3":
            print("\n--- Realizar Venta ---")
            id_usuario = input("ID del usuario comprador: ").strip()
            cod_producto = input("Código del producto a vender: ").strip()
            try:
                cantidad = int(input("Cantidad a vender: "))
                if restaurante.vender_producto(cod_producto, id_usuario, cantidad):
                    print(">> ¡Venta realizada con éxito! Stock y registro de venta actualizados.")
            except ValueError as e:
                print(f">> [OPERACIÓN RECHAZADA]: {e}")

        elif opcion == "4":
            print("\n--- Consultar Ventas por Usuario ---")
            id_usuario = input("Ingrese ID del usuario a consultar: ").strip()
            try:
                ventas = restaurante.consultar_ventas_usuario(id_usuario)
                if not ventas:
                    print(f">> El usuario ID '{id_usuario}' no registra compras en el sistema.")
                else:
                    print(f"\nHistorial de Ventas del Usuario ID '{id_usuario}':")
                    for idx, v in enumerate(ventas, 1):
                        prod = restaurante.buscar_producto(v.producto_codigo)
                        nombre_prod = prod.nombre if prod else "Producto no encontrado"
                        print(f"  {idx}. Código Producto: {v.producto_codigo} ({nombre_prod}) | Cantidad: {v.cantidad}")
            except ValueError as e:
                print(f">> [ERROR]: {e}")

        elif opcion == "5":
            print("\n--- Inventario de Productos y Stock ---")
            productos = restaurante.obtener_productos()
            if not productos:
                print("No hay productos registrados en el sistema.")
            else:
                for p in productos:
                    print(f"Código: {p.codigo:<8} | Nombre: {p.nombre:<20} | Precio: ${p.precio:<7.2f} | Stock: {p.stock}")

        elif opcion == "6":
            print("\n--- Lista de Usuarios Registrados ---")
            usuarios = restaurante.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados en el sistema.")
            else:
                for u in usuarios:
                    print(f"ID: {u.identificacion:<10} | Nombre: {u.nombre}")

        elif opcion == "7":
            print("\nCerrando la aplicación... ¡Hasta luego!")
            break

        else:
            print("\n>> Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_aplicacion()