'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def my_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f"This {k} belongs to {v}")

my_kwargs(carrot="rabbit", grass="cow", pizza="human")

