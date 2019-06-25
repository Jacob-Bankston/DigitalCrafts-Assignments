#Defining a function to add two numbers together from user input
def add_numbers(input_1, input_2):
    total = input_1 + input_2
    return print(f"Your two numbers added together are: {total}")

#Seeking user input for the add_numbers function
while 1:
    try: #Checking for integer input on the first number's input
        first_number = input("Give me your first number to add: ")
        first_number = int(first_number)
        break
    except ValueError:
        print("Please enter an integer instead!")

while 1: 
    try: #Checking for integer input on the second number's input
        second_number = input("Give me your second number to add: ")
        second_number = int(second_number)
        break
    except ValueError:
        print("Please enter an integer instead!")

#Calling the function to check the integers
add_numbers(first_number, second_number)