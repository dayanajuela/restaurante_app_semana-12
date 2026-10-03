# Restaurante App - Semana 16

## Propósito y Evolución
Evolución del sistema de gestión de restaurante con arquitectura modular en Python y Tkinter, incorporando la gestión avanzada de usuarios, asignación de roles y control de acceso.

## Estructura del Proyecto
- `datos/`: Archivos JSON de persistencia (`productos.json`, `usuarios.json`, `ventas.json`).
- `modelos/`: Clases de datos del dominio (`producto.py`, `usuario.py`, `venta.py`).
- `servicios/`: Lógica de negocio y persistencia (`archivo_servicio.py`, `restaurante_servicio.py`).
- `ui/`: Interfaz gráfica Tkinter (`login_view.py`, `main_view.py`).
- `assets/`: Recursos gráficos e íconos (`logo.png`).
- `main.py`: Punto de entrada de la aplicación.

## Gestión de Usuarios y Roles
- **Administrador**: Acceso completo a la pestaña de "Gestión de Usuarios" para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y control de ventas.
- **Empleado / Cliente**: Acceso restringido únicamente a las vistas operativas de ventas.
- **Persistencia**: Todos los cambios se leen y almacenan en `datos/usuarios.json` mediante la capa de servicios.

## Eventos y Atajos de Teclado Implementados
- `<<TreeviewSelect>>`: Carga automáticamente los datos del usuario seleccionado de la tabla al formulario de edición.
- `<<ComboboxSelected>>`: Permite reaccionar a la selección dinámica del rol en la interfaz.
- `<Return>` (Tecla Enter): Acciona el guardado/registro del usuario activo.
- `<Escape>` (Tecla Esc): Limpia el formulario y deselecciona elementos del Treeview.
- `command=`: Botones vinculados a los métodos de la clase para reutilización de código.

## Instrucciones de Ejecución
1. Asegurarse de tener Python instalado.
2. Ejecutar la aplicación desde la raíz del proyecto:
   ```bash
   python main.py