# Alphabet Pattern (Alphabet Pyramid)
n = 5
import string
letters = string.ascii_uppercase
for i in range(n):
    # Spaces before
    print(" " * (n - i - 1), end="")
    # Print characters
    for j in range(i + 1):
        print(letters[j], end=" ")
    print()
