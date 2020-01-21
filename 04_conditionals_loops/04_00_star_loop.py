'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5

for i in range(0,n):
    for j in range(i+1):
        print("*", end=" ")
    print("\r")
