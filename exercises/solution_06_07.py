import pprint
import pandas as pd
from pingouin import compute_bootci

# read in the file
dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

# create an empty dictinary
nwbv_estimation = dict() # or nwbv_estimation = {}

for cdr_level in [0, 0.5, 1]: # iterate over possible CDR values
    # average values of a sample
    x_bar = dementia_df['nWBV'][dementia_df['CDR'] == cdr_level].mean()
    # add to the dictinary
    nwbv_estimation[cdr_level] = {"mean": round(x_bar, 4)}
    ci = compute_bootci(
        x=dementia_df['nWBV'][dementia_df['CDR'] == cdr_level], # sample
        func='mean',     # CI for the mean
        method='norm',   # normal approximation method
        confidence=0.95, # confidence level
        decimals=4)      # number of rounded decimals to return
    # uodate the dictinary value
    nwbv_estimation[cdr_level].update({"CI": ci})

pprint.pprint(nwbv_estimation)
