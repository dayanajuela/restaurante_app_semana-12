import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Restaurante - Semana 13")
        
        # Tamaño inicial para que todo quepa en pantalla
        self.geometry("700x550")
        
        # Permitir redimensionar y maximizar la ventana
        self.resizable(True, True)
        
        self.servicio = RestauranteServicio()
        self.vista_actual = None
        self.mostrar_login()

    def mostrar_login(self):
        if self.vista_actual:
            self.vista_actual.destroy()
        self.vista_actual = LoginView(self, self.servicio, self.on_login_exitoso)
        self.vista_actual.pack(expand=True, fill=tk.BOTH)

    def on_login_exitoso(self, usuario):
        if self.vista_actual:
            self.vista_actual.destroy()
        self.vista_actual = MainView(self, self.servicio, usuario, self.mostrar_login)
        self.vista_actual.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    app = App()
    app.mainloop()