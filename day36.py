# Diamond Pattern with Alphabets
n = 5
for i in range(n):
    print(" " * (n - i - 1) + " ".join(chr(65 + j) for j in range(i + 1)))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + " ".join(chr(65 + j) for j in range(i + 1)))
