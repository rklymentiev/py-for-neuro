from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

# import the file
h1_data = loadmat(
    file_name="exercises/data/H1_neuron.mat",
    squeeze_me=True)

# amount of timepoints to keep
n = 250
# slice of an `rho` array
spikes = h1_data["rho"][:n]
# slice of an `stim` array
stimulus = h1_data["stim"][:n]
# time points for the slice
timepoints = np.arange(n)
# select only those when spike occurred
timepoints = timepoints[spikes == 1]

plt.figure(figsize=(10,5), facecolor="white")
plt.vlines(
    x=timepoints,        # time points when spike occurred
    ymin=stimulus.min(), # lower end of a line
    ymax=stimulus.max(), # upper end of a line
    linewidth=1,
    label="Spike")
# plot stimulus values
plt.plot(stimulus, label="Stimulus")
plt.legend()
plt.title("Fly H1 neuron response to\napproximate white-noise visual motion stimulus")
plt.xlabel('Time step')
plt.ylabel('Stimulus value, mV')
plt.show()
