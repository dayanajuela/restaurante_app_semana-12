# Sistema Básico de Gestión de Restaurante (POO)

## Información del Estudiante
* **Nombre Completo:** Keyder Dayana Juela Huanca
* **Materia:** Programación Orientada a Objetos
* **Actividad:** Tarea Académica - Organizacion Modular de un Sistema

---

## Descripción del Sistema
Este proyecto implementa un sistema básico de simulación y gestión interna para un restaurante empleando los pilares fundamentales de la Programación Orientada a Objetos (POO) en Python. El sistema permite modelar entidades individuales como platos o bebidas (`Producto`) y usuarios de las instalaciones (`Cliente`), centralizando su administración dentro de una clase de control lógico (`Restaurante`) mediante tipos de datos compuestos (listas).

---

## Importancia de la Estructura Modular e Identificadores Descriptivos

### 1. Estructura Modular e Importaciones
La correcta separación de carpetas y archivos permite aislar las responsabilidades del software. Al estructurar paquetes con archivos `__init__.py`, Python es capaz de reconocer directorios específicos (`modelos` y `servicios`) para importar componentes de forma limpia, promoviendo la escalabilidad, el mantenimiento eficiente y evitando fallas de acoplamiento de código.

### 2. Identificadores Descriptivos y Tipado Eficiente
El uso estricto de convenciones como `PascalCase` para clases y `snake_case` junto a anotaciones explícitas de tipo de datos (`str`, `int`, `float`, `bool`) mejora significativamente la legibilidad del código para terceros. Evitar variables genéricas asegura que el código sea autoexplicativo y disminuye drásticamente la tasa de errores de lógica durante el ciclo de desarrollo.

---

## Estructura Esperada del Repositorio

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
