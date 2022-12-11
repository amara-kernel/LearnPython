import this

"""
Name (also called identifier) is simply a name given to objects. Everything in Python is an object. 
Name is a way to access the underlying object.

For example, when we do the assignment a = 2, 2 is an object stored in memory and a is the name we associate it with. 
We can get the address (in RAM) of some object through the built-in function id(). Let's look at how to use it.
"""
a = 2
print("id(2) : ", id(2))
print("id(a) : ", id(a))
# Both refer to the same object.

print("-------------------")
a = 2
print("id(a) : ", id(a))

a = a+1
print("id(a) : ", id(a))

b = 2
print("id(b) : ", id(b))

b = 3
c = 3
print("id(3) : ", id(3))
print("id(b) : ", id(b))
print("id(c) : ", id(c))

"""
This is efficient as Python does not have to create a new duplicate object. This dynamic nature of name 
binding makes Python powerful; a name could refer to any type of object.
"""

a = 3
a = 'Hello'
a = [1, 2, 3, 4]

# Functions are objects too!! So, a name can refer to them as well


def func():
    print("I am in function")


a = func
a()

"""
Refer : https://www.programiz.com/python-programming/namespace
"""
