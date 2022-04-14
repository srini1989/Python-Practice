import numpy as np
# We will add the vector v to each row of the matrix

x = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([1, 0, 1])
y = x + v
print(y)
