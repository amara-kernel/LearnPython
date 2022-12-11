"""
Types of Python Operators
Here's a list of different types of Python operators that we will learn in this tutorial.

Arithmetic operators
Assignment Operators
Comparison Operators
Logical Operators
Bitwise Operators
Special Operators
"""

# SPECIAL OPERATORS::

# Integrity operator:
# is - True if the operands are identical (refer to the same object)
# is not - True if the operands are not identical (do not refer to the same object)

x1 = 5
y1 = 5
x2 = "Hello"
y2 = "Hello"
x3, y3 = [1, 2, 3], [1, 2, 3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3) #x3 and y3 are equal, but not identical.It is because the interpreter locates them separately in
# memory although they are equal.

# MEMBERSHIP OPERATORS::
#In Python, in and not in are the membership operators. They are used to test whether a value or variable is
# found in a sequence (string, list, tuple, set and dictionary).

message = "History"
dictionary = {'a': "one", 'b': "two"}
print("H" in message)
print("History" not in message)
print("a" not in dictionary)
