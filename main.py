from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto

def ejecutar_app():
    archivo_serv = ArchivoServicio()
    restaurante = Restaurante("Mi Restaurante")
    
    # Cargar datos guardados previamente en el JSON
    productos_guardados = archivo_serv.cargar_productos()
    for p in productos_guardados:
        restaurante.agregar_producto(p)

    while True:
        print("\n=== SISTEMA DE GESTIÓN DE RESTAURANTE (SEMANA 10) ===")
        print("1. Listar productos")
        print("2. Registrar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            prods = restaurante.obtener_productos()
            if not prods:
                print("No hay productos registrados.")
            else:
                for p in prods:
                    print(p)

        elif opcion == "2":
            try:
                codigo = input("Código del producto: ")
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))
                
                nuevo_prod = Producto(codigo, nombre, categoria, precio)
                if restaurante.agregar_producto(nuevo_prod):
                    archivo_serv.guardar_productos(restaurante.obtener_productos())
                    print("Producto guardado correctamente en JSON.")
            except ValueError as e:
                print(f"Error de entrada: {e}")

        elif opcion == "3":
            try:
                codigo = input("Código del producto a actualizar: ")
                nombre = input("Nuevo Nombre: ")
                categoria = input("Nueva Categoría: ")
                precio = float(input("Nuevo Precio: "))
                
                if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
                    archivo_serv.guardar_productos(restaurante.obtener_productos())
                    print("Producto actualizado exitosamente.")
                else:
                    print("No se encontró el producto.")
            except ValueError as e:
                print(f"Error de entrada: {e}")

        elif opcion == "4":
            codigo = input("Código del producto a eliminar: ")
            if restaurante.eliminar_producto(codigo):
                archivo_serv.guardar_productos(restaurante.obtener_productos())
                print("Producto eliminado correctamente.")
            else:
                print("No se encontró el producto.")

        elif opcion == "5":
            print("Saliendo de la aplicación...")
            break

if __name__ == "__main__":
    ejecutar_app()