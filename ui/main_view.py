import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Toplevel):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Sistema de Restaurante - Gestión de Ventas")
        self.geometry("800x600")

        self.crear_widgets()

    def crear_widgets(self):
        # Marco Principal
        frame_ventas = ttk.LabelFrame(self, text="Ventas")
        frame_ventas.pack(fill="both", expand=True, padx=10, pady=10)

        lbl_sub = ttk.Label(frame_ventas, text="Registrar Venta", font=("Arial", 10, "bold"))
        lbl_sub.grid(row=0, column=0, columnspan=4, sticky="w", padx=5, pady=5)

        # Combobox Usuarios
        ttk.Label(frame_ventas, text="Usuario:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.combo_usuarios = ttk.Combobox(frame_ventas, state="readonly")
        self.combo_usuarios.grid(row=1, column=1, padx=5, pady=5)

        # Combobox Productos
        ttk.Label(frame_ventas, text="Producto:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.combo_productos = ttk.Combobox(frame_ventas, state="readonly")
        self.combo_productos.grid(row=1, column=3, padx=5, pady=5)

        # Botón Registrar Venta
        btn_registrar = ttk.Button(frame_ventas, text="Registrar Venta", command=self.registrar_venta)
        btn_registrar.grid(row=1, column=4, padx=10, pady=5)

        # Carga de datos desde RestauranteServicio
        self.cargar_datos_combos()

    def cargar_datos_combos(self):
        # Obtener listas tratadas de usuarios y productos
        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        self.combo_usuarios['values'] = usuarios
        if usuarios:
            self.combo_usuarios.current(0)

        self.combo_productos['values'] = productos
        if productos:
            self.combo_productos.current(0)

    def registrar_venta(self):
        usuario_sel = self.combo_usuarios.get()
        producto_sel = self.combo_productos.get()

        if not usuario_sel or not producto_sel:
            messagebox.showwarning("Atención", "Debe seleccionar un usuario y un producto.")
            return

        try:
            self.servicio.registrar_venta(usuario_sel, producto_sel)
            messagebox.showinfo("Éxito", "Venta registrada con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la venta: {e}")