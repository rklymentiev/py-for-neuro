import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read in the data
cancer_df = pd.read_csv("exercises/data/breast_cancer.csv")

plt.figure(facecolor="white")
# regression plot
sns.regplot(x="radius_mean", y="texture_mean", data=cancer_df, x_ci='sd')
# add the vertical line with the average radius_mean
plt.axvline(x=cancer_df["radius_mean"].mean(),
            color='black', linewidth=1, linestyle='dashed')
# add the horizontal line with the average texture_mean
plt.axhline(y=cancer_df["texture_mean"].mean(),
            color='black', linewidth=1, linestyle='dashed')
plt.title("Radius vs Texture")
# show the figure
plt.show()
