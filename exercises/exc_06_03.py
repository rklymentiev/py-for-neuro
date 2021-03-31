import ___ as pd
import ___ as pg

# read in the data
dementia_df = ___

result = pg.pairwise_ttests(
    dv=___,          # dependent variable
    between=___,     # between-subject factor
    data= ___,       # don't forget to filter the df
    padjust="bonf",  # Bonferroni correction of pvalues
    effsize="cohen"  # include Cohen d effect size
)

display(result.round(2))
