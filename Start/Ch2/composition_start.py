# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects

# Book class
class Book:
    # By default, no author
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        # Book object contains the author object
        self.author = author

        # Empyt list of chapters
        self.chapters = []

    # Method to add chapters to the chapter list
    # Takes a chapter object as input
    def addchapter(self, chapter):
        self.chapters.append(chapter)

    # Method to calculate the number of pages in the book
    def getBookPageCount(self):
        # Set initial counter to 0
        result = 0
        # Iterate over the chapters
        for ch in self.chapters:
            # Increment the counter by the no. pages in that chapter
            result += ch.pagecount
        # return the final page count
        return result

# Create a class for the author information
class Author:
    # Initialiser - set first and last name attributes
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    # Overwrite the built-in str function to get the object in string format
    def __str__(self):
        return f"{self.fname} {self.lname}"

# Chapter class
class Chapter:
    def __init__(self, name, pagecount):
        # Get name and length of that chapter
        self.name = name
        self.pagecount = pagecount

# Test the code
# Instantiate author object
auth = Author("Leo", "Tolstoy")

# Instantiate the book object
b1 = Book("War and Peace", 39.0, auth)

# Add chapters to the book
b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

# Print information about the book
print(f"The book is {b1.title} by {b1.author}.")
print(f"The book is {b1.getBookPageCount()} pages long.")
