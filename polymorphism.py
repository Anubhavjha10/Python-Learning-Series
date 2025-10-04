# polymorphism = greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck Typing" = object must have necessary attributes/methods
from abc import ABC, abstractmethod

class shape:

    @abstractmethod
    def area(self):
        return 3.14 * self.radius ** 2

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

class square(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return 3.14 * self.side ** 2


class triangle(shape):
    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return 3.14 * self.side1 * self.side2 * 0.5

shapes = [circle(4), square(5), triangle(6, 7)]

for shape in shapes:
    print(shape.area())
