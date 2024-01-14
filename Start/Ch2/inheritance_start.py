# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance
# Base class for all publications (includes price and title attributes)
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

# Base class for periodicals (inherits title and price from Publication, adds period and publisher)
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        # call super class initialiser to get title and price
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


# Book class inherits from the Publication class
class Book(Publication):
    def __init__(self, title, author, pages, price):
        # initialiser from the parent (super) class
        super().__init__(title, price)
        self.author = author
        self.pages = pages

# Magazine class of inherits from the Periodical class (which inherits from the Publication class)
class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

# Newspaper class of inherits from the Periodical class (which inherits from the Publication class)
class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
