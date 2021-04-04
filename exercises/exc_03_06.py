import pandas as pd

table_1 = pd.read_json("exercises/data/table1.json")
table_2 = pd.read_json("exercises/data/table2.json")

joined_table = ___  # join two tables together
joined_table.___(labels=___, ___=1, inplace=___) # drop the redundant column
___                 # replace the missing values in a column

display(joined_table)
