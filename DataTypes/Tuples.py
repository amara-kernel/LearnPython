"""
A tuple in Python is similar to a list. The difference between the two is that we cannot change
the elements of a tuple once it is assigned whereas we can change the elements of a list.
"""

# Creating a tuple
"""
A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. 
The parentheses are optional, however, it is a good practice to use them.

A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).
"""

# Empty tuple

etple = ()
print(etple)

mytple = (1, 2, 3, 4)  # Integer tuple
print(mytple)

mytple = (1, 2.3, "Hyderabad")  # Mixed tuple
print(mytple)

mytple = (1, 'man pages', 2.3, [6, 7, 8], (1, 2, 3))  # Nested tuple
print(mytple)

mytple = "john", "tracy", 100  # Parentheses are optional
print(type(mytple))

# Create a Python Tuple With one Element
"""
In Python, creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough.

We will need a trailing comma to indicate that it is a tuple,
"""

v1 = ("Hello")  # String
v2 = ("Hello",)  # Tuple

print(type(v1), " --- ", type(v2))

# Access Python Tuple Elements
# Tuple elements are accessed like a list using index.

letters = ('l', 'e', 't', 't', 'e', 'r', 's')
print(letters[0])
print(letters[5])

letters = ('l', 'e', 't', 't', 'e', 'r', 's', ('h', 'e', 'l', 'l', 'o'))
print(letters[7][1])  # Access data elements using nested indexing
print(letters[-2])  # Access tuple elements using negative indexing
print(letters[:3])  # Slicing similar to lists slicing. Prints index 0 to 2.
print(letters[-4:-1])
print(letters[:])

# Tuple methods
# We can't add or modify tuples. So, only two methods available in tuples
print(letters.count('t'))
print(letters.index("t"))

# Iterating through tuples
languages = ('C', "C++", "Java")
for language in languages:
    print(language)

# Check if an item exists in python tuple
# print("C" in languages)
if "C" in languages:
    print("C language is available in languages")

"""
We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
"""


