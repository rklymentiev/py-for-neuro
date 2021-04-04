import numpy as np

X = np.load("exercises/data/X.npy")
y = np.load("exercises/data/y.npy")

b = np.linalg.inv(X.T @ X) @ X.T @ y

print(f"Linear Regression Model: Accuracy = {b[0]:.2f} + {b[1]:.2f}*TAI")
