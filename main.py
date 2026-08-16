from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# Tupla para información estable del sistema (Opciones inmutables)
OPCIONES_MENU = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Ver categorías únicas (Set)",
    "9. Salir"
)

def mostrar_menu() -> None:
    print("\n==========================================")
    print("      SISTEMA DE GESTIÓN RESTAURANTE      ")
    print("==========================================")
    for opcion in OPCIONES_MENU:
        print(opcion)
    print("==========================================")

def menu_registrar_producto(servicio: Restaurante) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Ingrese el código único: ").strip()
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría: ").strip()
    
    if not codigo or not nombre or not categoria:
        print("❌ Error: Todos los campos son obligatorios.")
        return

    try:
        precio = float(input("Ingrese el precio ($): "))
        if precio <= 0:
            print("❌ Error: El precio debe ser un número positivo.")
            return
    except ValueError:
        print("❌ Error: Ingrese un valor numérico válido para el precio.")
        return

    nuevo_prod = Producto(codigo, nombre, categoria, precio)
    if servicio.registrar_producto(nuevo_prod):
        print("✅ Producto registrado exitosamente.")
    else:
        print("❌ Error: Ya existe un producto registrado con ese código.")

def menu_buscar_producto(servicio: Restaurante) -> None:
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Ingrese el código a buscar: ").strip()
    prod = servicio.buscar_producto(codigo)
    if prod:
        print(f"✅ Encontrado: {prod}")
    else:
        print("❌ Producto no encontrado.")

def menu_actualizar_producto(servicio: Restaurante) -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    if not servicio.buscar_producto(codigo):
        print("❌ Producto no encontrado.")
        return

    nombre = input("Ingrese el nuevo nombre: ").strip()
    categoria = input("Ingrese la nueva categoría: ").strip()
    try:
        precio = float(input("Ingrese el nuevo precio ($): "))
        if precio <= 0:
            print("❌ Error: El precio debe ser un valor positivo.")
            return
    except ValueError:
        print("❌ Error: El precio ingresado no es válido.")
        return

    if servicio.actualizar_producto(codigo, nombre, categoria, precio):
        print("✅ Producto actualizado exitosamente.")

def menu_eliminar_producto(servicio: Restaurante) -> None:
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if servicio.eliminar_producto(codigo):
        print("✅ Producto eliminado exitosamente.")
    else:
        print("❌ Error: No se encontró el producto con ese código.")

def menu_listar_productos(servicio: Restaurante) -> None:
    print("\n--- LISTA DE PRODUCTOS ---")
    productos = servicio.listar_productos()
    if not productos:
        print("No hay productos registrados en el sistema.")
    else:
        for p in productos:
            print(p)

def menu_registrar_usuario(servicio: Restaurante) -> None:
    print("\n--- REGISTRAR USUARIO ---")
    identificacion = input("Ingrese la identificación/ID único: ").strip()
    nombre = input("Ingrese el nombre completo: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()

    if not identificacion or not nombre or not correo:
        print("❌ Error: Todos los campos de usuario son obligatorios.")
        return

    nuevo_usuario = Usuario(identificacion, nombre, correo)
    if servicio.registrar_usuario(nuevo_usuario):
        print("✅ Usuario registrado exitosamente.")
    else:
        print("❌ Error: Ya existe un usuario registrado con esa identificación.")

def menu_listar_usuarios(servicio: Restaurante) -> None:
    print("\n--- LISTA DE USUARIOS ---")
    usuarios = servicio.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados en el sistema.")
    else:
        for u in usuarios:
            print(u)

def menu_ver_categorias(servicio: Restaurante) -> None:
    print("\n--- CATEGORÍAS ÚNICAS REGISTRADAS (SET) ---")
    categorias = servicio.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías disponibles aún.")
    else:
        for cat in categorias:
            print(f"• {cat}")

def main() -> None:
    servicio_restaurante = Restaurante("Mi Restaurante Gourmet")

    # Diccionario para mapear opciones con funciones (Relación clave -> valor)
    acciones = {
        "1": menu_registrar_producto,
        "2": menu_buscar_producto,
        "3": menu_actualizar_producto,
        "4": menu_eliminar_producto,
        "5": menu_listar_productos,
        "6": menu_registrar_usuario,
        "7": menu_listar_usuarios,
        "8": menu_ver_categorias,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "9":
            print("\n👋 ¡Gracias por usar el sistema! Hasta luego.")
            break

        accion = acciones.get(opcion)
        if accion:
            accion(servicio_restaurante)
        else:
            print("❌ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()