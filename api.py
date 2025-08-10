import fastapi
from task_manager.manager.tasks import Tasks
from pydantic import BaseModel
from datetime import date

# Create a fastapi instance
app = fastapi.FastAPI()

# Create an instance of tasks
db_tasks = Tasks()

# Define a model for the tasks
def taskModel(BaseModel):
    title: str
    Description: str
    Due_Date: date
    Tag: str

# Endpoint to list all tasks
@app.get("/tasks")
def get_tasks():
    """Return a list of all tasks"""
    tasks_list = db_tasks.list_tasks()
    return {"tasks": tasks_list}

# Endpoint to search tasks by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """Return a specific task by its ID"""
    task = db_tasks.search_task_by_id(task_id)
    
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return {"task": task}

# Endpoint to add a new task
@app.post("/tasks")
def createTask(task: taskModel):
    """Create a new task"""
    new_task = db_tasks.add_task(**task.model_dump())
    
    return {"message": "Task created successfully", "task": new_task}

# Endpoint to edit an existing task
@app.put("/tasks/{task_id}")
def updateTask(task_id: int, task: taskModel):
    """Update an existing task by its ID"""
    
    # Validate if the task exists
    if not db_tasks.search_task_by_id(task_id):
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    
    task_data = updateTask.model_dump()
    db_tasks.edit_tasks(id=task_id, new_title=task_data['title'], new_description=task_data['Description'], new_due_date=task_data['Due_Date'], new_tag=task_data['Tag'])

    return {"message": f"Task {task_id} updated successfully", "task": task_data}

# Endpoint to delete a task
@app.delete("/tasks/{task_id}")
def deleteTask(task_id: int):
    """Delete a task by its ID"""

    if not db_tasks.search_task_by_id(task_id):
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    
    was_deleted = db_tasks.delete_task(task_id)
    return