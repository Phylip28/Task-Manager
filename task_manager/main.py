# Import necessary classes and functions
from manager.tasks import Tasks  # Import the Tasks class from the tasks module
from manager.helpers import validate_data  # Import the validate_data function from the helpers module
from time import sleep  # Import the sleep function to make pauses in execution

# Function that displays the main system menu
def show_menu() -> None:
    print("\nTask Management System")
    print("1. Add task")
    print("2. List tasks")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Search tasks by tag")
    print("6. Exit")

# Create an instance of the Tasks class
task = Tasks()

# Main system loop
while True:
    show_menu()  # Show the menu

    try:
        # Ask the user to enter a menu option
        option = int(input("Choose an option: "))

        # Use match-case to execute the selected option
        match option:
            case 1:
                try:
                    while True:
                        # Request data for the new task
                        print("\n")
                        title = input("Enter the task title: ")
                        description = input("Description: ")
                        due_date = input("Due date (YYYY-MM-DD): ")
                        tag = input("Tag (optional): ")
                        print("Verifying data...")
                        sleep(1.5)
                        # Verify that the data is valid
                        if validate_data(title, description, due_date, tag):
                            task.add_task(
                                title, description, due_date, tag
                            )
                            print("Task added successfully.")
                            break
                except KeyboardInterrupt:
                    print("\nReturning to menu...")
            case 2:
                try:
                    # Show registered tasks
                    print("Loading registered tasks")
                    sleep(1.5)
                    task.list_tasks()
                except KeyboardInterrupt:
                    print("\nReturning to menu...")
            case 3:
                try:
                    # Request the task id to edit it
                    while True:
                        id = int(input("Enter the id of the task to modify: "))
                        print("Please wait a moment...")
                        sleep(1.5)
                        # Check if the task exists
                        if not task.search_task_by_id(id):
                            print("No task found with the specified id")
                            break
                        new_title = input("Enter the task title: ")
                        new_description = input("Description: ")
                        new_due_date = input("Due date (YYYY-MM-DD): ")
                        new_tag = input("Tag (optional): ")
                        print("Resolving changes...")
                        sleep(1.5)
                        # Verify that the data is valid before making the change
                        if validate_data(
                            new_title,
                            new_description,
                            new_due_date,
                            new_tag,
                        ):
                            task.edit_tasks(
                                id,
                                new_title,
                                new_description,
                                new_due_date,
                                new_tag,
                            )
                            print("Changes made successfully.")
                            break
                except KeyboardInterrupt:
                    print("\nReturning to menu...")
            case 4:
                try:
                    # Request the id of the task to delete
                    id = int(input("Enter the id of the task to delete: "))
                    print("Please wait a moment...")
                    sleep(1.5)
                    # Check if the task exists before deleting it
                    if not task.search_task_by_id(id):
                        print("No task found with the specified id")
                    else:
                        print("Deleting task...")
                        sleep(1.5)
                        task.delete_task(id)
                        print("Task deleted successfully.")
                except KeyboardInterrupt:
                    print("\nReturning to menu...")
            case 5:
                try:
                    # Request the search tag to list tasks
                    tag = input("Enter the search tag: ")
                    print("Searching tasks...")
                    sleep(1.5)
                    tasks = task.search_task_by_tag(tag)
                    # Show found tasks or a message if there are no results
                    if not tasks:
                        print("No tasks found with that tag")
                    else:
                        for t in tasks:
                            print("\n")
                            print(f'Task Id: {t["Id"]}')
                            print(f'Title: {t["Title"]}')
                            print(f'Description: {t["Description"]}')
                            print(f'Due Date: {t["Due_Date"]}')
                            print(f'Tag: {t["Tag"]}')
                except KeyboardInterrupt:
                    print("\nReturning to menu...")
            case 6:
                print("See you later!")
                break
    except ValueError:
        print("Please enter a valid number")
        continue
    except KeyboardInterrupt:
        print("\nReturning to main menu...")
