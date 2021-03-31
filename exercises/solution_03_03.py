import pandas as pd

oasis_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

avg_ses1 = oasis_df[oasis_df['CDR'] == 0.0]['SES'].mean()
avg_ses2 = oasis_df.loc[oasis_df['CDR'] == 0.0, "SES"].mean()

print(avg_ses1 == avg_ses2)  # check that values are the same
print(round(avg_ses1, 1))
