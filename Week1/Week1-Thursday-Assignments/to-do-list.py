user_input = None
task_list = {}

def addTask():
    title_input = input("Please Enter the Title of your Task: ")
    priority_input = input("Priority Levels can be High, Medium or Low\nPlease Enter the Priority Level of your Task: ")
    task_list[title_input] = priority_input
    print("Task Added Successfully!")
    return task_list

def deleteTask(user_input):
    counter = 1
    for key in task_list.keys():
        if counter == user_input:
            del task_list[key]
            break
        counter += 1
    print(f"Task Deleted Successfully!")
    return task_list

def viewTasks():
    if len(task_list) == 0:
        print("There are no Tasks in your Task List")
    else:
        task_number = 0
        for (key, value) in task_list.items():
            print(f"{task_number + 1} - {key} - {value}")
            task_number += 1


while user_input != "q": #Looping to keep the program running while the user hasn't quit
    user_input = input("Press 1 to add task\nPress 2 to delete task\nPress 3 to view all tasks\nPress q to quit\n")
        
    while user_input == "1": # Adding a Task Menu
        task_list = addTask()
        user_response = input("Press y to return to the main menu\nPress any key to add another task\nPress q to quit\n")
        if user_response == "q":
            user_input = "q"
            break
        elif user_response == "y":
            break

    while user_input == "2": # Deleting a Task Menu
        viewTasks()
        while True:
            user_delete_request = input("Press the number of the task you want to delete, or press c to cancel: ")
            if user_delete_request == "c":
                break
            else:
                try:
                    user_delete_request_int = int(user_delete_request)
                    task_list = deleteTask(user_delete_request_int)
                    break
                except ValueError:
                    print("Invalid entry, please try again.")
        if user_delete_request == "c":
            break
        user_response = input("Press y to return to the main menu\nPress any key to delete another task\nPress q to quit\n")
        if user_response == "q":
            user_input = "q"
            break
        elif user_response == "y":
            break

    while user_input == "3": # View all tasks Menu
        viewTasks()
        user_response = input("Press y to return to the main menu\nPress q to quit\n")
        if user_response == "q":
            user_input = "q"
            break
        elif user_response == "y":
            break
        
    if user_input != "1" or user_input != "2" or user_input != "3" or user_input != "q":
        print("Please enter a listed option instead.")