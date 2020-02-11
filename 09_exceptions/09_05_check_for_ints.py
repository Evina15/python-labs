'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''



while True:
    try:
        number = int(input("Please enter a number: "))
    except ValueError:
        print("Please enter a valid integer")
    else:
        print("Thank you for entering a number!")
        break

# ALTERNATIVES

#while True:
    #user_input = input("Please enter a number: ")
    #if user_input.isdigit():
        #print("Thank you for entering the number!")
        #break
    #else:
        #print("You are not entering the valid number.")

