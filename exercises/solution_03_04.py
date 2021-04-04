import pandas as pd

dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

agg_df = dementia_df.groupby(by="CDR").agg({"ID": "count", "nWBV": "median"})
print("Original:")
display(agg_df)

agg_df.rename(columns={"ID": "Count", "nWBV": "nWBV_median"}, inplace=True)
print("Renamed:")
display(agg_df)
