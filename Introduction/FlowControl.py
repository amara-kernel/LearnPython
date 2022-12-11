# # print(list(range(1, 10)))
# genre = ['pop', 'rock', 'jazz']
#
# for i in range(0, len(genre)):
#     print(genre[i])
# else:
#     print("I am in else")

# sname = 'John'
# names={'jay': 30, 'adam': 55, 'lers': 69}
#
# for name in names:
#     if name == sname:
#         print(names[name])
#         break
# else:
#     print("Nothing matches with the list")

# def greet(him, msg="Good morning"):
#     """This function to greet people"""
#     print("Hello ", him, ". How are you?", msg)
#
#
# greet( "Good evening","Amara")
# #greet( him="Good evening","Amara") # gives error
# greet( "Good evening",msg="Amara")
# greet( him="Good evening",msg="Amara")
# greet( msg="Amara",him="Good evening")
#
#
# def greets(*names):
#     print(type(names))
#     print("Hello", names)
#
# greets("John","Jim","Foo")

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
#
# print(factorial(5))

# double = lambda x: x*x
# print(double(3))
# for i in range(5):
#     print(i)

# def unclear(x):
#     if x % 2 == 1:
#         return 1
# print(unclear(1) , unclear(2))

# for i in range(10):
#     pass
# # print(i)

i=5
while i>0:
    i = i//2
    if i%2 ==0:
        break
else:
    i+=1
print(i)