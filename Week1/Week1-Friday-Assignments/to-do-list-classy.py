class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

task_list = []

# class Task_List():
#     def __init__(self, name):
#         self.name = name

#     def add_task(self, title, priority):
#         self.title = input("Please select a Title for the Task: ")
#         while True:
#             priority_input = input("Please select a Priority Level for the Task [High, Medium, Low]")
#             if priority_input == ("l" or "L" or "low" or "Low" or "LOW"):
#                 self.priority = "LOW"
#             elif priority_input == ("m" or "M" or "medium" or "Medium" or "MEDIUM"):
#                 self.priority = "MEDIUM"
#             elif priority_input == ("h" or "H" or "high" or "HIGH" or "High"):
#                 self.priority = "HIGH"
#             else:
#                 print("Input not entered correctly.")
    
#     def del_task(self, task):1
#         del task
#         print("Task Deleted Successfully!")

def add_task_input():
    title = input("Please select a Title for the Task: ")
    while True:
        priority_input = input("Please select a Priority Level for the Task [High - h, Medium - m, Low - l]: ")
        priority = priority_levels(priority_input)
        if priority == False:
            print("ERROR: Input not entered correctly.\n")
        else:
            break
    return (title, priority)

def priority_levels(pinput):
    if 'l' in pinput:
        return "LOW"
    if 'm' in pinput:
        return "MEDIUM"
    if 'h' in pinput:
        return "HIGH"
    else:
        return False

def task_creator(title, priority):
    new_task = Task(title, priority)
    return new_task

def remove_task_input(task_to_remove):
    task_list.remove(task_list[task_to_remove - 1])
    print("Task Deleted Successfully!\n")

def view_task_list():
    if len(task_list) == 0:
        print("There are no tasks in your task list.\n")
    else:
        counter = 1
        for item in task_list:
            print(f"{spacing2}{counter} - {item.title} - {item.priority}")
            counter += 1

user_input = ""
out_going_message = "Thanks for using the Task List Manager app!\n+++          I Love You!          +++"
spacing = "        + "
spacing2 = "          "

print("       ++++++++++++++++++++++\nWelcome to your new Task List Manager!\n       ++++++++++++++++++++++")

while user_input != "q":
    print("           ++ Main Menu ++")
    counter = 0
    user_input = input(f"{spacing}Press 1 to add task\n{spacing}Press 2 to delete task\n{spacing}Press 3 to view all tasks\n{spacing}Press q to quit\n")

    if user_input == "1":
        add_input = "a"
        while add_input == "a":
            title, priority = add_task_input()
            task_list.append(task_creator(title, priority))
            add_input = input(f"{spacing}If you would like to add another task press 'a'.\n{spacing}Press any key to return to the main menu.\n")
        counter = 1

    if user_input == "2":
        print("-----------------------------------------------------------------------------------------------------")
        view_task_list()
        while counter == 0:
            delete_input = input(f"{spacing}Select which task you would like to delete, or press c to cancel: ")
            if delete_input == "c":
                counter = 1
                pass
            else:
                try:
                    number = int(delete_input)
                    if number > len(task_list) or number < 1:
                        print("ERROR: Entered value is not in the task list.\n")
                    else:
                        remove_task_input(number)
                        counter = 1
                except ValueError:
                    print("ERROR: Please enter a correct reponse.\n")


    if user_input == "3":
        print("        ++                             +++                            ++    ")
        view_task_list()
        user_response = input(f"{spacing}Press m to return to menu, or press q to quit.\n")
        counter = 1
        if user_response == "q":
            print(out_going_message)
            break

    if user_input == "q":
        print(out_going_message)
        break

    elif counter == 0:
        print("ERROR: Please select one of the available options!")