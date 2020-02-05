'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rect_area(self):
        rect_area_result = self.length * self.width
        return f"The area of this rectangle with length {self.length} and width {self.width} is {rect_area_result}"

    def rect_pmt(self):
        rect_pmt_result = 2*(self.length+self.width)
        return f"The perimeter of this rectangle with length {self.length} and width {self.width} is {rect_pmt_result}"


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circ_area(self):
        circ_area_result = 3.14 * self.radius * self.radius
        return f"The area of this circle with radius {self.radius} is {circ_area_result}"

    def circ_circum(self):
        circ_circum_result =  2 * 3.14 * self.radius
        return f"The circumference of this circle with radius {self.radius} is {circ_circum_result}"


my_rectangle = Rectangle(2, 3)
print(my_rectangle.rect_area())
print(my_rectangle.rect_pmt())

my_circle = Circle(3)
print(my_circle.circ_area())
print(my_circle.circ_circum())

