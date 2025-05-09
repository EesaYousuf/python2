#  Wave Pattern
import math
rows = 6
cols = 30
for i in range(rows):
    for j in range(cols):
        if math.sin(j / 3.0 + i) > 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
