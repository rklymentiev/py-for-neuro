import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = 'white'

# read in the data
dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

sns.relplot(
    data=dementia_df,
    x="eTIV",
    y="nWBV",
    col="CDR", # split by columns by group
    hue="M/F", # color points according to the group
    size="ASF", # change the size of a point according to the value
    sizes=(5, 500), # scale of the points
    col_wrap=2 # split to two columns
)
plt.show()
