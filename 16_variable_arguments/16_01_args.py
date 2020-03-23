'''
Write a script with a function that demonstrates the use of *args.

'''

def sum_(*args):
    result = sum(args)
    print(result)

sum_(10, 10, 20)

