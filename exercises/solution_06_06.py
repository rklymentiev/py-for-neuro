import numpy as np
from scipy.stats import ttest_1samp
from pingouin import ttest

np.random.seed(1) # seed for reproducibility

null_mean = 0.5 # value under the null hypothesis
n = 20          # sample size
sample = np.random.rand(n).round(2) # random values in a range [0, 1]

# scipy implementation
print("==scipy.stats implementation==")
t_score, p_val = ttest_1samp(a=sample, popmean=null_mean, alternative="less")
print(f"t score={t_score:.3f}, p-val={p_val:.3f}")

# pingouin implementation
print("\n==pingouin implementation==")
result = ttest(x=sample, y=null_mean, alternative="less")
display(result.round(3))
