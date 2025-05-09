# Number Pattern (Pyramid of Numbers)
n = 5
for i in range(1, n + 1):
    # Spaces
    for j in range(n - i):
        print(" ", end=" ")
    # Numbers
    for k in range(1, i + 1):
        print(k, end=" ")
    print()