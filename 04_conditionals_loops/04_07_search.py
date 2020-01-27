'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

n = int(input("Please enter a number between 0 and 1,000,000,000: "))

#x = -1
x = 0
#for x in range(0, 1000000000):
#while x < n:
while x in range(0, 100000000):
    if x == n:
        break
    x = x + 1
print(x)

#put break to exit