# Strings are sequence of characters. Can use single or double quotes.

string1 = 'Python programming'
string1 = "Python programming"

# Access String Characters in Python
print(string1[4])  # ne way is to treat strings as a list and use index values
print(string1[-2])  # NegativeIndexing
print(string1[:4])  # Slicing
# print(string1[24])  # Will get string index out of range error

# Python Strings are immutable
# In Python, strings are immutable. That means the characters of a string cannot be changed.
name = "John"
# name[1] = 'e'  # TypeError: 'str' object does not support item assignment
name = "Bijoy"  # However, we can assign the variable name to a new string.

# Multi line string. Can use """ or '''
message = """
Hi,
Good morning
"""
print(message)

# Python String Operations
# 1. Compare Two Strings - Use ==
str1 = "Hello world!"
str2 = "I am good"
str3 = "Hello world!"

print(str1 == str2)
print(str1 == str3)

# 2. Join Two or More Strings
print(str1 + " " + str2)

# Iterate Through a Python String
for i in str1:
    print(i)

print(len(str1))  # String length
print("z" in str1)  # Membership test
print("Hello" in str1)  # Membership test

"""
Other methods:
Methods	Description
upper()	converts the string to uppercase
lower()	converts the string to lowercase
partition()	returns a tuple
replace()	replaces substring inside
find()	returns the index of first occurrence of substring
rstrip()	removes trailing characters
split()	splits string from left
startswith()	checks if string starts with the specified string
isnumeric()	checks numeric characters
index()	returns index of substring
"""

# Escape Sequences in Python
# The escape sequence is used to escape some of the characters present inside a string.
# Suppose we need to include both double quote and single quote inside a string,
# example = "He said, "What's there?""  # This will give error
example = "He said, \"What\'s there?\""
print(example)

#  escape single quotes
example = 'He said, "What\'s there?"'
print(example)

"""
Here is a list of all the escape sequences supported by Python.

Escape Sequence	Description
\\	Backslash
\'	Single quote
\"	Double quote
\a	ASCII Bell
\b	ASCII Backspace
\f	ASCII Formfeed
\n	ASCII Linefeed
\r	ASCII Carriage Return
\t	ASCII Horizontal Tab
\v	ASCII Vertical Tab
\ooo Character with octal value ooo
\ xHH Character with hexadecimal value HH
"""

# Python String Formatting (f-Strings)
name = "Cathy"
country = "UK"
print(f'{name} is from {country}')




