'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

current_list = [23, 3333, 1000, 4567, 621, 899, 9999]

gen = (x for x in current_list if x//1111 == 0)
#for i in gen:
    #print(i)