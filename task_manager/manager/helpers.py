# Import the datetime class from the datetime module to work with dates
from datetime import datetime

# Function that validates the data entered for the task
def validate_data(title, description, due_date, tag) -> bool:
    # Dictionary with the fields to validate
    fields = {
        "Title": title,
        "Description": description,
        "Due date": due_date,
        "Tag": tag,
    }
    # Check if any field is empty
    for field, value in fields.items():
        if not value:
            print(f"The {field} field cannot be empty.")
            return False
    try:
        # Check that the due date has the correct format
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("The due date is not a valid date")
        return False
    return True
