#  Squares Grid Pattern with Colors
import matplotlib.pyplot as plt
import numpy as np

# Define grid size
rows, cols = 8, 8

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Loop through grid positions
for i in range(rows):
    for j in range(cols):
        # Create a rectangle at position (j, i)
        # with size 1x1
        rect = plt.Rectangle(
            (j, i), 1, 1,
            facecolor=plt.cm.tab20(np.random.randint(0, 20)),
            edgecolor='black'
        )
        ax.add_patch(rect)

# Set limits and aspect
ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
ax.set_aspect('equal')
ax.axis('off')  # Hide axes

plt.title('Colored Squares Grid Pattern')
plt.show()
 
