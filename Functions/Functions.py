# A function is a block of code that performs a specific task.
# There are two types of functions.
# 1. Standard library functions (Built-in functions)
# 2. User defined functions.

def greet():
    print("Hello")


greet()


def add_num(num1, num2):
    addnum = num1 + num2
    print("Sum : ", addnum)


add_num(9, 10)


def add_numbers(num1, num2):
    return num1 + num2


add_num = add_numbers(17, 18)
print(add_num)

import math

sqroot = math.sqrt(49)
print(sqroot)
print(math.pow(2, 4))


# Importing a module
import example

print(example.add(4, 66))


# Rename a module
import example as ex

print(ex.add(10,22))


# Import specific function or name
from example import add

print(add(100,200))

# Import names
from example import *
print(add(250, 250))
#__myprint("Amara") - * will not import functions beginning with underscore (private functions).

from example import __myprint
__myprint("Sreenivas")

"""Here, we have imported all the definitions from the math module. This includes all names visible in our 
scope except those beginning with an underscore(private definitions).

Importing everything with the asterisk (*) symbol is not a good programming practice. 
This can lead to duplicate definitions for an identifier. It also hampers the readability of our code.
"""

# In Python, we can use the dir() built in function to list all the function names in a module.
# Default Python attributes associated with the module are with __<name>__
print("All function names in example module: ", dir(example))
print("Name of the module : ", ex.__name__)


