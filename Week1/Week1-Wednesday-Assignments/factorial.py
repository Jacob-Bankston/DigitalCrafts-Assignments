#Defining a function to create factorials
def create_factorial(number):
    factorial = 1
    while number != 0:
        factorial = factorial * number
        number -= 1
    return factorial

#Defining a function to ask for user input, checking that they are entering an integer
def user_integer_input():
    while 1:
        try:
            number = input("Please enter a number to get the factorial of: ")
            number = int(number)
            break
        except ValueError:
            print("Please enter an integer instead!")
    return number

#Defining a function to print the factorial print statement
def factorial_print_statement(factorial_number, original_number):
    print(f"The factorial for your number, {original_number}, is {factorial_number}")

#Calling the function to get the user's integer
user_integer = user_integer_input()

#Calling the function to convert the user's integer into a factorial
factorial = create_factorial(user_integer)

#Calling the function to print the statement of the results
factorial_print_statement(user_integer, factorial)