import re

#Exercise 1

phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

# print(phonebook_dict['Elizabeth'])
# phonebook_dict['Kareem'] = '938-489-1234'
# del phonebook_dict['Alice']
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)

#Exercise 2

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])

#Letter Summary

def letter_histogram():
    word_dictionary = {}
    word = input("Please enter a word: ")
    for index in range(0, len(word)):
        if word[index] in word_dictionary.keys():
            word_dictionary[word[index]] += 1
        else:
            word_dictionary[word[index]] = 1
    return word_dictionary

# print(letter_histogram())

#Word Summary

def word_histogram():
    sentence_dictionary = {}
    sentence = input("Please enter a sentence: ")
    sentence_array = sentence.split()
    for index in range(0, len(sentence_array)):
        if sentence_array[index] in sentence_dictionary.keys():
            sentence_dictionary[sentence_array[index]] += 1
        else:
            sentence_dictionary[sentence_array[index]] = 1
    return sentence_dictionary

# print(word_histogram())

#Bonus Challenge

def top3():
    dictionary_to_search = word_histogram()
    words = []
    numbers = []
    big_num1 = 0
    big_num2 = 0
    big_num3 = 0
    big_word1 = ""
    big_word2 = ""
    big_word3 = ""
    for key, value in dictionary_to_search.items():
        words.append(key)
        numbers.append(value)
    for index in range(len(numbers)):
        if big_num1 < numbers[index]:
            big_num1 = numbers[index]
            big_word1 = words[index]
        elif big_num2 < numbers[index]:
            big_num2 = numbers[index]
            big_word2 = words[index]
        elif big_num3 < numbers[index]:
            big_num3 = numbers[index]
            big_word3 = words[index]

    print(f"The top three words are:\n{big_word1}: {big_num1}\n{big_word2}: {big_num2}\n{big_word3}: {big_num3} ")

top3()