'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''

class Animal:
    color = "grey"
    food = "other animal"

    def __init__(self, name, location, legs=4):
        self.name = name
        self.location = location
        self.legs = legs

    def extinct(self):
        print(f"Uh oh, too bad {self.name} already extinct.")
        self.name = self.name + "extinct"

    def __str__(self):
        return f"This beautiful animal that lives in {self.location} is {self.name} with {self.legs} legs."

class House:
    location = "in the city area"
    target = "small family"

    def __init__(self, type, bedroom, bathroom=1):
        self.type = type
        self.bedroom = bedroom
        self.bathroom = bathroom

    def sale(self):
        print(f"I'm sorry, this {self.type} property with {self.bedroom} bedroom is no longer on the market.")

    def __str__(self):
        return f"Someday I would love to buy a {self.type} with {self.bedroom} bedroom and {self.bathroom} bathroom."

    def __add__(self, other):
        total_bedroom = int(self.bedroom) + int(other.bedroom)
        total_bathroom = int(self.bathroom) + int(other.bathroom)
        return f"This property has {total_bedroom} bedroom and {total_bathroom} bathroom."

class Food:
    served_at = "restaurant"
    cooking_time = "30 minutes"

    def __init__(self, name, origin, taste="good"):
        self.name = name
        self.origin = origin
        self.taste = taste

    def specials(self):
        print(f"{self.name} is our special menu for tonight")

    def __str__(self):
        return f"This strange looking meal is called {self.name} originally come from {self.origin} and it has {self.taste} taste to it."

dinosaur = Animal("brontosaurus", "the wild")
print(dinosaur)
dinosaur.extinct()
print(dinosaur.food)

villa = House("villa", 2, 2)
print(villa)
villa.sale()
int(villa.bedroom) + 3
int(villa.bathroom) + 2

tomyum = Food("tomyom", "Thailand", "spicy")
print(tomyum)
tomyum.specials()
print(tomyum.cooking_time)

