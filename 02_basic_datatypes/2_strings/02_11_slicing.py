'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

name = input("Please enter your name: ")

first_letter = name[:1]
other_letter = name[1:]
pig_latin = "ay"

name1 = other_letter + first_letter + pig_latin
print(name1)