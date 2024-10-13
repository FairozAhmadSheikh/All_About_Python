# Property =Decorator used to define a method as a property (It can be accesssed like an attribute)
# Benifits =Add Additional logic when read write or delete Attributes
# Gives you getter settter and deleter methods
class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width can't be less than or equal to zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height can't be less than or equal to zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width deleted successfully")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted successfully")

# Example usage:
rectangle = Rectangle(16, 32)
print(rectangle.height)  # Output: 16.0 cm
print(rectangle.width)   # Output: 32.0 cm
rectangle.width=334
rectangle.height=664
print(rectangle.height)
print(rectangle.height)

del rectangle.height
del rectangle.width
