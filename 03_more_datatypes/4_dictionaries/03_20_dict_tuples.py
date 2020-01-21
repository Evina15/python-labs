'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''

input_dict = {"item1": 5, "item2": 6, "item3": 1}
sorted_d = {key: value for key, value in sorted(input_dict.items(), key=lambda item: item[1])}
return_list = list(sorted_d.items())
print(return_list)