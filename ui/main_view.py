import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Toplevel):
    def __init__(self, parent, servicio, usuario_actual):
        super().__init__(parent)
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.title("Sistema de Gestión de Restaurante")
        self.geometry("900x600")

        # Variable auxiliar para saber si estamos editando un usuario
        self.usuario_seleccionado_id = None

        self._crear_interfaz()

    def _crear_interfaz(self):
        # Notebook (Pestañas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña previa de Ventas/Productos
        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text="Ventas")
        self._construir_pestana_ventas()

        # Pestaña de Gestión de Usuarios (Restringida a Administrador)
        if self.usuario_actual.rol == "Administrador":
            self.tab_usuarios = ttk.Frame(self.notebook)
            self.notebook.add(self.tab_usuarios, text="Gestión de Usuarios")
            self._construir_pestana_usuarios()

    # --- PESTAÑA DE VENTAS (TU CÓDIGO EXISTENTE) ---
    def _construir_pestana_ventas(self):
        # Aquí mantienes tu UI previa de ventas
        frame = ttk.LabelFrame(self.tab_ventas, text="Registrar Venta")
        frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame, text="Usuario:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_usuarios = ttk.Combobox(frame, state="readonly")
        self.combo_usuarios.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Producto:").grid(row=0, column=2, padx=5, pady=5)
        self.combo_productos = ttk.Combobox(frame, state="readonly")
        self.combo_productos.grid(row=0, column=3, padx=5, pady=5)

        btn_venta = ttk.Button(frame, text="Registrar Venta", command=self.registrar_venta)
        btn_venta.grid(row=0, column=4, padx=5, pady=5)

    def registrar_venta(self):
        usuario_sel = self.combo_usuarios.get()
        producto_sel = self.combo_productos.get()

        if not usuario_sel or not producto_sel:
            messagebox.showwarning("Atención", "Debe seleccionar un usuario y un producto")
            return

        try:
            self.servicio.registrar_venta(usuario_sel, producto_sel)
            messagebox.showinfo("Éxito", "Venta registrada con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la venta: {e}")

    # --- PESTAÑA DE GESTIÓN DE USUARIOS (SEMANA 16) ---
    def _construir_pestana_usuarios(self):
        # Frame Formulario
        frame_form = ttk.LabelFrame(self.tab_usuarios, text="Formulario de Usuario")
        frame_form.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.txt_nombre = ttk.Entry(frame_form)
        self.txt_nombre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Usuario:").grid(row=0, column=2, padx=5, pady=5)
        self.txt_usuario = ttk.Entry(frame_form)
        self.txt_usuario.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5)
        self.txt_contrasena = ttk.Entry(frame_form, show="*")
        self.txt_contrasena.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Rol:").grid(row=1, column=2, padx=5, pady=5)
        self.combo_rol = ttk.Combobox(frame_form, values=["Administrador", "Empleado", "Cliente"], state="readonly")
        self.combo_rol.set("Cliente")
        self.combo_rol.grid(row=1, column=3, padx=5, pady=5)

        # Botones con command= (reutilizan callbacks)
        frame_btn = ttk.Frame(self.tab_usuarios)
        frame_btn.pack(fill="x", padx=10, pady=5)

        btn_guardar = ttk.Button(frame_btn, text="Guardar/Registrar", command=self.guardar_usuario)
        btn_guardar.pack(side="left", padx=5)

        btn_eliminar = ttk.Button(frame_btn, text="Eliminar", command=self.eliminar_usuario)
        btn_eliminar.pack(side="left", padx=5)

        btn_limpiar = ttk.Button(frame_btn, text="Limpiar (Esc)", command=self.limpiar_formulario)
        btn_limpiar.pack(side="left", padx=5)

        # Tabla Treeview
        frame_tabla = ttk.LabelFrame(self.tab_usuarios, text="Listado de Usuarios")
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

        self.tabla_usuarios = ttk.Treeview(
            frame_tabla, 
            columns=("ID", "Nombre", "Usuario", "Rol"), 
            show="headings"
        )
        self.tabla_usuarios.heading("ID", text="ID")
        self.tabla_usuarios.heading("Nombre", text="Nombre")
        self.tabla_usuarios.heading("Usuario", text="Usuario")
        self.tabla_usuarios.heading("Rol", text="Rol")
        self.tabla_usuarios.pack(fill="both", expand=True)

        # --- EVENTOS REQUERIDOS EN LA RÚBRICA ---
        # 1. <<TreeviewSelect>> mediante bind()
        self.tabla_usuarios.bind("<<TreeviewSelect>>", self.al_seleccionar_usuario)

        # 2. <<ComboboxSelected>> mediante bind()
        self.combo_rol.bind("<<ComboboxSelected>>", self.al_cambiar_rol)

        # 3. Atajos de Teclado (<Return> y <Escape>)
        self.bind("<Return>", lambda e: self.guardar_usuario())
        self.bind("<Escape>", lambda e: self.limpiar_formulario())

        # Cargar datos iniciales
        self.cargar_tabla_usuarios()

    # --- CALLBACKS Y MÉTODOS DE USUARIOS ---
    def cargar_tabla_usuarios(self):
        for item in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(item)

        for u in self.servicio.obtener_usuarios():
            # Sin mostrar contraseña sensible en la tabla
            self.tabla_usuarios.insert("", "end", values=(u.id_usuario, u.nombre, u.usuario, u.rol))

    def al_seleccionar_usuario(self, event):
        seleccion = self.tabla_usuarios.selection()
        if not seleccion:
            return
        
        item = self.tabla_usuarios.item(seleccion[0])
        valores = item["values"]

        self.usuario_seleccionado_id = valores[0]
        usuario_obj = self.servicio.obtener_usuario_por_id(self.usuario_seleccionado_id)

        if usuario_obj:
            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, usuario_obj.nombre)

            self.txt_usuario.delete(0, tk.END)
            self.txt_usuario.insert(0, usuario_obj.usuario)

            self.txt_contrasena.delete(0, tk.END)
            self.combo_rol.set(usuario_obj.rol)

    def al_cambiar_rol(self, event):
        # Evento virtual para reaccionar al cambio de selección en el Combobox
        pass

    def guardar_usuario(self):
        nombre = self.txt_nombre.get().strip()
        usuario = self.txt_usuario.get().strip()
        contrasena = self.txt_contrasena.get().strip()
        rol = self.combo_rol.get()

        if not nombre or not usuario:
            messagebox.showwarning("Atención", "Nombre y Usuario son obligatorios.")
            return

        try:
            if self.usuario_seleccionado_id:
                # Actualizar
                self.servicio.actualizar_usuario(self.usuario_seleccionado_id, nombre, usuario, contrasena, rol)
                messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
            else:
                # Registrar
                if not contrasena:
                    messagebox.showwarning("Atención", "La contraseña es requerida para un nuevo usuario.")
                    return
                self.servicio.agregar_usuario(nombre, usuario, contrasena, rol)
                messagebox.showinfo("Éxito", "Usuario registrado correctamente.")

            self.limpiar_formulario()
            self.cargar_tabla_usuarios()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

    def eliminar_usuario(self):
        if not self.usuario_seleccionado_id:
            messagebox.showwarning("Atención", "Seleccione un usuario de la tabla.")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el usuario seleccionado?")
        if confirmar:
            try:
                self.servicio.eliminar_usuario(self.usuario_seleccionado_id, self.usuario_actual.id_usuario)
                messagebox.showinfo("Éxito", "Usuario eliminado.")
                self.limpiar_formulario()
                self.cargar_tabla_usuarios()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def limpiar_formulario(self):
        self.usuario_seleccionado_id = None
        self.txt_nombre.delete(0, tk.END)
        self.txt_usuario.delete(0, tk.END)
        self.txt_contrasena.delete(0, tk.END)
        self.combo_rol.set("Cliente")
        if self.tabla_usuarios.selection():
            self.tabla_usuarios.selection_remove(self.tabla_usuarios.selection())