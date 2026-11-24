# Polymorphism = Means to "have many forms or faces"
from abc import ABC, abstractmethod
class Shape:

    @abstractmethod
    def area(self):
        pass

    

class Circle(Shape): # It's a circle AND a shape which means it has two form or faces
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Pizza(Circle):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius

shapes = [Circle(4), Square(3), Pizza(30)] # Pizza is a Circle and also a Shape

for shape in shapes:
    print(shape.area())

