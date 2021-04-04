___ ___ ___ ___

dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

agg_df = dementia_df.___(by=___).___({___: ___, ___: ___})
print("Original:")
display(agg_df)

agg_df.rename(columns={___: "Count", ___: "nWBV_median"}, inplace=True)
print("Renamed:")
display(agg_df)
