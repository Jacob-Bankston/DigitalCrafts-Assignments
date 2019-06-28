#Sum the Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 87, 66, 3]
numbers2 = [22, 45, 13, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
total_sum_numbers = 0
for number in numbers:
    total_sum_numbers += number
print(total_sum_numbers)

#Largest Number
largest_number = -100000000
for number in numbers:
    if largest_number < number:
        largest_number = number
print(largest_number)

#Smallest Number
smallest_number = 100000000000
for number in numbers:
    if smallest_number > number:
        smallest_number = number
print(smallest_number)

#Even Numbers
for number in numbers:
    if number % 2 == 0:
        print(number)

#Positive Numbers
for number in numbers:
    if number > 0:
        print(number)

#Positive Numbers 2
positives = []
for number in numbers:
    if number > 0:
        positives.append(number)

#Multiply a List
factored_list = []
factor = 5
for number in numbers:
    factored_list.append(number * factor)
print(factored_list)

#Multiply the Vectors
multiplied_lists = []
for index in range(0, len(numbers)):
    multiplied_lists.append(numbers[index] * numbers2[index])

#Matrix Addition
