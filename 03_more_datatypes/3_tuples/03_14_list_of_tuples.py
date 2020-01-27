'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

#str = input("Please enter a sentence: ")
str = "hello world"
splitted = str.split()
print(splitted)
arr = [tuple(list(splitted[0])), tuple(list(splitted[1]))]
print(arr)

#use split and loop and maybe using [0] index to iterate over the splitted

