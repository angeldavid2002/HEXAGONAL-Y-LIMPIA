import sqlite3
from app.core.entidades import Tarea
from app.core.puertos import RepositorioTarea

class RepositorioTareaSQLite(RepositorioTarea):
    def __init__(self, db_path="tareas.db"):
        # Configuración de la conexión SQLite para permitir el acceso en múltiples hilos
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._crear_tabla()

    def _crear_tabla(self):
        """Crea la tabla de tareas si no existe."""
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS tareas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    descripcion TEXT,
                    completa BOOLEAN NOT NULL CHECK (completa IN (0, 1))
                )
            """)

    def agregar_tarea(self, tarea: Tarea):
        """Inserta una nueva tarea en la base de datos."""
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO tareas (titulo, descripcion, completa) VALUES (?, ?, ?)",
                (tarea.titulo, tarea.descripcion, tarea.completa)
            )
            tarea.id = cursor.lastrowid  # Asigna el ID autogenerado a la tarea

    def obtener_tareas(self):
        """Obtiene todas las tareas de la base de datos."""
        cursor = self.conn.execute("SELECT id, titulo, descripcion, completa FROM tareas")
        tareas = [
            Tarea(id=row[0], titulo=row[1], descripcion=row[2], completa=bool(row[3]))
            for row in cursor.fetchall()
        ]
        return tareas

    def obtener_tarea_por_id(self, tarea_id: int):
        """Obtiene una tarea específica por su ID."""
        cursor = self.conn.execute(
            "SELECT id, titulo, descripcion, completa FROM tareas WHERE id = ?", (tarea_id,)
        )
        row = cursor.fetchone()
        if row:
            return Tarea(id=row[0], titulo=row[1], descripcion=row[2], completa=bool(row[3]))
        return None

    def actualizar_tarea(self, tarea_id: int, completa: bool):
        """Actualiza el estado de completitud de una tarea."""
        with self.conn:
            self.conn.execute(
                "UPDATE tareas SET completa = ? WHERE id = ?", (int(completa), tarea_id)
            )

    def eliminar_tarea(self, tarea_id: int):
        """Elimina una tarea de la base de datos por su ID."""
        with self.conn:
            self.conn.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
