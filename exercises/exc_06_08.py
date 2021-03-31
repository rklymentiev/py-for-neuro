import pandas as ___
import ___.pyplot as plt
import seaborn as ___

# read in the file
dementia_df = pd.___("exercises/data/oasis_cross-sectional.csv")

# thresholds for outliers detection (mu ± 2*sigma)
lower_bound = dementia_df['ASF'].___() - 2*dementia_df['ASF'].___(ddof=1)
upper_bound = dementia_df['ASF'].___() + 2*dementia_df['ASF'].___(ddof=1)

plt.figure(figsize=(10,6), facecolor="white")
plt.subplot(211)
# histogram
sns.___(x=dementia_df['ASF'], color="lightblue", linewidth=2)
# add lines with thresholds
plt.axvline(
    x=lower_bound, linestyle="dashed",
    color="red", label="$\mu ±2 \sigma$")
plt.axvline(x=___, linestyle="dashed", color="red")
plt.xticks([])
plt.xlabel("")
plt.title("Distribution of atlas scaling factor (ASF)", fontsize=18)
plt.legend()

plt.___(212)
# boxplot
sns.___(x=dementia_df['ASF'], color="lightblue", width=0.5, linewidth=2)
plt.___()

# filter those observations that are beyond the threshold values
condition = (___ < ___) ___ (___ > ___)
outliers_df = ___[condition]
print("\nObservations with extreme ASF values:")
display(outliers_df)
