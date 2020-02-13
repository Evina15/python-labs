'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

# Open war_and_peace.txt, read the whole file content and store it in a variable
var_war_peace = []
with open("/Users/budhiarta/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/war_and_peace.txt", "r") as warpeace:
    for word in warpeace.readlines():
        word = word.strip()
        if word != "":
            var_war_peace.append(word)

# Open crime_and_punishment.txt and overwrite the whole content with an empty string
with open("/Users/budhiarta/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/crime_and_punishment.txt", "w") as crimepunishment:
    var_crime_punishment = crimepunishment.write("")

var_pride_prejudice = []
with open("/Users/budhiarta/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/pride_and_prejudice.txt", "r") as prideprejudice:
    for word in prideprejudice.readlines():
        word = word.strip()
        if word != "":
            var_pride_prejudice.append(word)

# Loop over all three files and print out only the first character each
wp = "/Users/budhiarta/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/war_and_peace.txt"
pp = "/Users/budhiarta/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/pride_and_prejudice.txt"
cp = "/Users/budhiarta/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/crime_and_punishment.txt"


for x in [wp, pp, cp]:
    with open(x, "r") as f:
        first_line = f.readline()

        try:
            print(first_line[0])

        except IndexError as ie:
            print("Cannot print the first character in war and peace, pride and prejudice, crime and punishment because ", ie)
        except TypeError as te:
            print("Cannot print the first character in war and peace, pride and prejudice, crime and punishment because ", te)



# custom exception

#class WordPrince(Exception):
    #def __init__(self, message):
        #super().__init__(message)

#words = []
#for x in [wp, pp, cp]:
    #with open(x, "r") as f:
        #for word in f.readlines():
            #words = word.strip()


#for p in words:
    #for prince in range(0, 101):
        #prince_words = prince.startswith("Prince")
        #print(prince_words)









# try:
