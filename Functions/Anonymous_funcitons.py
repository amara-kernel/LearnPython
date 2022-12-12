# a lambda function is a special type of function without the function name.

greet = lambda : print("Hello")
greet()

greet_user = lambda name : print("Hello", name, "!")
greet_user("Amara")

# How to use lambda function with filter?
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 12, 18, 23, 24]
new_list = list(filter(lambda x: x%3 == 0, mylist))
print(new_list)

mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list1 = list(filter(lambda x: x%2 == 0, mylist1))
print(new_list1)

new_list2 = list(map(lambda x : x * 2, mylist1))
print(new_list2)