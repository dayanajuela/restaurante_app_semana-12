# Sistema de Gestión de Restaurante - Semana 14

Aplicación de escritorio desarrollada en Python con Tkinter y ttk, aplicando la arquitectura Modelo-Vista-Controlador (MVC), persistencia en archivos JSON y control de versiones con Git/GitHub.

## 🚀 Novedades y Avances - Semana 14

En esta fase se evolucionó la interfaz gráfica incorporando componentes y contenedores para organizar la información y permitir la gestión completa de productos:

* **Organización mediante Contenedores (Frames/LabelFrames):** Estructuración modular de la ventana principal separando las áreas de formulario, acciones y visualización de datos.
* **Módulo CRUD de Productos:**
  * **Registro:** Formulario interactivo con campos (`Entry`, `Spinbox`, `Combobox`) para agregar nuevos productos.
  * **Consulta/Carga:** Visualización dinámica de los datos almacenados.
  * **Actualización:** Modificación de datos y stock de productos existentes.
  * **Eliminación:** Remoción de elementos directamente desde la interfaz.
* **Persistencia y Separación de Responsabilidades:** Todas las operaciones pasan a través de `RestauranteServicio`, garantizando que la UI no maneje lógica de negocio ni manipulación directa de archivos JSON.
* **Manejo de Eventos y Controles:** Uso del parámetro `command=` en botones para la activación de acciones.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Interfaz Gráfica:** Tkinter / ttk (`LabelFrame`, `Frame`, `Entry`, `Button`, `Treeview`)
* **Persistencia:** Archivos JSON (`productos.json`, `usuarios.json`)
* **Arquitectura:** MVC (Modelo - Vista - Controlador / Servicios)
* **Control de Versiones:** Git & GitHub

## 📁 Estructura del Proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/ (opcional)
├── main.py
└── README.md