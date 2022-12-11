#This is comments

'''
This is
multi
line
comment
'''

"""
This is
multi
line
comment
"""
"""
## Python Identifiers
Identifiers are the names given to a variable, classes and methods.

"""
"""
## Python data types:
DataType - Classes
Numeric - int, float, complex
String - Str
Sequence - List, tuple, range
Mapping - Dict
Boolean - bool
Set - set, frozenset 

"""


a, b, c = 1, 1.2, 4+5j
print(a, " is of type ", type(a), "; ", b, " is of type ", type(b), c, " is of type ", type(c))
a, b = [1, 2.3, "Bangalore"], ("Hyd", 2, 3)
"""List is an ordered collection of similar or different types of items separated by commas 
and enclosed within brackets [ ]"""
"""
Tuple is an ordered sequence of items same as list, The only difference is that tuples are 
immutable. Tuples once created, cannot be modified.
"""
print(a, " is of type ", type(a), "; ", b, " is of type ", type(b))
print("Access list with index : a[0] - ", a[0])
print("Access tuple with index : b[1] - ", b[1])
name = "Python"
message = "Learn python strongly"
print(name, " is of ", type(name))

"""Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }."""
set_of_ids = {1, 2, 3, 4, None}
print("Set of type ", type(set))
"""Since sets are un ordered values, indexing has no meaning. Hence slicing operator [] does not work")"""

"""
Python dictionary is an unordered collection of items. It stores elements in key and value pairs.
Keys are unique identifiers that are associated with each value.
"""
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
# When we print dicitonary, we might get values in different order. This is because dictionary has no
# particular order. Dictionaries are accessed using keys.

print(capital_city["England"])

# variables
# var=20
# a, b, c = 10, 12.3, 'Costa'
# print(a)
# print(b)
# print(c)
# Pyton is case sensitive language


# Literals are representation of fixed values in a program. They can be numbers, characters or strings.
# Example: 45, 12.34, "A", "Hello"
# Boolean literal
pass1 = True
# Numberical literals are Integers, Floats and Complex values.
# Character and string literals examples are : "S", "Singapore"
# None is a special literal which is used to specify a null variable.
""" Literal collections::
There are 4 literal collections: List, Set, Dict and Tuple
"""
# # List literal
# fruits = ["Apple", "Orange"]
# print(fruits)
# # Tuple literal
# fruits = ("Apple", "Orange")
# print(fruits)
# # Dictionary literal
# fruits = {"a":"Apple", "b":"Orange"}
# print(fruits)
# # Set literal
# fruits = {"Apple", "Orange"}
# print(fruits)





# def prt(text):
#     print(text)
#
# x= prt("Hello")
# print(x)

## Print python keywords
# import keyword
# print(keyword.kwlist)

# import asyncio
#
#

# async def main():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("World")
# asyncio.run(main())
#
#
# a, b, c = 1, 20, 300
# print("a=", a, ' b=', b, ' c=', c)


# names = ['1','2','3','4','5']
# for name in names:
#     print('Hello ' + name)
#

# glbvar=10
# def read1():
#     print(glbvar)
# def read2():
#     global glbvar
#     glbvar = glbvar+5
# def read3():
#     glbvar=20
#
# read1()
# read2()
# read1()
# read3()
# read1()

# list1 = ['1','2','3','4']
# print('2' in list1)
# print(6 in list1)

# Run below in terminal
# True is True
# False is False
# None is None
# [] == []
# {} == {}
# [] is []
# {} is {}
# "" == ""
# '' is ''
# () == ()
# () is ()

# def full_outer():
#     a = 2
#     def outer_function():
#         a = 5
#         def inner_function():
#             nonlocal a
#             print("Before a =",a)
#             a = 10
#             print("Inner a = ",a)
#         inner_function()
#         print("Outer a = ",a)
#     print(a)
#     outer_function()
#
# full_outer()


# def some_function():
#     pass
#
# some_function()

# a=1+2+\
#     3+4+\
#     5
# print(a)
#
# b= (1+2+
#     3+ 4+
#     5)
# print(b)
# c=['a', 'b', 'c']
# print(c)

# def double(n):
#     """This doubles the value"""
#     return 2*n
#
#
# print(double.__doc__)
# a, b, c = 1, 2, "apple.com"
# print(a, " ~~ ", b, " ~~ ", c)
#
# import constant
# print(constant.PI)
#
# drink = "Available"
# food = None
# def menu(name):
#     if name == drink:
#         print(name)
#     else:
#         print(food)
#
#
# menu(drink)
# menu(food)

#
# country={"IND": "INDIA",
#          "USA": "UNITES STATES",
#          "UAE": "DUBAI"}
# print(country['IND'])

# STRINGS
# TUPLES
# DICTIONARIES
# LIST
# SET

# list_fruits=['a', 'b', 'c']
# tuplefruits=('a', 'b', 'c')
# dictaphabets={'a': 'A', 'b': 'B'}
# setvowels={'a', 'e', 'i', 'o', 'u'}


# a = 5
# print(a, 'is of type ', type(a))
# a = 2.0
# print(a, 'is of type ', type(a))
# b = 2+4j
# print(b, 'is of complex type?', isinstance(b, complex))
# print(a, 'is of float type?', isinstance(a, float))
#

# list1 = ['a', 1, 1.2]
# print(list1[1:])
#
# tp1=(1,2,3,4,5,'a',1.23)
# print(tp1)
# print(tp1[2:5])
# print(tp1[:5])

# set1={1,'a',1.2}
# print(set1)


# nint = 123
# nflt=1.23
# newnum=nint + nflt
# print("data type of num int ", type(nint))
# print("data type of num float ", type(nflt))
# print("Value of new num ", newnum)
# print("data type of new num ", type(newnum))


# num_int=123
# num_str= "hello"
# print(num_int + num_str)

# print(type(int("123")))
# a=5; b=6
# print("Value of a i {} and b is {}".format(a,b))
# print("Value of a i",a,"and b is",b)

# inp = input("Enter text")
# print(eval(inp))
#

# import math
# print(math.pi)

# from math import pi

# import sys
# print(sys.path)

# print(5 != 6)
# x={1,3}
# x.add(3)
# x.add(4)
# print(x)

import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = a*b
# d = np.dot(a,b)
# print(c)
# print(d)
#
# for x in range(1,5):
#     print(2*x)

# print({x: x*x for x in range(1, 10)})
# print([1,2,3] * 3)

# def outerfunc():
#     global a
#     a= 20
#     def inner():
#         global a
#         a=30
#         print('a3 :', a)
#     inner()
#     print('a2 : ',a)
#
#
# a = 10
# outerfunc()
# print('a1 : ', a)
#


