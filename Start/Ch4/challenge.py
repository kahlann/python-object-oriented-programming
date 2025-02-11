# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: implement a dataclass

# Challenge: convert your classes to dataclasses
# The subclasses are required to override the magic method
# that makes them sortable

# Import dataclass functionality
from dataclasses import dataclass
# Import abstract method
from abc import ABC, abstractmethod

# Make abstract class that the Stocks and Bonds classes can inherit from
@dataclass
class Asset(ABC):
    price: float

    # Abstract method - must be overwritten by the child classes
    @abstractmethod
    def __lt__(self, value):
        pass

# Class for Stocks
@dataclass
class Stock(Asset):
    ticker: str
    company: str

    # Overwrite the __lt__ method to enable sorting 
    def __lt__(self, other):
        if not isinstance(other, Stock):
            raise ValueError("Can't compare a Stocks to non-Stocks")
        return self.price < other.price

# Class for Bonds
@dataclass
class Bond(Asset):
    description: str
    length: int
    yieldamt: float

    # Overwrite the __lt__ method to enable sorting 
    def __lt__(self, other):
        if not isinstance(other, Bond):
            raise ValueError("Can't compare a Bonds to non-Bonds")
        return self.price < other.price

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
    
# Rearranged the input data - inherited attributes come first!
stocks = [
    Stock(342.0, "MSFT", "Microsoft Corp"),
    Stock(135.0, "GOOG", "Google Inc"),
    Stock(275.0, "META", "Meta Platforms Inc"),
    Stock(120.0, "AMZN", "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

try:
   ast = Asset(100.0)
except:
   print("Can't instantiate Asset!")

stocks.sort()
bonds.sort()

for stock in stocks:
   print(stock)
print("-----------")
for bond in bonds:
   print(bond)