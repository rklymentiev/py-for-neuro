from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

# import the file
h1_data = loadmat(
    file_name="exercises/data/H1_neuron.mat",
    squeeze_me=True # squeeze the file to remove empty indexes
    )

# create a new key with the time points
# from 0 to the length of the data
h1_data["timepnt"] = np.arange(0, len(h1_data['rho']), 1)
# select only those time point when spike occurred
h1_data["spike_time"] = h1_data["timepnt"][h1_data["rho"]  == 1]
# set the window size (timepoints)
window = 150

# create a vector of zeros with the shape (window,)
h1_data["sta"] = np.zeros(shape=(window,))
# iterate over all timepoints when spike occurred
# and use the time point as a end index
# note that we cannot take the window of length 150 for first 149 observations
for end_index in h1_data["spike_time"][h1_data["spike_time"]>window]:
    # specify the start index of a window
    start_index = end_index - window
    # take the slice from the stimulus value
    sample = h1_data["stim"][start_index:end_index]
    # add the slice to the STA vector
    h1_data["sta"] += sample

# divide the resulting STA vector on the amount of time points
# to get the actual average
h1_data["sta"] /= len(h1_data["spike_time"][h1_data["spike_time"]>window])

plt.figure(figsize=(10,5), facecolor="white")
plt.plot(range(0, 300, 2), h1_data["sta"])
plt.title('Spike-Triggered average', fontsize=18)
plt.ylabel('Stimulus Value, [mV]')
plt.xlabel('Time, [ms]')
plt.show()
