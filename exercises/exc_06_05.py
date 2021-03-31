import ___ as np
import ___.___ as plt
from ___ import ___

np.random.seed(1) # seed for reproducibility

alpha = ___     # significance level
null_mean = ___ # value under the null hypothesis
n = ___         # sample size

sample = np.random.rand(n).round(2) # random values in a range [0, 1]
sample_mean = sample.___
sample_std = sample.___(ddof=___) # standard deviation
se = ___                          # standard error

t_score = ___
p_val = ___
t_crit = ___ # threshold value

x = np.linspace(start=-4, stop=4, num=300) # values for the plot
t_dist = stats.t.___(x, df=n-1)            # pdf

print(f"t score={t_score:.2f}, p-val={p_val:.2f}")

plt.figure(figsize=(10,5), facecolor="white")
plt.plot(x, t_dist, color="black", linewidth=3, label="Null distribution")
# vertical lines with t score and t critical
plt.axvline(x=t_score, color="blue", label="Observed value")
plt.axvline(x=t_crit, color="red", label="Threshold value")
# shade area under the curve
plt.fill_between(x[x<=t_crit], t_dist[x<=t_crit], color='red', alpha=0.5,
                 label="Rejection area (alpha)")
plt.fill_between(x[x<=t_score], t_dist[x<=t_score], color='blue', alpha=0.5,
                 label="p-value")
plt.xlabel("t")
plt.ylabel("Density")
plt.legend()
plt.show()
