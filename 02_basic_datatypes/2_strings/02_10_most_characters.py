'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

s1 = input("Please enter a sentence: ")
s2 = input("Please enter another sentence: ")
s3 = input ("Please enter another sentence: ")

len_s1 = len(s1)
len_s2 = len(s2)
len_s3 = len(s3)

if (len_s1 > len_s2 > len_s3):
    print(s1)
elif (len_s2 > len_s1 > len_s3):
    print(s2)
else:
    print(s3)




