'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

user_input = input("Please enter a sentence: ")
my_dict = {}

for letter in user_input:
    my_dict[letter] = my_dict.get(letter,0) + 1
print(my_dict)

