import numpy as np
import matplotlib.pyplot as plt

# Define grid size
rows, cols = 50, 50

# Create coordinate arrays
x = np.linspace(0, 1, cols)
y = np.linspace(0, 1, rows)
X, Y = np.meshgrid(x, y)

# Generate a gradient based on position
# For example, red to blue gradient
colors = np.zeros((rows, cols, 3))
colors[:, :, 0] = X  # Red channel varies across columns
colors[:, :, 2] = Y  # Blue channel varies across rows

# Display the colored grid
plt.imshow(colors, origin='lower')
plt.axis('off')  # Hide axes
plt.title("Gradient Color Pattern")
plt.show()
