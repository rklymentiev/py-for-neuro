import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read in the file
dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

# thresholds for outliers detection (mu ± 2*sigma)
lower_bound = dementia_df['ASF'].mean() - 2*dementia_df['ASF'].std(ddof=1)
upper_bound = dementia_df['ASF'].mean() + 2*dementia_df['ASF'].std(ddof=1)

plt.figure(figsize=(10,6), facecolor="white")
plt.subplot(211)
# histogram
sns.histplot(x=dementia_df['ASF'], color="lightblue", linewidth=2)
# add lines with thresholds
plt.axvline(
    x=lower_bound, linestyle="dashed",
    color="red", label="$\mu ±2 \sigma$")
plt.axvline(x=upper_bound, linestyle="dashed", color="red")
plt.xticks([])
plt.xlabel("")
plt.title("Distribution of atlas scaling factor (ASF)", fontsize=18)
plt.legend()

plt.subplot(212)
# boxplot
sns.boxplot(x=dementia_df['ASF'], color="lightblue", width=0.5, linewidth=2)
plt.show()

# filter those observations that are beyond the threshold values
condition = (dementia_df['ASF'] < lower_bound) | (dementia_df['ASF'] > upper_bound)
outliers_df = dementia_df[condition]
print("\nObservations with extreme ASF values:")
display(outliers_df)
