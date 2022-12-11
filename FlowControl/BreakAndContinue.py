
# The break statement is used to terminate the loop immediately when it is encountered.

for i in range(10):
    if i == 6:
        break
    print(i)

# The continue statement is used to skip the current iteration of the loop and the control flow of the program
# goes to the next iteration.

for i in range(8):
    if i == 5:
        continue
    print(i, " : ", "*" * i)
