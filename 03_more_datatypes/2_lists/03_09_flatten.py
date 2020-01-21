'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [list[0][0], list[0][1], list[0][2], list[0][3], list[1][0], list[1][1], list[2][0], list[2][1], list[2][2]]

print(flattened_list)