import pickle
import pandas as pd

# read in the fMRI file
fmri_df = pd.read_csv(___)

# split into two DataFrames according to the region
frmi = {
    "parietal": ___,
    "frontal": ___
}

# write the resulting dictionary as pickle file
with open(file="frmi_dict.pickle", mode="wb") as ___:
    pickle.dump(obj=___, file=___)

# read in pickle file
with open(file=___, mode=___) as ___:
    output = pickle.load(file=___)

# print out the keys of the loaded dictionary
display(output['parietal'].head())
display(output['frontal'].head())
