import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pingouin as pg
from scipy import stats

# read in the data
dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

result = pg.pairwise_ttests(
    dv='nWBV', # dependent variable
    between='CDR', # between-subject factor
    data=dementia_df[dementia_df["CDR"] != 2], # don't forget to filter the df
    padjust="bonf", # Bonferroni correction of pvalues
    effsize="cohen" # include Cohen d effect size
)

display(result.round(2))
