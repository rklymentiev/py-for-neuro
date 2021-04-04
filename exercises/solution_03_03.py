import pandas as pd

dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

avg_ses1 = dementia_df[dementia_df['CDR'] == 0.0]['SES'].mean()
avg_ses2 = dementia_df.loc[dementia_df['CDR'] == 0.0, "SES"].mean()

print(avg_ses1 == avg_ses2)  # check that values are the same
print(round(avg_ses1, 1))
