import tkinter as tk
from tkinter import ttk, messagebox

class MainView(ttk.Frame):
    def __init__(self, parent, servicio, usuario_actual, on_logout):
        super().__init__(parent)
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.on_logout = on_logout
        self.carrito = []  # Lista temporal para la venta actual

        self.crear_encabezado()
        self.crear_pestanias()

    def crear_encabezado(self):
        frame_top = ttk.Frame(self, padding=10)
        frame_top.pack(fill=tk.X)

        lbl_user = ttk.Label(
            frame_top, 
            text=f"Usuario: {self.usuario_actual.nombre} | Rol: {self.usuario_actual.rol}",
            font=("Arial", 10, "bold")
        )
        lbl_user.pack(side=tk.LEFT)

        btn_logout = ttk.Button(frame_top, text="Cerrar Sesión", command=self.on_logout)
        btn_logout.pack(side=tk.RIGHT)

    def crear_pestanias(self):
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Pestaña 1: Productos
        tab_productos = ttk.Frame(notebook)
        notebook.add(tab_productos, text="Productos")
        self.configurar_tab_productos(tab_productos)

        # Pestaña 2: Usuarios
        tab_usuarios = ttk.Frame(notebook)
        notebook.add(tab_usuarios, text="Usuarios")
        self.configurar_tab_usuarios(tab_usuarios)

        # Pestaña 3: Ventas
        tab_ventas = ttk.Frame(notebook)
        notebook.add(tab_ventas, text="Ventas")
        self.configurar_tab_ventas(tab_ventas)

    # --- PESTAÑA PRODUCTOS ---
    def configurar_tab_productos(self, parent):
        columnas = ("Codigo", "Nombre", "Precio", "Stock")
        tree = ttk.Treeview(parent, columns=columnas, show="headings")
        
        tree.heading("Codigo", text="Código")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio ($)")
        tree.heading("Stock", text="Stock")

        tree.column("Codigo", width=80, anchor=tk.CENTER)
        tree.column("Nombre", width=200, anchor=tk.W)
        tree.column("Precio", width=100, anchor=tk.E)
        tree.column("Stock", width=80, anchor=tk.CENTER)

        tree.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        for p in self.servicio.obtener_productos():
            tree.insert("", tk.END, values=(p.codigo, p.nombre, f"${p.precio:.2f}", p.stock))

    # --- PESTAÑA USUARIOS ---
    def configurar_tab_usuarios(self, parent):
        columnas = ("Identificacion", "Nombre", "Rol")
        tree = ttk.Treeview(parent, columns=columnas, show="headings")
        
        tree.heading("Identificacion", text="Identificación")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Rol", text="Rol")

        tree.column("Identificacion", width=120, anchor=tk.CENTER)
        tree.column("Nombre", width=220, anchor=tk.W)
        tree.column("Rol", width=120, anchor=tk.CENTER)

        tree.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        for u in self.servicio.obtener_usuarios():
            tree.insert("", tk.END, values=(u.identificacion, u.nombre, u.rol))

    # --- PESTAÑA VENTAS ---
    def configurar_tab_ventas(self, parent):
        frame_controles = ttk.LabelFrame(parent, text="Agregar al Carrito", padding=10)
        frame_controles.pack(fill=tk.X, padx=5, pady=5)

        ttk.Label(frame_controles, text="Producto:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        
        self.productos_dict = {f"{p.nombre} (${p.precio:.2f})": p for p in self.servicio.obtener_productos()}
        self.combo_productos = ttk.Combobox(
            frame_controles, 
            values=list(self.productos_dict.keys()), 
            state="readonly", 
            width=30
        )
        self.combo_productos.grid(row=0, column=1, padx=5, pady=5)
        if self.productos_dict:
            self.combo_productos.current(0)

        ttk.Label(frame_controles, text="Cantidad:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.spin_cantidad = ttk.Spinbox(frame_controles, from_=1, to=100, width=5)
        self.spin_cantidad.set(1)
        self.spin_cantidad.grid(row=0, column=3, padx=5, pady=5)

        btn_agregar = ttk.Button(frame_controles, text="Agregar Producto", command=self.agregar_al_carrito)
        btn_agregar.grid(row=0, column=4, padx=10, pady=5)

        frame_tabla = ttk.LabelFrame(parent, text="Carrito de Compras", padding=10)
        frame_tabla.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        columnas = ("Nombre", "Precio", "Cantidad", "Subtotal")
        self.tree_carrito = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        
        self.tree_carrito.heading("Nombre", text="Producto")
        self.tree_carrito.heading("Precio", text="Precio U.")
        self.tree_carrito.heading("Cantidad", text="Cantidad")
        self.tree_carrito.heading("Subtotal", text="Subtotal")

        self.tree_carrito.column("Nombre", width=200, anchor=tk.W)
        self.tree_carrito.column("Precio", width=100, anchor=tk.E)
        self.tree_carrito.column("Cantidad", width=80, anchor=tk.CENTER)
        self.tree_carrito.column("Subtotal", width=100, anchor=tk.E)

        self.tree_carrito.pack(expand=True, fill=tk.BOTH)

        frame_total = ttk.Frame(parent, padding=10)
        frame_total.pack(fill=tk.X, padx=5, pady=5)

        self.lbl_total = ttk.Label(frame_total, text="Total: $0.00", font=("Arial", 12, "bold"))
        self.lbl_total.pack(side=tk.LEFT)

        btn_registrar = ttk.Button(frame_total, text="Registrar Venta", command=self.registrar_venta)
        btn_registrar.pack(side=tk.RIGHT)

    def agregar_al_carrito(self):
        prod_seleccionado_str = self.combo_productos.get()
        if not prod_seleccionado_str:
            messagebox.showwarning("Atención", "Seleccione un producto válido.")
            return

        producto = self.productos_dict[prod_seleccionado_str]
        try:
            cantidad = int(self.spin_cantidad.get())
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida mayor a 0.")
            return

        if cantidad > producto.stock:
            messagebox.showwarning("Stock Insuficiente", f"Solo hay {producto.stock} unidades en stock.")
            return

        for item in self.carrito:
            if item["producto"].codigo == producto.codigo:
                if item["cantidad"] + cantidad > producto.stock:
                    messagebox.showwarning("Stock Insuficiente", "Supera el stock disponible.")
                    return
                item["cantidad"] += cantidad
                break
        else:
            self.carrito.append({"producto": producto, "cantidad": cantidad})

        self.actualizar_vista_carrito()

    def actualizar_vista_carrito(self):
        for fila in self.tree_carrito.get_children():
            self.tree_carrito.delete(fila)

        total = 0.0
        for item in self.carrito:
            p = item["producto"]
            cant = item["cantidad"]
            subtotal = p.precio * cant
            total += subtotal
            self.tree_carrito.insert("", tk.END, values=(p.nombre, f"${p.precio:.2f}", cant, f"${subtotal:.2f}"))

        self.lbl_total.config(text=f"Total: ${total:.2f}")

    def registrar_venta(self):
        if not self.carrito:
            messagebox.showwarning("Carrito Vacío", "No hay productos en el carrito para procesar.")
            return

        exito, mensaje = self.servicio.registrar_venta(self.usuario_actual.identificacion, self.carrito)
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.carrito.clear()
            self.actualizar_vista_carrito()
        else:
            messagebox.showerror("Error", mensaje)