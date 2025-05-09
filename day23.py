#  Diamond Pattern
n = 5
# Upper part
for i in range(1, n + 1):
    # Spaces
    for j in range(n - i):
        print(" ", end=" ")
    # Stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
# Lower part
for i in range(n - 1, 0, -1):
    # Spaces
    for j in range(n - i):
        print(" ", end=" ")
    # Stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()