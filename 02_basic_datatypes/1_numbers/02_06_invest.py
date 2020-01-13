'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

i = int(input("Please enter the amount you want to invest: " )) # investment amount
r_percent= int(input("Please enter the interest rate in percentage: ")) # interest rate in percentage
t = int(input("How many years you want to invest? ")) # number of years

r = r_percent/100

fv = i*(1+(r*t))
print(int(fv))
