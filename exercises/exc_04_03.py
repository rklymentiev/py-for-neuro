import ___ as pd
import ___ as sns
import ___.___ as plt

# read in the data
dementia_df = ___

plt.figure(figsize=(10,7), facecolor="white")

# add first figure to the 2x2 plot with age ("Age")
plt.subplot(___,___,___)
sns.___(
    x=___, data=___, y=___,
    hue= ___, ci="sd", color="lightblue")
plt.title("Age (Mean ± SD)")

# add sedond figure to the 2x2 plot
# with years of education ("Educ")
plt.subplot(___,___,___)
sns.___(
    x=___, data=___, y=___,
    hue= ___, ci="sd", color="lightblue")
plt.title("Years of education (Mean ± SD)")

# add third figure to the 2x2 plot
# with socioeconomic status ("SES")
plt.subplot(___,___,___)
sns.___(
    x=___, data=___, y=___,
    hue= ___, ci="sd", color="lightblue")
plt.title("Socioeconomic status (Mean ± SD)")

# add third fourth to the 2x2 plot
# with Mini-Mental State Examination score ("MMSE")
plt.subplot(___,___,___)
sns.___(
    x=___, data=___, y=___,
    hue= ___, ci="sd", color="lightblue")
plt.title("Mini-Mental State Examination score (Mean ± SD)")

plt.tight_layout() # adjust the padding between and around subplots
___.___()

print("Summary statistics:")

# get the numerical values
summary_stats = dementia_df.___(by=[___, ___]).___(
    {___: "count", ___: ["mean", "std"], ___: ___,
     ___: ___, "MMSE": ___}).round(2)

display(summary_stats)
