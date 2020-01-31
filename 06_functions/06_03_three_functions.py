'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

def make_order(food):
    take_order(food)
    final_order = "Deliver the " + food + " when it's hot please"
    print(final_order)
    return final_order

def take_order(food):
    cooking_order(food)
    cooking_finish = "I would like to have the " + food + " with extra toppings"
    print(cooking_finish)
    return cooking_finish

def cooking_order(food):
    print("I would like to order " + food + " please.")

make_order("pizza")