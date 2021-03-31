import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pingouin as pg
from scipy import stats

# read in the data
dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

# create a boxplot
plt.figure(figsize=(9,5), facecolor="white")
sns.boxplot(
    x="CDR", y="nWBV",
    data=dementia_df, palette="vlag",
    width=.5, showmeans=True)
# add points to the plot
sns.stripplot(
    x="CDR", y="nWBV",
    data=dementia_df, size=4,
    color=".3", linewidth=0)
plt.title(
    "Distribution of eTIV",
    fontsize=18)
plt.show()

# scipy.stats implementation:
F_stat, p_val = stats.f_oneway(
    dementia_df["nWBV"][dementia_df["CDR"] == 0],
    dementia_df["nWBV"][dementia_df["CDR"] == 0.5],
    dementia_df["nWBV"][dementia_df["CDR"] == 1])

print("==scipy.stats implementation==")
print(f"Calculated test statistic: {F_stat: .3f}\np-value: {p_val: .3f}")

# pingouin implementation:
result = pg.anova(
    dv='nWBV', # dependent variable
    between='CDR', # between-subject factor
    data=dementia_df[dementia_df["CDR"] != 2], # don't forget to filter the df
    detailed=True)

print("\n==pingouin implementation==")
display(result)
