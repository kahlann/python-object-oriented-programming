# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: define a class to represent a stock symbol

# Challenge: create a class to represent stock information.
# Your class should have properties for:
# Ticker (string)
# Price (float)
# Company (string)
# And a method get_description() which returns a string in the form
# of "Ticker: Company -- $Price"

class Stock:
    # Initialiser
    def __init__(self, ticker, price, company):
    
        # Check the input types
        # Ticker
        if isinstance(ticker, str):
            self.ticker = ticker
        else: 
            raise ValueError("Ticker input must be a string.")
    
        # Price
        if isinstance(price, float):
            self.price = price
        else: 
            raise ValueError("Price input must be a float.")
    
        # Company name
        if isinstance(company, str):
            self.company = company
        else: 
            raise ValueError("Ticker input must be a string")

    # define method to return a string with a description of each stock 
    def get_description(self):
        return F"{self.ticker}: {self.company} -- ${self.price}"

    
# ~~~~~~~~~ TEST CODE ~~~~~~~~~
msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())
