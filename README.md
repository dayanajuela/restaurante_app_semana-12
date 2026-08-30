# Sistema de Gestión de Restaurante - Semana 11

## Descripción del Sistema
Este sistema desarrollado en Python amplía las funcionalidades del proyecto `restaurante_app`, incorporando la gestión de ventas, el control automático de stock y la persistencia de datos mediante archivos en formato JSON para Productos, Usuarios y Ventas.

## Estructura del Proyecto
```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md
## Responsabilidad de Componentes
​Modelos (modelos/): Clases Producto, Usuario y Venta encargadas de representar las entidades fundamentales con validaciones internas e intercambio con diccionarios (to_dict y from_dict).
​Servicio de Archivos (servicios/archivo_servicio.py): Maneja exclusivamente la lectura y escritura en disco con codificación UTF-8 e invocaciones de json.load() y json.dump().
​Servicio Restaurante (servicios/restaurante.py): Contiene la lógica central del negocio: registro, búsquedas y la validación/ejecución del método vender_producto.
​Interfaz de Consola (main.py): Captura de datos interactiva del usuario con input(), despliegue de menús y captura organizada de excepciones.
## ​Persistencia e Interacción con JSON
​Los datos son almacenados en tres archivos JSON dentro de la carpeta datos/:
​productos.json: Guarda la lista de productos actualizando el stock disponible.
​usuarios.json: Guarda el registro de usuarios.
​ventas.json: Almacena el historial de transacciones asociadas al ID de usuario y Código de producto.
​Al iniciar la aplicación, las colecciones de objetos Producto, Usuario y Venta se reconstruyen dinámicamente desde sus respectivos archivos JSON.
## ​Excepciones Controladas
​Se gestionaron explícitamente las siguientes excepciones sin hacer uso de except: pass:
​ValueError: Para validaciones de lógica de negocio (cantidades <= 0, stock insuficiente, duplicados) e ingresos inválidos.
​FileNotFoundError / JSONDecodeError: Para manejar la ausencia o lectura de archivos corruptos inicializando colecciones vacías.
​PermissionError: Ante restricciones de lectura/escritura en el sistema operativo.
## ​Pruebas Realizadas
​Registro: Registro de usuarios y productos con stock inicial.
​Realización de Venta Válida: Ejecución de compras de productos comprobando el descuento automático de stock y el guardado en ventas.json.
​Rechazo por Stock Insuficiente: Intento de compra con cantidad mayor al stock disponible, confirmando el rechazo de la transacción sin alterar el inventario.
​Verificación de Persistencia: Cierre y reapertura de la aplicación verificando que los datos de usuarios, productos, stock actualizado y historial de ventas se mantienen intactos.

