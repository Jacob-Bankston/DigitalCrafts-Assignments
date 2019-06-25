#Defining the function to create a greeting message
def greet(first_name, last_name):
    print(f"Hello! My name is {first_name} {last_name}.")

#Gathering the user input to declare their name
first_name = input("Please enter your first name for your greeting message: ")
last_name = input("Please enter your last name for your greeting message: ")

#call the function to produce the greeting message with the user's name
greet(first_name, last_name)