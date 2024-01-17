# Python Object Oriented Programming by Joe Marini course example

# Using data classes to represent data objects
from dataclasses import dataclass

# Add dataclass decorator to the Book class
# rewrites the attributes in the Class so they are instance variables rather than class variables
@dataclass
class Book:
    # Remove __init__, list attributes and annotate with the data type for each attribute
    title: str      # Title should be a str
    author: str     # Author should be a str
    pages: int      # No. pages should be an integer
    price: float    # Price should be a float

    # Function to return book info
    def bookinfo(self):
        return f"{self.title} by {self.author} is {self.pages} pages long and costs ${self.price}."

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__ automatically!
print(b1)

# TODO: comparing two dataclasses - they implement __eq__ automatically!
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
print(b1 == b3)    # Should return True
print(b1 == b2)    # Should return False

# TODO: change some fields
b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())