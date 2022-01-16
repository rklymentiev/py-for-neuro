import pprint
import ___ as pd
from ___ import compute_bootci

# read in the file
dementia_df = ___

# create an empty dictinary
nwbv_estimation = ___

for ___ in [0, 0.5, 1]: # iterate over possible CDR values
    # average values of a sample
    x_bar = dementia_df[___][dementia_df[___] == ___].___()
    # add to the dictinary
    nwbv_estimation[___] = {"mean": round(x_bar, 4)}
    ci = ___(
        x=dementia_df[___][dementia_df[___] == ___], # sample
        func='mean',     # CI for the mean
        method='norm',   # normal approximation method
        confidence=0.95, # confidence level
        decimals=4)      # number of rounded decimals to return
    # uodate the dictinary value
    nwbv_estimation[___].___({"CI": ci})

pprint.pprint(nwbv_estimation)
