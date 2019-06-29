# Array Duplicate Remover

def array_duplicate_remover(array): # With the in function
    new_array = []
    for item in array:
        if item not in new_array:
            new_array.append(item)
    print(new_array)

new_array = []
def array_duplicate_remover2(array): # Without the in function
    for index in range(0, len(array)):
        if does_item_exist(array[index]):
            continue
        else:
            new_array.append(array[index])
    print(new_array)
            
def does_item_exist(item_to_search):
    found = False
    for item in new_array:
        if item == item_to_search:
            found = True
            break
    return found

# Array Largest Element

def largest_element(array):
    long_element_length = -1
    long_element_index = -1
    for index in range(0, len(array)):
        if len(array[index]) > long_element_length:
            long_element_length = len(array[index])
            long_element_index = index
    return print(array[long_element_index])

# Array Smallest Element

def smallest_element(array):
    small_element_length = -1
    small_element_index = -1
    for index in range(0, len(array)):
        if len(array[index]) < small_element_length:
            small_element_length = len(array[index])
            small_element_index = index
    return print(array[small_element_index])

# Missing Element from Integer List

def missing_element(array): # With the in function
    missing_item = range(0, 9)
    for item in missing_item:
        if item not in array:
            missed_item = item
    print(missed_item)

def missing_element_2(array): #Without the in function
    for number in range(0, len(array) - 1):
        if number + 1 != array[number + 1]:
            missed_number = number + 1
            break
    print(missed_number)

# Duplicate the Array

def duplicate_array(array):
    new_array = array + array
    print(new_array)

loves = ['Chocolate', 'Wife', 'Video Games', 'Wife', 'Stand Up Comedy', 'Wife', 'Family', 'Wife', 'Chocolate', 'Wife']
nums = [0, 1, 2, 3, 4, 5, 7, 8, 9]

#array_duplicate_remover(loves)
#array_duplicate_remover2(loves)
#largest_element(loves)
#smallest_element(loves)
#missing_element(nums)
#missing_element_2(nums)
#duplicate_array(nums)


# HARD Assignment - Write a program to display a pyramid as shown below

def pyramid_generator(n):
    i = 1
    j = n - 2
    star = "*"
    space = " "
    while i < n:
        stars = (i*2 - 1) * star
        spaces = space * j
        print(spaces + stars + spaces)
        i += 1
        j -= 1


user_selected_number = input("Select a number for how many rows you would like in the pyramid: ")
pyramid_generator(int(user_selected_number) + 1)