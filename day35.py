# Recursive Fractal Pattern (Sierpinski Triangle)
def sierpinski(n):
    size = 2 ** n
    for i in range(size):
        for j in range(2 * size - 1):
            if (j // (size // 2) + i // (size // 2)) % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()

n = 4  # Adjust for complexity
sierpinski(n)
