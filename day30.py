#  Concentric Square Pattern
n = 7
size = 2 * n - 1
for i in range(size):
    for j in range(size):
        # Determine the minimum distance to the edges
        min_dist = min(i, j, size - 1 - i, size - 1 - j)
        print(n - min_dist, end=" ")
    print()
