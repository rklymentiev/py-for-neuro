___

table_1 = pd.read_json("exercises/data/table1.json")
table_2 = pd.read_json("exercises/data/table2.json")

joined_table = pd.merge(left=___, ___=table_2, how=___,
                        left_on=___, ___=___)

radius_mean_benign = joined_table[___]['radius_mean'].___()
radius_mean_malignant = ___

print(radius_mean_malignant > radius_mean_benign)
