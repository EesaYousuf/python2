#  Pascal’s Triangle
rows = 10
for i in range(rows):
    # Print spaces for alignment
    print(' ' * (rows - i - 1), end='')
    number = 1
    for j in range(i + 1):
        print(f"{number} ", end='')
        number = number * (i - j) // (j + 1)
    print()
