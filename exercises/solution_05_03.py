import pandas as pd

# read in the data
df = pd.read_csv("exercises/data/fmri_data.csv", sep=';')
display(df.head())

# take only the parietal region
parietal_df = df[df["region"] == "parietal"]
# save as Excel file
parietal_df.to_excel("parietal_sample.xlsx")
