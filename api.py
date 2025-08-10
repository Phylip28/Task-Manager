import fastapi
from Task_manager.gestor import Tareas

# Create a fastapi instance
app = fastapi.FastAPI()

# Create an instance of tasks
db_tareas = Tareas()

# Endpoint to list all tasks
@app.get("/tareas")
def get_tasks():
    """Return a list of all tasks"""
    tasks_list = db_tareas.listar_tareas()
    return {"tareas": tasks_list}

