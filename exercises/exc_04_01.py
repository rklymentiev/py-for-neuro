___
import seaborn as ___
import ___.___ as plt

# read in the data
___ = ___.___(___)

plt.figure(facecolor="white")
# regression plot
sns.regplot(x=___, y=___, data=___, x_ci='sd')
# add the vertical line with the average radius_mean
plt.axvline(x=___, color=___, linewidth=___, linestyle=___)
# add the horizontal line with the average texture_mean
plt.axhline(y=____, color=___, linewidth=___, linestyle=___)
plt.title("Radius vs Texture")
# show the figure
___.___()
