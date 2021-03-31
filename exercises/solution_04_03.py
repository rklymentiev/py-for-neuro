import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read in the data
dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

plt.figure(figsize=(10,7), facecolor="white")

# add first figure to the 2x2 plot with age ("Age")
plt.subplot(2,2,1)
sns.barplot(
    x="CDR", data=dementia_df, y="Age",
    hue="M/F", ci="sd", color="lightblue")
plt.title("Age (Mean ± SD)")

# add sedond figure to the 2x2 plot
# with years of education ("Educ")
plt.subplot(2,2,2)
sns.barplot(
    x="CDR", data=dementia_df, y="Educ",
    hue="M/F", ci="sd", color="lightblue")
plt.title("Years of education (Mean ± SD)")

# add third figure to the 2x2 plot
# with socioeconomic status ("SES")
plt.subplot(2,2,3)
sns.barplot(
    x="CDR", data=dementia_df, y="SES",
    hue="M/F", ci="sd", color="lightblue")
plt.title("Socioeconomic status (Mean ± SD)")

# add third fourth to the 2x2 plot
# with Mini-Mental State Examination score ("MMSE")
plt.subplot(2,2,4)
sns.barplot(
    x="CDR", data=dementia_df, y="MMSE",
    hue="M/F", ci="sd", color="lightblue")
plt.title("Mini-Mental State Examination score (Mean ± SD)")

plt.tight_layout() # adjust the padding between and around subplots
plt.show()

print("Summary statistics:")

# get the numerical values
summary_stats = dementia_df.groupby(by=["CDR", "M/F"]).agg(
    {"ID": "count", "Age": ["mean", "std"], "Educ": ["mean", "std"],
     "SES": ["mean", "std"], "MMSE": ["mean", "std"]}).round(2)

display(summary_stats)
