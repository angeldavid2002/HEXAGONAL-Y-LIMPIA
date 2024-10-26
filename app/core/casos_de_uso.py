from typing import List
from .entidades import Tarea
from .puertos import RepositorioTarea

class GestionTareas:
    def __init__(self, repositorio: RepositorioTarea):
        self.repositorio = repositorio

    def agregar_tarea(self, tarea: Tarea) -> Tarea:
        return self.repositorio.agregar_tarea(tarea)

    def obtener_tareas(self) -> List[Tarea]:
        return self.repositorio.obtener_tareas()

    def actualizar_tarea(self, tarea: Tarea) -> Tarea:
        return self.repositorio.actualizar_tarea(tarea)

    def eliminar_tarea(self, tarea_id: int) -> None:
        self.repositorio.eliminar_tarea(tarea_id)
        
    def marcar_completada(self, tarea_id: int, completa: bool):
        """Actualiza el estado de una tarea (completa o no completa)."""
        self.repositorio.actualizar_tarea(tarea_id, completa)