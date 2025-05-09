# Number Pyramid with Repeating Numbers
n = 5
for i in range(1, n + 1):
    # Spaces
    for j in range(n - i):
        print(" ", end=" ")
    # Numbers
    for k in range(1, i + 1):
        print(k, end=" ")
    # Print the same pattern in reverse
    for k in range(i - 1, 0, -1):
        print(k, end=" ")
    print()
