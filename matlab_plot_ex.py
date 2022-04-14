import numpy as np
import matplotlib.pyplot as plt

# Compute X & Y Coordinates
x = np.arange(0, 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up the subplot grid
plt.subplot(2, 1, 1)

# Make the first plot
plt.plot(x, y_sin)
plt.title("Sine")

# Set th second subplot
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title("Cosine")

# Show the figure
plt.show()
