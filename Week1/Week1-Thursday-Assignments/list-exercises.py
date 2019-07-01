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

# #Multiply the Vectors
multiplied_lists = []
for index in range(0, len(numbers)):
    multiplied_lists.append(numbers[index] * numbers2[index])
print(multiplied_lists)

#Matrix Addition
matrix1 = [[3, 4], [5, 6]]
matrix2 = [[2, 3], [2, 3]]
sum_matrix = []
new_matrix = []
for index in range(0, 2):
    for i in range(0, 2):
        sum_matrix.append(matrix1[index][i] + matrix2[index][i])
for index in range(0, 3, 2):
    new_matrix.append([sum_matrix[index], sum_matrix[index + 1]])
print(new_matrix)

#Matrix Addition 2
matrix3 = [[3, 4], [5, 6], [7, 8], [9, 10]]
matrix4 = [[2, 3], [2, 3], [3, 2], [1, 4]]
sum_matrix2 = []
new_matrix2 = []
for index in range(0, len(matrix3)):
    for i in range(0, 2):
        sum_matrix2.append(matrix3[index][i] + matrix4[index][i])
for index in range(0, len(sum_matrix2), 2):
    new_matrix2.append([sum_matrix2[index], sum_matrix2[index + 1]])
print(new_matrix2)

#De-dup
new_string_array = []
string_array = ['Mary', 'Joseph', 'John', 'Andy', 'Andy', 'Andy', 'Mary', 'John', 'Jacob', 'Elianne', 'John', 'Andy', 'Andy']
for item in string_array:
    if item not in new_string_array:
        new_string_array.append(item)
print(new_string_array)

#Bonus: Matrix Multiplication
matrix5 = [[3, 4], [5, 6]]
matrix6 = [[2, 3], [2, 3]]
sum_matrix3 = [[0, 0], [0, 0]]

for i in range(0, 2): #creating a list of the multiplied matrix locations
    for j in range(0, 2):
        for k in range(0, 2):
            sum_matrix3[i][j] += matrix5[i][k] * matrix6[k][j]
print(sum_matrix3)