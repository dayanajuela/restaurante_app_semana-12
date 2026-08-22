# Sistema de Gestión de Restaurante - Semana 10

## Descripción del Proyecto
Evolución del sistema de gestión de restaurante incorporando persistencia de datos mediante un archivo `JSON` y manejo de excepciones. Los productos registrados se guardan localmente para no perder la información al cerrar la aplicación.

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md 

