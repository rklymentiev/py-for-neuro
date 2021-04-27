import pickle
import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

with open("exercises/data/eeg_sample.pickle", mode="rb") as f:
    eeg = pickle.load(file=f)

print(eeg.keys())

fc_1 = np.fft.fft()
