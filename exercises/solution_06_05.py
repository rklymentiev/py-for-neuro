import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(1) # seed for reproducibility

alpha = 0.05    # significance level
null_mean = 0.5 # value under the null hypothesis
n = 20          # sample size

sample = np.random.rand(n).round(2) # random values in a range [0, 1]
sample_mean = sample.mean()
sample_std = sample.std(ddof=1) # standard deviation
se = sample_std / np.sqrt(n)    # standard error

t_score = (sample_mean - null_mean) / se
p_val = 1 - stats.t.sf(t_score, df=n-1)
t_crit = stats.t.ppf(alpha, df=n-1) # threshold value

x = np.linspace(start=-4, stop=4, num=300) # values for the plot
t_dist = stats.t.pdf(x, df=n-1)            # pdf

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
