'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]


online_shop = [(x,y) for x in colors for y in sizes]
print(online_shop)
