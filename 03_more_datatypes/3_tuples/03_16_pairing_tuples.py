'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''


#sorting numbers

#stores the number in tuples of two [(x,y),(a,b)]

#using if statement (odd numbers = 1,3,5,7...)
#adding number 0 to the lonely number [(x,y),(a,b),(c,0)]

#prints x,y AND a,b


numbers = [55, 12, 4, 90, 33, 28, 45]
numbers.sort()
print(numbers)
cur_list = []
big_list = []
for x in range(0, len(numbers)):
    cur_list.append(numbers[x])
    if len(cur_list) == 2:
        big_list.append(tuple(cur_list))
        cur_list = []
if len(cur_list) == 1:
    cur_list.append(0)
    big_list.append(tuple(cur_list))
print(big_list)
