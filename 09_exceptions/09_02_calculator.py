'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


try:
    a = int(input("Please enter a number: "))
    b = int(input("Please enter another number as divisor: "))
    result = a / b
    print(f"The result of {a} divided by {b} is {result}.")
except ValueError as ve:
    print("There is an error with message: ", ve)
except ZeroDivisionError as zde:
    print("There is an error with message: ", zde)
except Exception:
    print("Something went wrong.")