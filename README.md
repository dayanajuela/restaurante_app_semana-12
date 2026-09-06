# Sistema de Gestión de Restaurante - Semana 12

## Descripción del Proyecto
Evolución del sistema de gestión de restaurante enfocada en la **optimización del rendimiento** mediante la incorporación de estructuras de datos orientadas a búsquedas de alta eficiencia ($O(1)$). Se reestructuró la capa de servicios para reemplazar el recorrido lineal de listas por diccionarios hash indexados por claves únicas (`identificacion` y `codigo`).

## Estructura del Proyecto
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── init.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── init.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
## Mejoras de Rendimiento Aplicadas (Semana 12)
1. **Indexación con Diccionarios**:
   - `self.productos`: Indexado mediante `{codigo: Objeto Producto}`.
   - `self.usuarios`: Indexado mediante `{identificacion: Objeto Usuario}`.
2. **Búsquedas de Complejidad $O(1)$**:
   - Validación de duplicados al registrar productos/usuarios de forma instantánea.
   - Localización directa de entidades durante las transacciones de venta sin recorrer colecciones completas.
3. **Mantenimiento del Modelo y Consola**:
   - Se preservó la compatibilidad total con la capa `main.py` y el formato de persistencia en archivos JSON (`datos/`).

## Ejecución del Proyecto
Para ejecutar la aplicación en consola:
```bash
python main.py