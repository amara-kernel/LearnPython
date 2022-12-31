
# A set is a collection of unique data.
# A set can have any number of items and they may be of different types (integer, float, tuple, string etc.).
# But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

# Create a set of integers
intset = {1, 100, 101}
print("Int set :", intset)
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
mixed_set = {1, 'a', 2.3, (10, "Hello", 'a', 4.5)}
print(mixed_set) # Output values order my vary each. This is because the set has no particular order.

# set1 = {[1, 2, 3]} TypeError: unhashable type: 'list'
# print(set1)

# Create an Empty Set in Python
# Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.

# To make a set without any elements, we use the set() function without any argument.
empty_set = set()

empty_dict = { }

print("Data type of empty set is :", type(empty_set))
print("Data type of empty dictionary is :", type(empty_dict))

numbers = {1, 2, 2, 2, 3}
print(numbers) # we can see there are no duplicate items in the set as a set cannot contain duplicates.

# Add and Update Set Items in Python

"""
Sets are mutable. However, since they are unordered, indexing has no meaning.

We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.
"""

# Add Items to a Set in Python
# we use the add() method
numbers = {1, 2, 3, 4}
numbers.add(5) # Add takes only one argument
print(numbers)

# Update set
# The update() method is used to update the set with items other collection types (lists, tuples, sets, etc).

numbers_list = [4, 5, 6, 7] # Update with a list elements.
numbers.update(numbers_list)
print(numbers)
numbers_list1 = [1, 5, 6, 8]
numbers.difference_update(numbers_list1)  # Removes the common values and keeps only original values.
print(numbers)
numbers_tuple = (7, 8, 'a')
numbers.update(numbers_tuple) # Update with a tuple elements
print(numbers)
numbers_set = {'b', 8, 9, 10}
numbers.update(numbers_set) # Update with other set
print(numbers)
numbers_set = {'b', 9, 10}  # This can be a set or list or tuple
numbers.intersection_update(numbers_set)  # Updated with the intersection of elements.
print(numbers)

# Removes an element from a set
# Use discard() method.
languages = {'java', 'python', 'swift'}
languages.discard("java")
print(languages)

"""
Built-in Functions with Set
Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc. are commonly used with sets to perform different tasks.

Function	Description
all()	Returns True if all elements of the set are true (or if the set is empty).
any()	Returns True if any element of the set is true. If the set is empty, returns False.
enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
len()	Returns the length (the number of items) in the set.
max()	Returns the largest item in the set.
min()	Returns the smallest item in the set.
sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
sum()	Returns the sum of all elements in the set.
"""

# Iterate Over a Set

fruits = {'apple', 'orange', 'fuji'}
for fruit in fruits:
    print(fruit)

print(f'Length of the fruits set is ',len(fruits))

# Set operations
a = {1, 2, 3}
b = {2, 4, 5}
print(f'Union of set a and b is : ', a | b)
print(f'Union of set a and b is : ', a.union(b))

print("Intersection of set a and b is :", a & b)
print("Intersection of set a and b is :", a.intersection(b))

print("Difference between set a and b is :", a - b)
print("Difference between set a and b is :", a.difference(b))

print("All elements of A and B without the common elements :", a ^ b)
print("All elements of A and B without the common elements :", a.symmetric_difference(b))

# Check two sets are equal
c = {1, 2, 3}
if a == c:
    print("Set a and c are equal.")
elif a == b:
    print("Set a and c are not equal")
    print("Set a and b are equal")
else:
    print("a and b are not equal")

"""
Other Python Set Methods
There are many set methods, some of which we have already used above. Here is a list of all the methods that are available with the set objects:

Method	Description
add()	Adds an element to the set
clear()	Removes all elements from the set
copy()	Returns a copy of the set
difference()	Returns the difference of two or more sets as a new set
difference_update()	Removes all elements of another set from this set
discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	Returns the intersection of two sets as a new set
intersection_update()	Updates the set with the intersection of itself and another
isdisjoint()	Returns True if two sets have a null intersection
issubset()	Returns True if another set contains this set
issuperset()	Returns True if this set contains another set
pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()	Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
union()	Returns the union of sets in a new set
update()	Updates the set with the union of itself and others
"""





