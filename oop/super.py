# super() = function used in a child class to call methods from a parent class (superclass)
# Allows you to extend the functionallity of the inherited methods.

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print("Something")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):  # The child's method would be used instead of parent's method
        print("Something overwrite")
    # How to avoid?
        super().describe() # this will extend the method

   

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height