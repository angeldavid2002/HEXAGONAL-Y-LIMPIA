from fastapi import FastAPI
from app.interface.api import router

app = FastAPI()

# Registrar las rutas de la API
app.include_router(router, prefix="/tareas", tags=["Tareas"])
