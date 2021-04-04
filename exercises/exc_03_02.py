import ___ as ___

X = np.load("exercises/data/X.npy")
y = np.load("exercises/data/y.npy")
b = np.load("exercises/data/b.npy")

y_pred = ___ + ___*___        # the predicted values
residuals_sq = ____           # squared residuals
RMSE = ___                    # square root of average residuals squared

print(f"RMSE = {RMSE: .2f}")
