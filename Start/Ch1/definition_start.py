# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
# The parentheses are unnecessary unless inheriting from another class
class Book():
  # Initialiser (not constructor) - takes book title as argument
  def __init__(self, title):
    self.title = title

# TODO: create instances of the class
book1 = Book("Fundamentals of Physical Chemistry")
book2 = Book("The Book Thief")
book3 = Book("")

# TODO: print the class and property
# Print the object (first book)
print(book1)
# Print the title (first book)
print(book1.title)