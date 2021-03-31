import numpy as np

X = np.load("exercises/numpy/X.npy")
y = np.load("exercises/numpy/y.npy")

b = np.linalg.inv(X.T @ X) @ X.T @ y

print(f"Linear Regression Model: Accuracy = {b[0]:.2f} + {b[1]:.2f}*TAI")
