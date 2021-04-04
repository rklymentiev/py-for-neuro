import numpy as np

X = np.load("exercises/data/X.npy")
y = np.load("exercises/data/y.npy")
b = np.load("exercises/data/b.npy")

y_pred = b[0] + b[1]*X[:,1]           # the predicted values
# or
# y_pred = X @ b
residuals_sq = (y_pred - y)**2        # squared residuals
RMSE = np.sqrt(np.mean(residuals_sq)) # square root of average residuals squared

print(f"RMSE = {RMSE: .2f}")
