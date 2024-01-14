# Python Object Oriented Programming by Joe Marini course example
# Checking class types and instances

# Define the Book class
class Book:
    def __init__(self, title):
        self.title = title

# Define the Newspaper class
class Newspaper:
    def __init__(self, name):
        self.name = name

# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type
# Get type for a book and a newspaper
print("{} is a {}".format(b1.title, type(b1)))
print("{} is a {}".format(n1.name, type(n1)))

# TODO: compare two types together
# Are the types of b1 and b2 the same?
print("Are b1 and b2 the same type? " + str(type(b1) == type(b2)))
print("Are b1 and n2 the same type? " + str(type(b1) == type(n2)))

# TODO: use isinstance to compare a specific instance to a known type
# Cleaner than parsing the type function 
# Is b1 an instance of the Book class?
print("Is b1 an instance of the Book class? "+ str(isinstance(b1, Book)))
# Is b1 an instance of the Newspaper class?
print("Is b1 an instance of the Newspaper class? " + str(isinstance(b1, Newspaper)))

# Note that isinstance works with inheritance: Book and Newspaper classes inherit from the object class!
print("Is b1 an instance of the object class? {}".format(isinstance(b1, object)))
