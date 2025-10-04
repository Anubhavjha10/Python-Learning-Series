# super() = function in a child class methods from a parent class (Superclass).
#           Allow you to extend the functionality of the inherited methods
class shape:
    def __init__(self,colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

class circle(shape):
    def __init__(self,colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

class square(shape):
    def __init__(self,colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.radius = width

class triangle(shape):
    def __init__(self,colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.radius = width
        self.height = height


circle = circle("Red", True, 5)
print(circle.is_filled)