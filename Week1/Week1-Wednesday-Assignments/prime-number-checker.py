def user_input():
    while True: #Checking to be sure the user is entering an integer
        try:
            number = input("Enter a number to check if it's prime: ")
            number = int(number)
            while number < 0: #Making sure the user enters a positive integer
                print("Please select a positive integer!")
                number = input("Enter a number to check if it's prime: ")
                number = int(number)
            break
        except ValueError:
            print("Please enter an integer instead!")
    return number

def prime_number_check(number):
    
    checker = True
    nums = []
    string = ""
    full_string = ""
    while number > 1: # Print statements precoded for 1 and 0
        for index in range(2, number):
            if number % index == 0:
                nums.append(index) #Gathering an array of numbers that are factors of the argument
                checker = False
        for index in range(0, len(nums)): #Creating a string out of the array of factors from the argument
            if index == len(nums) - 1:
                string += str(nums[index])
            else:
                string += str(nums[index]) + ", "
        full_string = "It has " + str(len(nums)) + " factors which are the following: " + string
        break
    return checker, full_string

def print_results(user_number = 1, checker = "", string = ""):
    while user_number > 1:
        if checker == True:
            results = "is a Prime Number!"
        else:
            results = "is not a Prime Number... " + string
        print(f"Here are the results! The number you entered, '{user_number}', {results}")
        break
    if user_number < 2: # Print statements precoded for 1 and 0
        if user_number == 1:
                print("Here are the results! The number you entered, '1', is a Prime Number!")
        if user_number == 0:
                print("Here are the results! The number you entered, '0', is kind of a Prime Number? Definitely no factors there!")

user_number = user_input()

results_checker, results_factors = prime_number_check(user_number)

print_results(user_number, results_checker, results_factors)