#Defining the function to calculate tips from the total amount (total) and the tip percentage(tip_perc)
def tip_calculator(total, tip_perc = "15"):
    tip_total = round((float(total) * float(tip_perc) / 100), 2) 
    return print(f"Tip amount: ${tip_total}")

#User total input entered here
user_total = input("Please enter the total amount for the bill: ")

#User preferred percentage for the tip entered here
user_percent_pref = input("Please enter the percentage amount you would like to tip: ")

#Calling the Function to calculate the user's input to return the tip total amount
tip_calculator(user_total, user_percent_pref)