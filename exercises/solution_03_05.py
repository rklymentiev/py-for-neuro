import pandas as pd

table_1 = pd.read_json("exercises/data/table1.json")
table_2 = pd.read_json("exercises/data/table2.json")

joined_table = pd.merge(left=table_1, right=table_2, how="inner",
                        left_on="id", right_on="ID")

radius_mean_benign = joined_table[joined_table['diagnosis'] == 'benign']['radius_mean'].mean()
radius_mean_malignant = joined_table[joined_table['diagnosis'] == 'malignant']['radius_mean'].mean()

print(radius_mean_malignant > radius_mean_benign)
