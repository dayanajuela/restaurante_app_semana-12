import json
import os

class ArchivoServicio:
    @staticmethod
    def cargar_datos(ruta_archivo: str) -> list:
        if not os.path.exists(ruta_archivo):
            return []
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError, PermissionError):
            return []

    @staticmethod
    def guardar_datos(ruta_archivo: str, datos: list) -> bool:
        try:
            os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
            return True
        except (PermissionError, OSError) as e:
            print(f"[ERROR DE ARCHIVO]: No se pudieron guardar los datos: {e}")
            return False