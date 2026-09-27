# 🍽️ Sistema de Gestión de Restaurante - Semana 14

Aplicación de escritorio desarrollada en Python utilizando **Tkinter** y **ttk**, implementando el patrón arquitectónico **Modelo-Vista-Controlador (MVC)**, persistencia de datos mediante archivos **JSON** y control de versiones con **Git/GitHub**[span_2](start_span)[span_2](end_span).

---

## 🚀 Novedades y Avances - Semana 14

En esta fase se evolucionó la interfaz gráfica incorporando componentes avanzados y contenedores para organizar la información y permitir la gestión completa del sistema[span_3](start_span)[span_3](end_span):

- **📦 Organización mediante Contenedores (`Frames` / `LabelFrames`):** Estructuración modular de la ventana principal para separar áreas de formulario, acciones y visualización de datos[span_4](start_span)[span_4](end_span).
- **🛠️ Módulo CRUD de Productos y Ventas:**
  - **Registro:** Formulario interactivo con campos (`Entry`, `Spinbox`, `Combobox`) para agregar y gestionar elementos[span_5](start_span)[span_5](end_span).
  - **Consulta / Carga:** Visualización dinámica de los datos almacenados en los archivos JSON[span_6](start_span)[span_6](end_span).
  - **Actualización:** Modificación en tiempo real de datos y stock[span_7](start_span)[span_7](end_span).
  - **Eliminación:** Remoción segura de elementos desde la interfaz[span_8](start_span)[span_8](end_span).
- **💾 Persistencia y Separación de Responsabilidades:** Todas las operaciones de datos se gestionan a través de `RestauranteServicio`, garantizando que la UI no maneje lógica de negocio ni manipulación directa de los archivos JSON[span_9](start_span)[span_9](end_span).
- **⚡ Manejo de Eventos y Controles:** Vinculación de acciones mediante `command=` y manejo de eventos del sistema[span_10](start_span)[span_10](end_span).

---

## 📁 Estructura del Proyecto

```text
restaurante_app/
│
├── assets/                  # Recurso gráfico (logos e imágenes)
│   └── logo.png
│
├── datos/                   # Archivos de almacenamiento persistente
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/                 # Clases de dominio del sistema
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/               # Lógica de negocio y persistencia
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/                      # Vistas e interfaz de usuario (Tkinter)
│   ├── login_view.py
│   └── main_view.py
│
├── main.py                  # Punto de entrada de la aplicación
└── README.md                # Documentación del proyecto