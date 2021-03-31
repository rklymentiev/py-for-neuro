import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

p = 0.38
n = 65

# 1. Probability that X>=25
k = 25
p_x25 = stats.binom.sf(k=k-1, n=n, p=p)
print(f"P(X>=25)={p_x25:.3f}")

# 2. Probability that X=20
k = 18
p_x18 = stats.binom.pmf(k=k, n=n, p=p)
print(f"P(X=18)={p_x18:.3f}")

# 3. Probability Mass Function
x = np.arange(0, n+1) # sample space (0, 1, ..., n)
pmf = stats.binom.pmf(k=x, n=n, p=p)

plt.figure(figsize=(10,5), facecolor="white")
plt.bar(x=x, height=pmf, color="lightblue")
plt.xticks(rotation=-45)
plt.title("PMF", fontsize=18)
plt.xlabel("Amount of patients with the side effect")
plt.show()
