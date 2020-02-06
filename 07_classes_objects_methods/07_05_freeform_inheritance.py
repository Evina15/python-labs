'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Movie:
    def __init__(self, year, title):
        self.year = year
        self.title = title

    def __str__(self):
        return f"In {self.year}, the most popular movie is {self.title}."

    def played(self, amount_played):
        print(f"This {self.title} movie has been played for " + str(amount_played) + " times in the cinema.")


class RomCom(Movie):
    def __init__(self, year, title, rating=1):
        super().__init__(year, title)
        self.rating = rating

    def __str__(self):
        return f"In {self.year}, this movie {self.title} just won an award in Romantic Comedy with {self.rating} rating. "

class ActionMovie(Movie):
    def __init__(self, year, title, pg=13):
        super().__init__(year, title)
        self.pg = pg

    def __str__(self):
        return f"If you see a movie with pg {self.pg}, that means it needs parental guidance." \
               f"{self.title} that come out in {self.year} is one of them."



class Restaurant:
    def __init__(self, name, food_type):
        self.name = name
        self.food_type = food_type

    def __str__(self):
        return f"I love eating in {self.name} that serves {self.food_type}."

class Gourmet(Restaurant):
    def __init__(self, name, food_type, location):
        super().__init__(name, food_type)
        self.location = location

    def __str__(self):
        return f"Since I like {self.food_type} type food and {self.location} is very close to my house, {self.name} is my favourite!"

class FastFood(Restaurant):
    def __init__(self, name, food_type, rating=1):
        super().__init__(name, food_type)
        self.rating = rating

    def __str__(self):
        return f"I think the {self.food_type} food in {self.name} has {self.rating} rating."

    def junk_food(self):
        if self.name == "KFC":
            print(f"Don't keep eating in {self.name}! It will kill you!")
        else:
            print(f"Oh I heard the food in {self.name} is really good for your health!")


class Education:
    def __init__(self, type, major):
        self.type = type
        self.major = major

    def __str__(self):
        return f"You should go to {self.type} if you want to study {self.major}."

class College(Education):
    def __init__(self, type, major, duration=1):
        super().__init__(type, major)
        self.duration = duration

    def __str__(self):
        return f"If you want to take {self.major} in {self.type} type of education, you have to study for {self.duration} years."

    def extra_study(self):
        self.duration += 2
        print(f"Uh oh you failed your last test. So you will have to study for another {self.duration} years")

class HighSchool(Education):
    def __init__(self, type, major, name, students, duration=1):
        super().__init__(type, major)
        self.name = name
        self.students = students
        self.duration = duration

    def __str__(self):
        return f"My daughter is in {self.type} now taking {self.major} subject." \
               f"{self.name} is the best school in our city with {self.students} students." \
               f"She will stay in that school for {self.duration} years."

    def unpopular(self):
        if self.students <= 10:
            print(f"This {self.name} school has no student left!")
        else:
            self.students -= 10
            print(f"{self.name} were once a very popular school. Now they only have {self.students} of students.")

class JuniorHighSchool(HighSchool):
    pass


marvel = Movie(2001, "Iron Man")
print(marvel)
marvel.played(30)
fastfurious = ActionMovie(2014, "The Fast and Furious")
print(fastfurious)

kfc = FastFood("KFC", "western", 2)
print(kfc)
kfc.junk_food()

tafe = College("vocational", "hairdressing", 3)
print(tafe)
tafe.extra_study()

bali_school = HighSchool("senior high school", "math", "Bali School", 5, 3)
print(bali_school)
bali_school.unpopular()


