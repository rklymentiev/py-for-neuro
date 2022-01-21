___ ___ as pd

dementia_df = ___.read_csv("exercises/data/oasis_cross-sectional.csv")

avg_ses1 = dementia_df[___][___].___()
avg_ses2 = ____.loc[___, ___].___()

print(avg_ses1 == avg_ses2)  # check that values are the same
print(round(avg_ses1, 1))
