from modelos.usuario import Usuario

class RestauranteServicio:
    # ... otros inicializadores y métodos existentes ...

    def obtener_usuarios(self):
        return self.usuarios

    def obtener_usuario_por_id(self, id_usuario):
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                return u
        return None

    def agregar_usuario(self, nombre, usuario, contrasena, rol):
        nuevo_id = max([u.id_usuario for u in self.usuarios], default=0) + 1
        nuevo_user = Usuario(nuevo_id, nombre, usuario, contrasena, rol)
        self.usuarios.append(nuevo_user)
        self._guardar_usuarios()
        return nuevo_user

    def actualizar_usuario(self, id_usuario, nombre, usuario, contrasena, rol):
        u = self.obtener_usuario_por_id(id_usuario)
        if u:
            u.nombre = nombre
            u.usuario = usuario
            if contrasena:  # Solo actualiza si no está vacía
                u.contrasena = contrasena
            u.rol = rol
            self._guardar_usuarios()
            return True
        return False

    def eliminar_usuario(self, id_usuario, usuario_actual_id):
        # Evitar que el administrador actual se elimine a sí mismo
        if id_usuario == usuario_actual_id:
            raise Exception("No puedes eliminar la cuenta con la que has iniciado sesión.")
        
        u = self.obtener_usuario_por_id(id_usuario)
        if u:
            self.usuarios.remove(u)
            self._guardar_usuarios()
            return True
        return False

    def _guardar_usuarios(self):
        # Utiliza tu archivo_servicio para guardar la lista en datos/usuarios.json
        datos = [u.to_dict() for u in self.usuarios]
        self.archivo_servicio.guardar_json("datos/usuarios.json", datos)