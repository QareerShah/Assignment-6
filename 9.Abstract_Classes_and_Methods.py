from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class inheriting from Shape and implementing the area method
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create a Rectangle object
rect = Rectangle(5, 3)

# Calling the area method
print(f"Area of the rectangle: {rect.area()} square units")
