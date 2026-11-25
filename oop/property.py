# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
# Benefit: add additional logic when read, write or delete attributes
# Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width # _var private attributes
        self._height = height

    # get methods
    @property
    def width(self):
        return f"Rectangle width: {self._width:1f}cm"
    
    @property
    def height(self):
        return f"Rectangle height: {self._height:1f}cm"

    # set methods
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Width must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
                
rectangle = Rectangle(10, 12)
rectangle.width = 0 # width must be greater than 0
print(rectangle.width) # Rectangle width: 0cm
print(rectangle.height)

del rectangle.width
print(rectangle.width) # AttributeError: 'Rectangle' object has no attribute '_width'. Did you mean '.width' instead of '._width'? 