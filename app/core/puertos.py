from abc import ABC, abstractmethod
from typing import List
from .entidades import Tarea

class RepositorioTarea(ABC):
    @abstractmethod
    def agregar_tarea(self, tarea: Tarea) -> Tarea:
        pass

    @abstractmethod
    def obtener_tareas(self) -> List[Tarea]:
        pass

    @abstractmethod
    def actualizar_tarea(self, tarea: Tarea) -> Tarea:
        pass

    @abstractmethod
    def eliminar_tarea(self, tarea_id: int) -> None:
        pass
