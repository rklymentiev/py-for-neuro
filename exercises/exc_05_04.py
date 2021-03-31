from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

# import the file
h1_data = ___("exercises/data/H1_neuron.mat", squeeze_me=True)

# amount of timepoints to keep
n = 250
# slice of an `rho` array
spikes = ___
# slice of an `stim` array
stimulus = ___
# time points for the slice
timepoints = ___
# select only those when spike occurred
timepoints = ___

plt.figure(figsize=(10,5), facecolor="white")
plt.vlines(
    x=___,     # time points when spike occurred
    ymin=___,  # lower end of a line
    ymax=___,  # upper end of a line
    linewidth=1,
    label="Spike")
# plot stimulus values
plt.plot(___, label="Stimulus")
plt.legend()
plt.title("Fly H1 neuron response to\napproximate white-noise visual motion stimulus")
plt.xlabel('Time step')
plt.ylabel('Stimulus value, mV')
plt.show()
