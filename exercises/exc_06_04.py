import ___ as np
import seaborn as ___
import matplotlib.___ as plt
from ___ import stats

p = ___
n = ___

# 1. Probability that X>=25
k = ___
p_x25 = stats.___.___(k=___, n=___, p=___)
print(f"P(X>=25)={p_x25:.3f}")

# 2. Probability that X=20
k = ___
p_x18 = stats.binom.___(k=___, n=___, p=___)
print(f"P(X=18)={p_x18:.3f}")

# 3. Probability Mass Function
x = np.arange(___, ___) # sample space (0, 1, ..., n)
pmf = ___.binom.___(k=___, n=___, p=___)

plt.figure(figsize=(10,5), facecolor="white")
plt.bar(x=___, height=___, color="lightblue")
plt.xticks(rotation=-45)
plt.title("PMF", fontsize=18)
plt.xlabel("Amount of patients with the side effect")
plt.show()
