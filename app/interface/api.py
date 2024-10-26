from fastapi import APIRouter, HTTPException
from app.core.casos_de_uso import GestionTareas
from app.infraestructura.repositorio_sqlite import RepositorioTareaSQLite
from app.core.entidades import Tarea

# Crear el enrutador de FastAPI
router = APIRouter()

# Inicializar la clase de gestión de tareas con el repositorio
repositorio = RepositorioTareaSQLite("tareas.db")
gestion_tareas = GestionTareas(repositorio)

@router.get("/tareas/")
async def listar_tareas():
    """Devuelve la lista de todas las tareas almacenadas."""
    try:
        return gestion_tareas.obtener_tareas()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tareas/")
async def crear_tarea(titulo: str, descripcion: str):
    """Crea una nueva tarea en la base de datos."""
    tarea = Tarea(id=None, titulo=titulo, descripcion=descripcion, completa=False)
    try:
        gestion_tareas.agregar_tarea(tarea)
        return {"mensaje": "Tarea creada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/tareas/{tarea_id}")
async def actualizar_tarea(tarea_id: int, completa: bool):
    """Actualiza el estado de una tarea por su ID."""
    try:
        gestion_tareas.marcar_completada(tarea_id, completa)
        return {"mensaje": "Tarea actualizada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/tareas/{tarea_id}")
async def eliminar_tarea(tarea_id: int):
    """Elimina una tarea de la base de datos por su ID."""
    try:
        gestion_tareas.eliminar_tarea(tarea_id)
        return {"mensaje": "Tarea eliminada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
