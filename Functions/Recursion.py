
def factorial(x):
    result = 1
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

# print(factorial(4))


# By default, the maximum depth of recursion is 1000. If the limit is crossed, it results in RecursionError
def recursor():
    recursor()
recursor()