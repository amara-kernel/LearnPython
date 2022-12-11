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

