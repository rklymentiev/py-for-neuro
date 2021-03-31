import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read in the data
cancer_df = pd.read_csv("exercises/data/breast_cancer.csv")
# select the columns with 'mean' in the name
selected_columns = list(filter(lambda x: "mean" in x, cancer_df.columns))
# find the correlations
corr_matrix = cancer_df[selected_columns].corr()

# make a plot
plt.figure(figsize=(8,7), facecolor='white')
sns.heatmap(data=corr_matrix, cmap="YlGnBu")
plt.title("Correlation Among Variables")
plt.show()
