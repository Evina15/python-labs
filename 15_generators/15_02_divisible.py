'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

current_list = [23, 3333, 1000, 4567, 621, 899, 9999]

gen = (x for x in current_list if x%1111 == 0)
for i in gen:
    print(i)