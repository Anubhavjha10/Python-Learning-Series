#@property = Decorator used to define a method as a property (it can be accessed like an attribute)
#            Benifit: Add additional logic when read, write or delete attributes
#            Gives you getter, setter and deleter method

class rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f}cm"

    def height(self):
        return f"{self._height:.2f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width cannot be negative")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height cannot be negative")

rectangle1 = rectangle(100, 110)



print(rectangle1.width)
print(rectangle1.height)