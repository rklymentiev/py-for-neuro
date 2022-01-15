import pickle
import pandas as pd

# read in the fMRI file
fmri_df = pd.read_csv(filepath_or_buffer="exercises/data/fmri_data.csv", sep=';')

# split into two DataFrames according to the region
frmi = {
    "parietal": fmri_df[fmri_df["region"] == "parietal"],
    "frontal": fmri_df[fmri_df["region"] == "frontal"]
}

# write the resulting dictionary as pickle file
with open(file="frmi_dict.pickle", mode="wb") as file:
    pickle.dump(obj=frmi, file=file)

# read in pickle file
with open(file="frmi_dict.pickle", mode="rb") as f:
    output = pickle.load(file=f)

# print out the keys of the loaded dictionary
display(output['parietal'].head())
display(output['frontal'].head())
