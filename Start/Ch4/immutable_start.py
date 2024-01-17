# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes - data within the class cannot be changed

from dataclasses import dataclass

# TODO: Add the "frozen" parameter to the dataclass decorator
# This makes the class immutable, the values of the attributes cannot be changed
@dataclass(frozen=True)  
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    # Method that will attempt to change an attribute
    # Will be unsuccessful as the attributes are frozen!
    def change_attr(self, newval):
        self.value1 = newval

obj = ImmutableClass()
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "Changed value"      # Returns a FrozenInstanceError

# TODO: even functions within the class can't change anything
# obj.change_attr("A new string")     # Returns a FrozenInstanceError

# The attributes CAN be re-assigned at instantiation
obj = ImmutableClass("Another String", 20)
print(obj.value1, obj.value2)