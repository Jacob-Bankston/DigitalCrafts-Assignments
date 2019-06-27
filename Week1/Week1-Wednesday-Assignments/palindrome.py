#Defining a Function to request user input of a string
def user_input():
    string = input("PALINDROME CHECKER: Please enter a string to check to see if it's a palindrome: ")
    return string

#Defining a function to reverse a string
def reverse_string(string): #new_string = string[::-1]
    new_string = ""
    for index in range((len(string) - 1), -1, -1):
        new_string += string[index]
    return new_string

#Defining a Function to Check if a string is a palindrome
def check_if_palindrome(string, reversed_string):
    new_string = ""
    new_reversed_string = ""
    for index in range(-1, (len(string) - 1)): #Checking to make sure that spaces aren't a factor in the string input
        if string[index] != " ":
            new_string += string[index]
    for index in range(-1, (len(reversed_string) - 1)): #Checking to make sure that spaces aren't a factor in the reversed_string input
        if reversed_string[index] != " ":
            new_reversed_string += reversed_string[index]
    if new_string == new_reversed_string:
        return True
    else:
        return False

#Defining a Function to print to the user whether or not their string is a palindrome
def palindrome_test_statement(tested_strings, string, reversed_string):
    if tested_strings == True:
        result_statement = "is a palindrome!"
    else:
        result_statement = "is not a palindrome... Sorry!"
    print(f'Results! Your string, "{string}" reverses to the string "{reversed_string}", which {result_statement}')

#Calling the function to request the user input
user_string = user_input()

#Calling the function to reverse the string from the user
reversed_user_string = reverse_string(user_string)

#Calling the function to test if the user input is a palindrome
boolean_test_value = check_if_palindrome(user_string, reversed_user_string)

#Calling the function to print the print statement to inform the user about their input
palindrome_test_statement(boolean_test_value, user_string, reversed_user_string)