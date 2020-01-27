'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''


str = input("Please enter a sentence: ")
l = str.split()

dict = dict((x,l.count(x)) for x in set(l))
print(dict)

max = max(dict, key=dict.get)
print(max, dict[max])





