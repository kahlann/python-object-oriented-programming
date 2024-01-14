# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        # Add names 
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        # Add names 
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()

    # Add method to show the properties inherited
    def showProps(self):
        print(self.prop1)
        print(self.prop2)
        # Print name - inherits this attribute from both A and B, but will only show the one listed first in the inheritance!
        print(self.name)

c = C()
# Show resolution (inheritance) order
print(C.__mro__)
c.showProps()
