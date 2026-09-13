# Sistema de Gestión de Restaurante - Semana 13

Aplicación de escritorio desarrollada en Python utilizando Tkinter bajo la arquitectura Modelo-Vista-Controlador (MVC), con persistencia de datos en formato JSON y control de versiones integrado con Git y GitHub.

## 🚀 Novedades y Avances - Semana 13

En esta fase se completó la integración final del módulo de ventas y la persistencia completa del sistema:

* **Módulo de Ventas Integrado:** Desarrollo del flujo completo para agregar productos al carrito, calcular subtotales/totales dinámicamente y procesar la transacción.
* **Gestión y Control de Inventario:** Descuento automático de stock en el archivo `datos/productos.json` al confirmar cada venta de forma limpia y precisa.
* **Persistencia de Datos JSON:** 
  * Registro de transacciones históricas en `datos/ventas.json`.
  * Serialización de objetos utilizando los métodos `to_dict()` y `from_dict()` en todos los modelos (`Producto`, `Usuario`, `Venta`).
* **Manejo de Excepciones y Validaciones:**
  * Control de stock insuficiente antes de procesar ventas.
  * Normalización en la lectura/escritura de archivos JSON para prevenir errores en tiempo de ejecución.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Interfaz Gráfica:** Tkinter / ttk
* **Persistencia:** Archivos JSON (`productos.json`, `usuarios.json`, `ventas.json`)
* **Arquitectura:** MVC (Modelo - Vista - Controlador / Servicios)
* **Control de Versiones:** Git & GitHub

## 📁 Estructura del Proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   └── ... (vistas del sistema)
│
├── main.py
└── README.md