
# When we declare variables inside a function, these variables will have a local scope (within the function).
# We cannot access them outside the function.

def greet():
    message = "This is local variable"
    print("Local ", message)

greet()
# print(message) #This will give error.

# Global variable
message = "Hello"
def greet1():
    print("Local ", message)


print("Global ", message)

# Non-local variable
# In Python, nonlocal variables are used in nested functions whose local scope is not defined. This means that the
# variable can be neither in the local nor the global scope.
# We use the nonlocal keyword to create nonlocal variables.


def outer():
    message = "local"

    def inner():
        nonlocal message
        print("inner1 ", message)
        message = 'nonlocal'
        print("inner2 ", message)
    inner()
    print("Outer1 ", message)


outer()

# Need more examples for non local variables


