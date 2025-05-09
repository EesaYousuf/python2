# pattern print
n=4
for i in range(4):
    print("*" *(i+1))    # print simple patterns in python
    # 1. Right-Angled Triangle Pattern
    # ************************************ end="\n"*******************************************************************
    print()
    n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


