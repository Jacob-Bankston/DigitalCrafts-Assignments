# Write a function that takes a normal time string and turns it into a military time string
# (ex. '02:00PM' -> '14:00')

def to_military_time(time):
    
    slice_five = slice(0, 5)
    slice_two = slice(0, 2)
    slice_end = slice(2, 5)
    if time[5] == "P" or time[5] == "p":
        int_time = int(time[slice_two]) + 12
        new_time = str(int_time) + time[slice_end]
        if len(new_time) < 5:
            new_time = "0" + new_time
    else:
        new_time = time[slice_five]
    return new_time
    



# Write a function that counts the number of integers that are duplicated in an array
# (ex. [3, 1, 4, 1, 5, 3, 3] -> 2)0638 

user_input_time = input("Using the following - 02:00PM - Please enter the time you want to convert: ")

print(to_military_time(user_input_time))