task_list = []

class Task():
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority


def add_task_input():
    title_input = input("Please select a Title for the Task: ")
    while true:
        priority_input = input("Please select a Priority Level for the Task [High, Medium, Low]")
        if priority_input == ("l" or "L" or "low" or "Low" or "LOW"):
            priority = "LOW"
        elif priority_input == ("m" or "M" or "medium" or "Medium" or "MEDIUM"):
            priority = "MEDIUM"
        elif priority_input == ("h" or "H" or "high" or "HIGH" or "High"):
            priority = "HIGH"
        else:
            print("Input not entered correctly.")
    return (title_input, priority)

def remove_task_input():
    view_task_list()
    user_input = input("Select which task you would like to delete: ")
    task_list.remove(str(user_input))
    print("Task Deleted Successfully!")

def view_task_list():
    if len(task_list) == 0:
        print("There are no tasks in your task list.")
    else:
        counter = 1
        for item in task_list:
            print(counter + item.title + item.priority)
            counter += 1
    



user_input = ""

while user_input != "q":
    user_input = input("Press 1 to add task\nPress 2 to delete task\nPress 3 to view all tasks\nPress q to quit ")
    if user_input == "1":
        add_task_input()

    if user_input == "2":
        pass
    if user_input == "3":
        view_task_list()
        user_response = input("Press m to return to menu, or press q to quit.")
        if user_response == "q":
            user_input = "q"
    if user_input == "q":
        break
    else:
        print("Please select one of the available options!")