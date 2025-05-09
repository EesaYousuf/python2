#  Butterfly Pattern
n = 5
# Upper part
for i in range(1, n + 1):
    # Left stars
    for j in range(i):
        print("*", end=" ")
    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    # Right stars
    for j in range(i):
        print("*", end=" ")
    print()

# Lower part
for i in range(n, 0, -1):
    # Left stars
    for j in range(i):
        print("*", end=" ")
    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    # Right stars
    for j in range(i):
        print("*", end=" ")
    print()
