
# Display output and take input
print("Python is so powerful")

# The actual syntax of the print function accepts 5 parameters
# print(object= separator= end= file= flush=)
"""
object - value(s) to be printed
separator (optional) - allows us to separate multiple objects inside print().
end (optional) - allows us to add add specific values like new line "\n", tab "\t"
file (optional) - where the values are printed. It's default value is sys.stdout (screen)
flush (optional) - boolean specifying if the output is flushed or buffered. Default: False
"""

print("Good morning!")
print("It is very pleasant today")

print("Good morning!", end=' ')
print("It is very pleasant today")

print("one", "two", "three", end=' ')
print("one", "two", "three", sep='~')

# INPUT:

name = input("Enter name : ")
print("Name :", name)
num=int(input("Enter number : "))
print("Num : ", num, ' and it\'s type is : ', type(num))


