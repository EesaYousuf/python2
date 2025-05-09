# Hourglass Pattern
n = 5
for i in range(n):
    # Upper part
    for j in range(i):
        print(" ", end=" ")
    for k in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()

for i in range(1, n):
    # Lower part
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
