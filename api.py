import fastapi
from task_manager.manager.tasks import Tasks

# Create a fastapi instance
app = fastapi.FastAPI()

# Create an instance of tasks
db_tasks = Tasks()

# Endpoint to list all tasks
@app.get("/tasks")
def get_tasks():
    """Return a list of all tasks"""
    tasks_list = db_tasks.list_tasks()
    return {"tasks": tasks_list}

