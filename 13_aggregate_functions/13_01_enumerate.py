'''
Demonstrate the use of the .enumerate() function.
'''

#enumerate() function is to put a counter on iterable items

food_list = ["pizza", "fried rice", "burger", "noodle"]

def my_enumerate(food_list):
    for number, food in enumerate(food_list, start=100):
        print(f"{number}: {food} is so yummy")


my_enumerate(food_list)