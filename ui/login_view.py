import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(ttk.Frame):
    def __init__(self, parent, servicio, on_login_success):
        super().__init__(parent)
        self.servicio = servicio
        self.on_login_success = on_login_success
        self.crear_widgets()

    def crear_widgets(self):
        lbl_titulo = ttk.Label(self, text="Acceso al Sistema de Restaurante", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=25)

        frame_form = ttk.Frame(self)
        frame_form.pack(pady=10)

        ttk.Label(frame_form, text="Usuario / ID:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.txt_usuario = ttk.Entry(frame_form, width=25)
        self.txt_usuario.grid(row=0, column=1, pady=5, padx=5)

        ttk.Label(frame_form, text="Contraseña:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.txt_clave = ttk.Entry(frame_form, show="*", width=25)
        self.txt_clave.grid(row=1, column=1, pady=5, padx=5)

        btn_ingresar = ttk.Button(self, text="Iniciar Sesión", command=self.ingresar)
        btn_ingresar.pack(pady=20)

    def ingresar(self):
        usuario = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        if not usuario or not clave:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return

        exito, usr_obj = self.servicio.validar_acceso(usuario, clave)
        if exito:
            self.txt_usuario.delete(0, tk.END)
            self.txt_clave.delete(0, tk.END)
            self.on_login_success(usr_obj)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")