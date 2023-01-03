"""
When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed
so that the resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order:

Open a file
Read or write (perform operation)
Close the file
"""

# Opening files in python
# Use open() method to open a file

file1 = open("test_input.txt")
file2 = open("test_input.txt")
print(type(file1))
print(file2)
# We have created file1 as file object.
# By default, the files are open in read mode (cannot be modified).

file2 = open("test_input.txt", "r")

"""
Mode Description
r	Open a file for reading. (default)
w	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Open a file for exclusive creation. If the file already exists, the operation fails.
a	Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Open in text mode. (default)
b	Open in binary mode.
+	Open a file for updating (reading and writing)
"""

file1 = open("test_input.txt")  # Equivalent to 'r' or 'rt'
file1 = open("test_input.txt", 'w')  # Write in text mode
file1 = open("img.bmp", 'r+b')  # read and write in binary mode

# Reading files

