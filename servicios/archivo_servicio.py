import json
import os
from modelos.producto import Producto

class ArchivoServicio:
    def __init__(self, ruta_archivo: str = "datos/productos.json"):
        self.ruta_archivo = ruta_archivo
        self._asegurar_directorio()

    def _asegurar_directorio(self):
        directorio = os.path.dirname(self.ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

    def cargar_productos(self) -> list[Producto]:
        productos = []
        if not os.path.exists(self.ruta_archivo):
            return productos

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    try:
                        p = Producto(
                            codigo=item["codigo"],
                            nombre=item["nombre"],
                            categoria=item["categoria"],
                            precio=float(item["precio"])
                        )
                        productos.append(p)
                    except (KeyError, ValueError) as e:
                        print(f"Aviso: Registro omitido por datos inválidos -> {e}")
        except FileNotFoundError:
            print("Archivo no encontrado. Se iniciará con lista vacía.")
        except json.JSONDecodeError:
            print("Error: Formato JSON inválido.")
        except PermissionError:
            print("Error: Permisos insuficientes para leer el archivo.")
        
        return productos

    def guardar_productos(self, productos: list[Producto]) -> bool:
        try:
            lista_dict = [p.to_dict() for p in productos]
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(lista_dict, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("Error: Permisos insuficientes para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"Error al guardar datos: {e}")
            return False