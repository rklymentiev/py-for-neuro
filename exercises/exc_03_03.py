___ ___ ___ ___

oasis_df = ___.read_csv("exercises/data/oasis_cross-sectional.csv")

avg_ses1 = oasis_df[___][___].___()
avg_ses2 = oasis_df.loc[___, ___].___()

print(avg_ses1 == avg_ses2)  # check that values are the same
print(round(avg_ses1, 1))
