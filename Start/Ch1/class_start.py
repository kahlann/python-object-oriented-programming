# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods

class Book:
    # TODO: Properties defined at the class level are shared by all instances
    # Set a tuple of booktypes to choose from
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    # Initial list of books is empty
    __booklist = None

    # TODO: create a class method
    # Class methods work on the entire class
    # Class method to get the list of book types
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    # Static methods do not modify the state of either the class or a specific object instance
    # Use static method to keep track of list of books (number of instances of the Book class?)
    def getBookList():
        # if the booklist is empty
        if Book.__booklist == None:
            # Instantiate a new empty booklist
            Book.__booklist = []
        # return the booklist
        return Book.__booklist


    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    # Metod to rename the book
    def set_title(self, newtitle):
        self.title = newtitle

    # Initialiser that takes the book title and book type
    def __init__(self, title, booktype):
        self.title = title
        # valid book type? if the given booktype is not in teh list of available booktypes
        if (not booktype in Book.BOOK_TYPES):
            # raise a value error
            raise ValueError(F"{booktype} is not a valid book type!")
        # Otherwise, set the given book type
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("Book types available: ", Book.get_book_types())

# TODO: Create some book instances
b1 = Book("Title1", "HARDCOVER")
b2 = Book("Title2", "PAPERBACK")

# TODO: Use the static method to access a singleton object
thebooks = Book.getBookList()
# Add the books to the booklist
thebooks.append(b1)
thebooks.append(b2)
# print the booklist
print(thebooks)