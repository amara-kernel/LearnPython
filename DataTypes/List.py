# Create list
# Read list
# Add to list
# Update list
# Delete from list

# A list is a collection of similar or different types of data.
student_age = [27, 28, 25, 27]  # List can have any number of items and they can be repeated.
mylist = [1, 'Hello', 3.12, 1+3j]

# Access list elements
# Using index
print(mylist[1])
# All items
for i in mylist:
    print(i)
# Negative indexing
print(mylist[-1])  # -1 is the last item in the list
print(mylist[-3])
# print(mylist[-5])  # We will get IndexError: list index out of range

# Slicing of a python list.
# We can access a slice of a list using slicing operator :
my_list = ['p','r','o','g','r','a','m','i','z']
# Items from index 2 to 4
print(my_list[2:5])  # Index 5 is not included
print(my_list[5:])  # Index 5 till end
print(my_list[:5])  # Index from 0 to 5
print(my_list[:])  # All items
print(my_list[:-3])  # Using negative index
print(my_list[-5:-3])  # Using negative index

# Add elements to python list

numbers = [21, 34, 54, 12]
print(numbers)

# The append() method adds an item at the end of the list.
numbers.append('100')
# numbers.append('101', '102', '103') # TypeError: list.append() takes exactly one argument (3 given)
print(numbers)

prime_num = [2, 3, 5]
even_num = [2, 4, 6]

prime_num.extend(even_num)
print(prime_num)

# Change List Items
# Python lists are mutable. Meaning lists are changeable.
languages = ['java', 'scala', 'C++']
languages[2] = 'C'  # Update the list
print(languages)

# Remove an Item From a List using del. Index based removal.
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
del languages[1]
print(languages)
del languages[-1]
print(languages)
del languages[0:2] # to delete multiple values
print(languages)
languages.pop(0) # to delete single index value
print(languages)


# Remove an item from a list using remove() - item based removal.
# We can also use the remove() method to delete a list item.
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
languages.remove("Java")
print(languages)


"""
Method	Description
append()	add an item to the end of the list
extend()	add items of lists and other iterables to the end of the list
insert()	inserts an item at the specified index
remove()	removes item present at the given index
pop()	returns and removes item present at the given index
clear()	removes all items from the list
index()	returns the index of the first matched item
count()	returns the count of the specified item in the list
sort()	sort the list in ascending/descending order
reverse()	reverses the item of the list
copy()	returns the shallow copy of the list
"""

l1 = ['a', 'b', 1, 2.3, "Hello"]
l2 = [10,20,30]

# index based access
print(l1[3])

# access from right
print(l1[-1])

# print all
for i in l2:
    print(i)

print(l2)

# append an item
l2.append("Hi")
print(l2)

# merge two lists
l1.extend(l2)
print(l1)

# slice list
print(l1[3:])

# add at 2nd index
l1[2] = 'Hyd'
print(l1)
l1.insert(2, 'Master')
print(l1)

# delete at 2nd index
del l1[1]
print(l1)
l1.pop(1)
print(l1)

# delete a particular item in list
l1.remove(10)
print(l1)

# revers the list
l1.reverse()
print(l1)

# sort the list
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
languages.sort()
print(languages)

# count of the list
print(" Count : ", languages.count("C"))

# clear the list
languages.clear()
print(" Cleared languages list : ", languages)

# Index of first occurrence of an element
print("Index of a in l1: ", l1.index("a"))

# length of the list
print("No of elements in list l1:", len(l1))


