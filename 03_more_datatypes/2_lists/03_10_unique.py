'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list1= [10, 20, 30, 40, 20, 50, 60, 40]
my_set = set(list1)
my_list = list(my_set)
print(my_list)