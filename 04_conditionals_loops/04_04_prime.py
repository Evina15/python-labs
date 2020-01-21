'''
Print out every prime number between 1 and 100.

'''

lower = 1
upper = 100

for x in range(lower, upper):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            print(x)