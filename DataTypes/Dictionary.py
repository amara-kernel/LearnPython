"""
Python dictionary is an ordered collection (starting from Python 3.7) of items. It stores elements in key/value pairs.
Here, keys are unique identifiers that are associated with each value.
"""

# Create a dictionary
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)
# We can also have keys and values of different data types.
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

# Add a value to a dictionary
capital_city["India"] = "Delhi"
print(capital_city)

# Update a value
numbers[1] = "ONE"
print(numbers)

# If we try to access the value of a key that doesn't exist, we'll get an error.
del numbers[1] # Delete elements
print(numbers)
del numbers  # Deletes entire dictionary

emptydict = {}
print(all(emptydict)) # all() will return true if all keys of a dictionary are true or dictionary is empty
print(all(capital_city))

"""
Python Dictionary Methods
Methods that are available with a dictionary are tabulated below. Some of them have already been used in the above examples.

Function	Description
all()	Return True if all keys of the dictionary are True (or if the dictionary is empty).
any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len()	Return the length (the number of items) in the dictionary.
sorted()	Return a new sorted list of keys in the dictionary.
clear()	Removes all items from the dictionary.
keys()	Returns a new object of the dictionary's keys.
values()	Returns a new object of the dictionary's values
"""

# Dictionary Membership Test
# We can test if a key is in a dictionary or not using the keyword in. Notice that the membership test is only for
# the keys and not for the values

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares) # prints True

print(2 not in squares) # prints True

# membership tests for key only not value
print(49 in squares) # prints false

# Iterating Through a Dictionary
# We can iterate through each key in a dictionary using a for loop.
# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

