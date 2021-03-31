from scipy import stats
import matplotlib.pyplot as ___
import ___ as pd
import numpy as ___

# read in the data
dementia_df = ___.___(___)

# cross table with count of observation for each CDR&Educ combination
ct = pd.___(
    index=dementia_df["Educ"],
    columns=dementia_df["CDR"])

print("Cross table:")
display(ct)

# extract the test results
chisq_stat, p_val, dof, expctd = stats.chi2_contingency(
    observed=___)

alpha = ___ # significance level
# percent point function (P[Chi-squared]<q)
threshold = stats.chi2.ppf(q=___, df=___) # chi-squared critical

# values for the PDF plot
x = np.linspace(0, 30, 1000)
y = stats.chi2.___(x=x, df=dof) # probability density function

plt.figure(figsize=(9,5), facecolor="white")
plt.plot(x, y, color="black", linewidth=3, label="Null distribution")
plt.axvline(x=chisq_stat, color="blue", label="Observed value")
plt.axvline(x=threshold, color="red", label="Threshold value")
plt.fill_between(
    x[x>=threshold], y[x>=threshold],
    color='red', alpha=0.5,
    label="Rejection area (alpha)")
plt.fill_between(
    x[x>=chisq_stat], y[x>=chisq_stat],
    color='blue', alpha=0.5, label="p-value")
plt.legend()
plt.xlabel("Chi squared")
plt.ylabel("Density")
plt.title("Null Distribution")
plt.show()

print(f"Chi-squared={chisq_stat:.2f}, p-val={p_val:.2f}")
if p_val ___ alpha:
    print("Reject the H_0 in favor of H_A")
else:
    print("Fail to reject the H0")
