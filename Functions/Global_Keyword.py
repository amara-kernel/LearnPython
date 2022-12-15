
c = 1


def add():
    print("c = ", c)


add()


def mod():
    #    c = c + 2 # This will throw error "UnboundLocalError: local variable 'c' referenced before assignment"
    """
    This is because we can only access the global variable but cannot modify it from inside the function.

    The solution for this is to use the global keyword.
    """
    print("c2 = ", c)


mod()


def mod1():
    global c
    c += 3
    print("c3 = ", c)


mod1()

# Global in nested functions:


def outer_function():
    num = 20

    def inner_function():
        global num
        num = 30

    print("Before calling inner function : ", num)
    inner_function()
    print("After calling inner function : ", num)


outer_function()
print("Outside both function: ", num)


"""Inside outer_function(), num has no effect of the global keyword.

Before and after calling inner_function(), num takes the value of the local variable i.e num = 20.

Outside of the outer_function() function, num will take the value defined in the inner_function() function i.e x = 25.

This is because we have used the global keyword in num to create a global variable inside the inner_function() 
function (local scope).

So, if we make any changes inside the inner_function() function, the changes appear outside the local scope, 
i.e. outer_function().
"""

"""
Rules of global Keyword
The basic rules for global keyword in Python are:

When we create a variable inside a function, it is local by default.
When we define a variable outside of a function, it is global by default. You don't have to use the global keyword.
We use the global keyword to read and write a global variable inside a function.
Use of the global keyword outside a function has no effect.
"""