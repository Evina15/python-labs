'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

# int to float
a_int = 2
b_int = 3
c_sum_float= float(a_int+b_int)
print(c_sum_float)

# float to int
a_float = 2.3
b_float = 1.2
c_sum_int = int(a_float+b_float)
print(c_sum_int)

# floor division
a = 10
b = 4
sum = a//b
print(sum)

# multiplication
a = int(input("Please enter a number from 1-10: "))
b = int(input("Please enter a number from 11-20: "))
sum = a*b
print(sum)