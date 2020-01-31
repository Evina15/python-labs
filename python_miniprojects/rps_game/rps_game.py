# take in a number 0-2 from the user that represents their hand
user_number = int(input("Please enter a number 0-2: "))

# generate a random number 0-2 to use for the computer's hand
import random

comp_number = random.randint(0, 2)

# call the function `get_hand` to get the string representation of the user's hand
# call the function `get_hand` to get the string representation of the computer's hand
# print out the player hand and computer hand


def get_hand(number):
    if number == 0:
        return "scissor"
    elif number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    else:
        return "Wrong number, please enter number 0-2: "

print(get_hand(user_number))
print(get_hand(comp_number))

# call the function `determine_winner` to figure out who won
def determine_winner():
    if user_number > comp_number:
        return "win"
    elif user_number < comp_number:
        return "lose"
    else:
        return "draw"

print(determine_winner())


# print out the winner