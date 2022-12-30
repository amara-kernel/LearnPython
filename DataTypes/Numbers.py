
"""
Python supports integers, floating-point numbers and complex numbers. They are defined as int, float,
and complex classes in Python.

int - holds signed integers of non-limited length.
float - holds floating decimal points and it's accurate up to 15 decimal places.
complex - holds complex numbers.
We can use the type() function to know which class a variable or a value belongs to.
"""

print("2 is of type ", type(2))
print("2.53 is of type ", type(2.53))
print("2+5j is of type ", type(2+5j))

"""
In python we can represent the binary (base2), hexadecimal (base16) and octa (base8) numbers by placing a prefix 
before that numbers
Binary - 0b or 0B
Octal - 0o or 0O
Hexa - 0b or 0B
"""
print("101011 is ", 0b101011)
print("FB is ", 0xFB)
print("27 is ", 0o27)
print("Sum : ", 0B101011 + 0XFB + 0O27)

# Type conversion
print(1 + 1.2) # 1 will be converted to float.

# Explicit type conversion
print(int(3.2))
print(int(-3.2))
print(float(9))
print(complex('2+4j'))

# Python random moduel
"""
Python offers the random module to generate random numbers or to pick a random item from an iterator.
"""

import random as rd
print(rd.randrange(10, 100))  # Picks a random number from 10 to 100
list1 = [1, 2, 3, 4, 5, 6]
print(rd.choice(list1)) # get random item from list1
print(list1)
rd.shuffle(list1)
print(list1)
print(rd.random())

# math module offers lot of
