#FIZZ BUZZ

#if the number is divisible by 3 thne you print "FIZZ"
#if the number is divisible by 5 then you print "BUZZ"
#if the number is divisible by 3 and 5 then you print "FIZZ BUZZ"

print("Welcome to FIZZ BUZZ!")
number = ""


while number != "q":
    while 1:
        try:
            number = input("Enter a number for the FIZZ BUZZ CHALLENGE: ")
            if number == "q":
                break
            number = int(number)
            break
        except ValueError:
            print("Please enter an integer instead!")
    if number == "q":
        print("Thanks for playing FIZZ BUZZ!")
        break
    if number % 3 == 0 and number % 5 == 0:
        print('FIZZ BUZZ')
    elif number % 3 == 0:
        print('FIZZ')
    elif number % 5 == 0:
        print('BUZZ')
    else:
        print("Your number wasn't fizzin' or buzzin', sorry!")
    print("At any time you can enter the letter 'q' to quit!")