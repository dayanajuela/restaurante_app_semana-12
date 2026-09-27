from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self):
        self.archivo_servicio = ArchivoServicio()
        
        # Rutas de los archivos JSON de datos
        self.ruta_usuarios = "datos/usuarios.json"
        self.ruta_productos = "datos/productos.json"
        self.ruta_ventas = "datos/ventas.json"
        
        # Carga inicial de datos
        self.usuarios = self.cargar_usuarios()
        self.productos = self.cargar_productos()
        self.ventas = self.cargar_ventas()

    # --- CARGA DE DATOS DESDE JSON ---

    def cargar_usuarios(self):
        datos = self.archivo_servicio.cargar_json(self.ruta_usuarios)
        usuarios = []
        for u in datos:
            if isinstance(u, dict):
                ident = u.get("identificacion") or u.get("id", "")
                nombre = u.get("nombre", "")
                rol = u.get("rol", "Cliente")
                clave = u.get("clave", "")
                usuarios.append(Usuario(ident, nombre, rol, clave))
            else:
                usuarios.append(u)
        return usuarios

    def cargar_productos(self):
        datos = self.archivo_servicio.cargar_json(self.ruta_productos)
        productos = []
        for index, p in enumerate(datos, start=1):
            if isinstance(p, dict):
                # Busca 'codigo' o 'id' para evitar enviar un código vacío
                codigo = p.get("codigo") or p.get("id") or f"P0{index}"
                nombre = p.get("nombre", "Sin nombre")
                precio = p.get("precio", 0.0)
                productos.append(Producto(str(codigo), nombre, precio))
            else:
                productos.append(p)
        return productos

    def cargar_ventas(self):
        datos = self.archivo_servicio.cargar_json(self.ruta_ventas)
        ventas = []
        for v in datos:
            if isinstance(v, dict):
                v_id = v.get("id", 0)
                usuario = v.get("usuario", "")
                producto = v.get("producto", "")
                ventas.append(Venta(v_id, usuario, producto))
            else:
                ventas.append(v)
        return ventas

    # --- AUTENTICACIÓN ---

    def autenticar(self, identificacion, clave):
        for u in self.usuarios:
            u_ident = getattr(u, 'identificacion', None) or (u.get('identificacion') if isinstance(u, dict) else None)
            u_clave = getattr(u, 'clave', None) or (u.get('clave') if isinstance(u, dict) else None)
            
            if str(u_ident) == str(identificacion) and str(u_clave) == str(clave):
                return u
        return None

    # Alias para compatibilidad con la llamada desde LoginView
    def autenticar_usuario(self, identificacion, clave):
        usr = self.autenticar(identificacion, clave)
        if usr:
            return True, usr
        return False, None

    # --- MÉTODOS PARA COMBOBOX / INTERFAZ ---

    def obtener_usuarios(self):
        lista_nombres = []
        for u in self.usuarios:
            if hasattr(u, 'nombre'):
                lista_nombres.append(u.nombre)
            elif isinstance(u, dict):
                lista_nombres.append(u.get('nombre', 'Sin nombre'))
            else:
                lista_nombres.append(str(u))
        return lista_nombres

    def obtener_productos(self):
        lista_prods = []
        for p in self.productos:
            if hasattr(p, 'nombre'):
                lista_prods.append(p.nombre)
            elif isinstance(p, dict):
                lista_prods.append(p.get('nombre', 'Sin producto'))
            else:
                lista_prods.append(str(p))
        return lista_prods

    def obtener_ventas(self):
        return self.ventas

    # --- REGISTRO Y PERSISTENCIA DE VENTAS ---

    def registrar_venta(self, usuario, producto):
        if not usuario or not producto:
            raise ValueError("Debe seleccionar un usuario y un producto")

        nuevo_id = len(self.ventas) + 1
        usr_nombre = usuario.nombre if hasattr(usuario, 'nombre') else str(usuario)
        prod_nombre = producto.nombre if hasattr(producto, 'nombre') else str(producto)

        nueva_venta = Venta(nuevo_id, usr_nombre, prod_nombre)
        self.ventas.append(nueva_venta)
        
        self.guardar_ventas()
        return nueva_venta

    def guardar_ventas(self):
        datos_guardar = []
        for v in self.ventas:
            if hasattr(v, '__dict__'):
                datos_guardar.append({
                    "id": getattr(v, 'id', 0),
                    "usuario": getattr(v, 'usuario', ''),
                    "producto": getattr(v, 'producto', '')
                })
            elif isinstance(v, dict):
                datos_guardar.append(v)
                
        self.archivo_servicio.guardar_json(self.ruta_ventas, datos_guardar)