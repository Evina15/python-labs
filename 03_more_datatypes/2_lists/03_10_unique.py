'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list1= [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

my_dict = {}
for x in list1:
    my_dict[x] = my_dict.get(x, 0) + 1
print(my_dict)

list2 = []
for key, value in my_dict.items():
    if value == 1:
        list2.append(key)
print(list2)

#for x in list2:
#    list2.append(x)
#    print(list2)