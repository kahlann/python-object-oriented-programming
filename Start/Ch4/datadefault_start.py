# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

# Function to randomly generate the default price of a book
def price_func():
    # Return random value between 20 and 40
    return float(random.randrange(20, 40))

# dataclass decorator
@dataclass
class Book:
    # you can define default values when attributes are declared
    # Allows you to instantiate a Book object with no input arguments
    # Attributes without default values must come first in the list of attributes
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    # Use field to make the default more flexible
    # In this case, the 'default' value is taken from the function price_func
    price: float = field(default_factory=price_func)

# Instantiate Book object with no inputs
b1 = Book()
print(b1)

# Instantiate book objects
# Use input to set values for all attributes except price
b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)

print(b1)
print(b2)