
def add_numbers(a, b):
    add = a + b
    return add


print(add_numbers(4, 5))


def greet(name="Sir!!"):
    print("Hello ", name)


greet("Joshua")


def display_info(firstname, lastname):
    print("First name :", firstname, " Last Name: ", lastname)


display_info("Rao", "Ramesh")
display_info(lastname="Rajesh", firstname="Rao") # You can give the arguments in any order.


def find_sum(*numbers):
    result = 0
    print(type(numbers))
    for i in numbers:
        result += i
    print("Sum : ", result)


find_sum(1, 3, 5, 7, 9, 10)

