# Class that manages tasks
class Tasks:
    def __init__(self) -> None:
        # Dictionary to store tasks, with the id as key
        self.tasks = {}
        # Variable to generate a unique id for each task
        self.task_id = 0

    # Method to add a new task
    def add_task(self, title, description, due_date, tag) -> None:
        self.task_id += 1
        # Store the task in the dictionary using the generated id
        self.tasks[self.task_id] = {
            "Id": self.task_id,
            "Title": title,
            "Description": description,
            "Due_Date": due_date,
            "Tag": tag,
        }

    # Method to list all registered tasks
    def list_tasks(self) -> str | None:
        if not self.tasks:
            return [] # Return an empty list if there are no tasks
        return list(self.tasks.values())

    # Method to edit an existing task
    def edit_tasks(
        self, id, new_title, new_description, new_due_date, new_tag
    ) -> bool:
        if not self.tasks:
            print("No tasks registered")
            return False
        # Update the task with the specified id
        self.tasks[id].update(
            {
                "Title": new_title,
                "Description": new_description,
                "Due_Date": new_due_date,
                "Tag": new_tag,
            }
        )
        return True

    # Method to delete an existing task
    def delete_task(self, id: int) -> bool:
        if not self.tasks:
            print("No tasks registered")
            return False
        for ids, tasks in self.tasks.items():
            if tasks["Id"] == id:
                del self.tasks[ids]
                return True
        return False

    # Method to search tasks by tag
    def search_task_by_tag(self, tag) -> list:
        return [
            tags
            for tags in self.tasks.values()
            if tags["Tag"] == tag
        ]

    # Method to search a task by its id
    def search_task_by_id(self, id) -> dict | None:
        return self.tasks.get(id, None)

    # Method to show task details
    def show_tasks(self, task) -> None:
        print(
            f"Id: {task['Id']}",
            f"Title: {task['Title']}",
            f"Description: {task['Description']}",
            f"Due Date: {task['Due_Date']}",
            f"Tag: {task['Tag']}",
            sep="\n",
        )
