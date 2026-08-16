# Sistema de Gestión de Restaurante - Semana 9

**Estudiante:** Keyder Dayana Juela Huanca  
**Materia:** Programación Orientada a Objetos  

---

## 📌 Descripción del Sistema
Evolución del proyecto `restaurante_app` mediante la integración práctica de estructuras de datos dinámicas y estáticas (`list`, `tuple`, `dict`, `set`), manteniendo una arquitectura modular limpia y aplicando la correcta separación de responsabilidades entre los modelos de datos, la lógica de servicios y la interacción por consola.

---

## 🛠️ Justificación de Estructuras de Datos

* **Listas (`list`):** Administran las colecciones dinámicas de `productos` y `usuarios` en el servicio `Restaurante`. Permiten agregar, buscar, actualizar y eliminar objetos en tiempo de ejecución.
* **Tuplas (`tuple`):** Almacenan la constante `OPCIONES_MENU` en `main.py`. Se utiliza por ser una estructura inmutable que garantiza la integridad de las opciones del menú.
* **Diccionarios (`dict`):** Relacionan la opción seleccionada por el usuario con su respectiva función en el menú (`acciones`). Permiten ejecutar acciones de forma directa sin usar bloques condicionales extensos (`if-elif`).
* **Conjuntos (`set`):** Utilizados en el método `obtener_categorias_unicas()` para extraer y presentar únicamente las categorías de los productos registrados sin duplicados.

---

## 📁 Estructura del Proyecto
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
---

## 🚀 Instrucciones de Ejecución

1. Abrir una terminal en la carpeta raíz del proyecto (`restaurante_app/`).
2. Ejecutar el script principal con el siguiente comando:
   ```bash
   python main.py
   ```
   3. Interactuar con las opciones desplegadas en consola (1 al 9).

---

## 💡 Reflexión sobre la Selección de Estructuras de Datos

Seleccionar la estructura de datos adecuada según las necesidades del problema es esencial para escribir código eficiente, mantenible y legible. El uso de **listas** provee flexibilidad para colecciones cambiantes, mientras que las **tuplas** aportan seguridad para valores inmutables. Por su parte, los **diccionarios** simplifican el control de flujo al mapear claves a funciones, y los **conjuntos** resuelven la unicidad de datos de forma nativa. Aplicar cada estructura en el contexto correcto optimiza tanto el rendimiento como la claridad de la arquitectura.