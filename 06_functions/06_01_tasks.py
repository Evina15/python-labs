'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def divide_1(x):
    return True if x % 4 == 0 or x % 7 == 0 else False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def divide_2(x):
    return True if x % 4 == 0 and x % 7 == 0 else False

# take in a number from the user between 1 and 1,000,000,000
x = int(input("Please enter a number between 1 and 1,000,000,000: "))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
y = divide_1(x)
z = divide_2(x)

# print your new variables to display the results
print(y)
print(z)