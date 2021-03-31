import ___
import ___
import ___
plt.rcParams['figure.facecolor'] = 'white'

# read in the data
dementia_df = ___

sns.relplot(
    data=___,
    x=___,
    y=___,
    col=___,        # split by columns by group
    hue=___,        # color points according to the group
    size=___,       # change the size of a point according to the value
    sizes=(5, 500), # scale of the points
    col_wrap=2      # split to two columns
)
plt.show()
