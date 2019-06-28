# Write a function that takes a normal time string and turns it into a military time string
# (ex. '02:00PM' -> '14:00')

def to_military_time(time):

    #slice_five = slice(0, 5)
    #slice_two = slice(0, 2)
    #slice_end = slice(2, 5)
    if time[5] == "P" or time[5] == "p":
        #int_time = int(time[slice_two]) + 12
        int_time = int(time[0] + time[1]) + 12
        if int_time == 24:
            int_time = 12
        #new_time = str(int_time) + time[slice_end]
        new_time = str(int_time) + time[2] + time[3] + time[4]
        if len(new_time) < 5:
            new_time = "0" + new_time
        if new_time[4] == "p":
            new_time = "0" + new_time[0] + new_time[1] + new_time[2] + new_time[3]
    else:
        #new_time = time[slice_five]
        if (time[0] + time[1]) == "12":
            new_time = "00" + time[2] + time[3] + time[4]
        else:
            new_time = time[0] + time[1] + time[2] + time[3] + time[4]
    return new_time


user_input_time = input("Using the following - 02:00PM - Please enter the time you want to convert: ")

print(to_military_time(user_input_time))


# Write a function that counts the number of integers that are duplicated in an array
# (ex. [3, 1, 4, 1, 5, 3, 3] -> 2)0638 

