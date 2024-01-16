# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


from typing import Any


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name):
        # Automatically apply the discount when the price attribute is retrieved
        # Check that it's the price attribute being retrieved
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)


    # TODO: __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name, value):
        # enforce float to set the price
        if name == "price": 
            if type(value) is not float:
                raise ValueError("Price must be set to a float value")
            return super().__setattr__(name, value)

    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    # This function only gets called if the __getattribute__ version isn't defined.
    # If __getattribute__ undefined, this will get used or if it throws an exception,
    # or if the attribute doesn't actually exist. 
    def __getattr__(self, name):
        return name + " is not here!"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# Set the book price - if not float, should return an error
b1.price = 38.00
print(b1)

# Try and return an attribute that doesn't exist
# Will call __getattr__ as __getattribute__ couldn't find the attribute
print(b2.randomprop)