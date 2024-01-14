# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

# Import abstract class and method functionality
from abc import ABC, abstractmethod

# Abstract base class for creating shapes
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    # Abstract method for calculating area - must be overwritten by child classes
    @abstractmethod
    def calcArea(self):
        pass

# Interface - not explicitly defined in python!
class JSONify(ABC):
    # Define an abstract method - must be overwritten when implemented in classes
    @abstractmethod
    def toJSON(self):
        pass


# Class: Circle
# Inerits from GraphicShape, implements JSONify
class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    # Overwrite the calcArea method
    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    # Overwrite the toJSON method
    def toJSON(self):
        return f"{{ \"Circle\": {str(self.calcArea())} }}"

c = Circle(10)
print(c.calcArea())
print(c.toJSON())