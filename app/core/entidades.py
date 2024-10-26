from dataclasses import dataclass

@dataclass
class Tarea:
    id: int
    titulo: str
    descripcion: str
    completa: bool = False
