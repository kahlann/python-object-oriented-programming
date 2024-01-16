# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, value):
        # If the second object is not a Book object, raise an error
        if not isinstance(value, Book):
            raise ValueError("Can't compare a Book to a non-Book")
        return (self.title == value.title and
                self.author == value.author and
                self.price ==value.price)


    # TODO: the __ge__ establishes >= relationship with another obj
    # In this case, compare the prices to determine whether something is greater than or equal to
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare a Book to a non-Book")
        return self.price >= value.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare a Book to a non-Book")
        return self.price < value.price

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality - should be equal as these are objects instantiated with the same attributes
# Python does not do attribute by attribute comparions, just compares whether 2 objects are the same in memory
# Overwrite the __eq__ function to fix this
# print(b1 == b3)     # Should be True
# print(b1 == b2)     # Should be False
# print(b1 == 42)     # Should raise a ValueError

# TODO: Check for greater and lesser value
print(b2 >= b1)     # Should be False
print(b2 < b1)      # Should be True

# TODO: Now we can sort them too
# Mixed list of the book objects
books = [b1, b3, b2, b4]
# Sort - the built in sort method uses the lt operator, which we've overwritten
books.sort()
# Print out the book titles for the books in the list
print([book.title for book in books])