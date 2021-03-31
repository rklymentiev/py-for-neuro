import pandas as pd

table_1 = pd.read_json("exercises/data/table1.json")
table_2 = pd.read_json("exercises/data/table2.json")

joined_table = pd.merge(left=table_1, right=table_2, how="right",
                        left_on="id", right_on="ID") 
joined_table.drop(labels="id", axis=1, inplace=True)
joined_table["diagnosis"] = joined_table["diagnosis"].fillna("unknown")

display(joined_table)
