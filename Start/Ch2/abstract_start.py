# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

# Import modules to implement the abstract base class functionality
from abc import ABC, abstractmethod

# Abstract class for all shape subclasses to inherit from
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    # Make the caclArea method abstract (must be overwritten by the subclasses)
    @abstractmethod
    def calcArea(self):
        pass

# Subclass: Circle
class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    # Overwrite the calcArea method
    def calcArea(self):
        return 3.14 * (self.radius)**2

# Subclass: Square
class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    # Overwrite the calcArea method 
    def calcArea(self):
        return (self.side)**2

# This line should not run - GraphicShape is an abstract class
# g = GraphicShape()

# Try the code out on circle of radius 10, square of side length 12
c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
