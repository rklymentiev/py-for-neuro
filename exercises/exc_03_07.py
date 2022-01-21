import pickle
___ numpy ___ np
import matplotlib.pyplot as plt

# load the pickled file
with open("exercises/data/eeg_sample.pickle", mode="rb") as f:
    eeg = pickle.load(file=f)

# filter the elements in the array to find the location (index) of channel C1
c1_loc = eeg[___] ___ ___
# slice the array with the data using the index of C1 location and
# 1000:2001 bounds for time axis (bounds correspond to 2 and 4s or recordings)
c1_data = eeg[___][___, ___]

# find the max, min and mean value of the c1_data array
max_v = c1_data.___()
min_v = ___.___()
mean_v = ___.___()

# find the indexes (time point) of max and min values
t_max_v = np.where(c1_data[0, :] ___ ___)
t_min_v = np.where(c1_data[0, :] ___ ___)

# print out the results using f-string.
# convert volts to microvolts and round up the outcome values to the 2 digit
print(___"""
    Max value: ___, microV
    Min value: ___, microV
    Average value: ___, microV
""")

# plot the results
plt.figure(figsize=(10,5), facecolor="white")
plt.plot(c1_data[0, :], c='black', label='Signal')
plt.plot(t_max_v, max_v, 'o', c='red', label='Maximum Value')
plt.plot(t_min_v, min_v, 'o', c='blue', label='Minimum Value')
plt.axhline(y=mean_v, linestyle='dashed', lw=1, label='Average Value')
plt.title('Sample of the Signal', fontweight='bold', fontsize=18)
plt.xlabel('Time point')
plt.ylabel('Voltage, [V]')
plt.legend()
plt.show()
