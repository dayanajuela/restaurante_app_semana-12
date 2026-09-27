import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def main():
    root = tk.Tk()
    root.title("Sistema de Restaurante")
    root.geometry("400x350")

    servicio = RestauranteServicio()

    def on_login_exitoso(usuario):
        root.destroy()
        app = MainView(servicio)
        if hasattr(app, 'mainloop'):
            app.mainloop()

    login_vista = LoginView(root, servicio, on_login_exitoso)
    if hasattr(login_vista, 'pack'):
        login_vista.pack(fill="both", expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    main()