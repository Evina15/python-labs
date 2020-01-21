'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

n1 = int(input("Please enter a number: "))
n2 = int(input("Please enter a number: "))
n3 = int(input("Please enter a number: "))
n4 = int(input("Please enter a number: "))
n5 = int(input("Please enter a number: "))
n6 = int(input("Please enter a number: "))
n7 = int(input("Please enter a number: "))
n8 = int(input("Please enter a number: "))
n9 = int(input("Please enter a number: "))
n10 = int(input("Please enter a number: "))
list = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

total = 0
for ele in range(0, len(list)):
    total += list[ele]
print("Sum of all elements in given list: ", total)

print("The largest number in the list is ", max(list))