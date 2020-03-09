'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

cars = ["BMW", "Toyota", "Honda"]

def my_enumerate(cars):
    for index, car in enumerate(cars):
        print(f"Inside the cars list, index {index} is {car}.")

car_list = my_enumerate(cars)