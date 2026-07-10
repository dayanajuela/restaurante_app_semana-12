from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str

    # Método de presentación (Polimorfismo con la firma de Producto)
    def mostrar_informacion(self) -> str:
        return f"Cliente ID: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}"