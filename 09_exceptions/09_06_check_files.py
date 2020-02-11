'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'

try:
    with open("integers.txt", "r") as intgr:
        str1 = intgr.read()
        first_number = int(str1[0])

    import random
    num1 = random.randint(-10, 10)
    num2 = random.randint(-1, 3)

    calculation = first_number + num1 / num2

except IOError as ioe:
    print(ioe)

except ValueError as ve:
    print(ve)

except ZeroDivisionError as zde:
    print(zde)

else:
    print(f"The result of {first_number} + {num1} /{num2} = {calculation}")


