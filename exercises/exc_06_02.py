import matplotlib.___ as plt
import ___ as sns
import pandas as ___
import pingouin as pg
from ___ import stats

# read in the data
dementia_df = ___

# create a boxplot
plt.figure(figsize=(9,5), facecolor="white")
sns.boxplot(
    x=___, y=___,
    data=___, palette="vlag",
    width=.5, showmeans=True)
# add points to the plot
sns.stripplot(
    x="CDR", y="nWBV",
    data=__, size=4,
    color=".3", linewidth=0)
plt.title(
    "Distribution of eTIV",
    fontsize=18)
plt.show()

# scipy.stats implementation:
F_stat, p_val = stats.f_oneway(
    dementia_df["nWBV"][dementia_df[___] == 0],
    dementia_df["nWBV"][dementia_df[___] == 0.5],
    dementia_df[___][dementia_df["CDR"] == 1])

print("==scipy.stats implementation==")
print(f"Calculated test statistic: {___: .3f}\np-value: {___: .3f}")

# pingouin implementation:
result = pg.anova(
    dv=___, # dependent variable
    between='CDR', # between-subject factor
    data=dementia_df[___], # don't forget to filter the df
    detailed=True)

print("\n==pingouin implementation==")
display(result)
