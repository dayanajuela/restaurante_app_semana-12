from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self):
        self.ruta_productos = "datos/productos.json"
        self.ruta_usuarios = "datos/usuarios.json"
        self.ruta_ventas = "datos/ventas.json"

    # --- USUARIOS ---
    def obtener_usuarios(self):
        datos = ArchivoServicio.cargar_json(self.ruta_usuarios)
        return [Usuario.from_dict(d) for d in datos]

    def validar_acceso(self, identificacion, clave):
        usuarios = self.obtener_usuarios()
        for u in usuarios:
            if str(u.identificacion) == str(identificacion) and str(u.clave) == str(clave):
                return True, u
        return False, None

    # --- PRODUCTOS ---
    def obtener_productos(self):
        datos = ArchivoServicio.cargar_json(self.ruta_productos)
        return [Producto.from_dict(d) for d in datos]

    # --- VENTAS ---
    def obtener_ventas(self):
        datos = ArchivoServicio.cargar_json(self.ruta_ventas)
        return [Venta.from_dict(d) for d in datos]

    def registrar_venta(self, id_usuario, carrito):
        if not carrito:
            return False, "El carrito está vacío."

        productos = self.obtener_productos()

        # Validar stock para todos los elementos del carrito
        for item in carrito:
            val = item.get("codigo") or item.get("nombre") or item.get("producto")
            identificador = val.nombre if hasattr(val, 'nombre') else str(val)

            prod_encontrado = None
            for p in productos:
                if p.codigo == identificador or p.nombre in identificador or identificador in p.nombre:
                    prod_encontrado = p
                    break

            if not prod_encontrado or prod_encontrado.stock < item["cantidad"]:
                nombre_mostrar = prod_encontrado.nombre if prod_encontrado else identificador
                return False, f"Stock insuficiente para {nombre_mostrar}."

        # Descontar stock de la lista de productos
        for item in carrito:
            val = item.get("codigo") or item.get("nombre") or item.get("producto")
            identificador = val.nombre if hasattr(val, 'nombre') else str(val)

            for p in productos:
                if p.codigo == identificador or p.nombre in identificador or identificador in p.nombre:
                    p.stock -= item["cantidad"]
                    break

        # Guardar lista de productos actualizada
        datos_prod = [p.to_dict() for p in productos]
        ArchivoServicio.guardar_json(self.ruta_productos, datos_prod)

        # Formatear items del carrito y calcular subtotales
        carrito_limpio = []
        total = 0.0

        for item in carrito:
            val = item.get("producto") or item.get("nombre")
            nombre_str = val.nombre if hasattr(val, 'nombre') else str(val)
            
            cantidad = item.get("cantidad", 1)
            precio = item.get("precio", 0.0)
            subtotal = item.get("subtotal", cantidad * precio)
            
            total += subtotal

            carrito_limpio.append({
                "producto": nombre_str,
                "cantidad": cantidad,
                "precio": precio,
                "subtotal": subtotal
            })

        # Generar nueva venta y guardarla
        ventas = self.obtener_ventas()
        nueva_id = len(ventas) + 1
        
        nueva_venta = Venta(nueva_id, id_usuario, carrito_limpio, total)
        ventas.append(nueva_venta)

        datos_ventas = [v.to_dict() for v in ventas]
        ArchivoServicio.guardar_json(self.ruta_ventas, datos_ventas)

        return True, "Venta registrada con éxito."