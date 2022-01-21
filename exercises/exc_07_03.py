import pickle
import numpy as ___
from scipy.fft import fft
import ___.pyplot as plt

# load the pickled file
with open(___, mode=___) as ___:
    eeg = ___.___(file=___)

# index of a FPz channel
fpz_index = np.where(___)[0][0]
# number of records
N = ___

# numpy realization of FFT
fc_np = np.fft.fft(a=___) / N
# scipy realization of FFT
fc_sp = fft(x=___) / N
# list of frequincies for plotting
hz = np.linspace(0, eeg['srate'], int(N))

plt.figure(figsize=(12,7), facecolor="white")
plt.subplot(2,1,1)
plt.plot(eeg['times'], eeg['data'][fpz_index, :])
plt.xlabel("Timepoint")
plt.ylabel("Amplitude")
plt.title("Signal in time domain")

plt.subplot(2,2,3)
plt.plot(hz, 2*np.abs(fc_sp), alpha=0.5, color="black")
plt.xlim([0, 10])
plt.ylabel("Amplitude")
plt.xlabel("Frequency, [Hz]")
plt.title("Signal in frequency domain (NumPy)")

plt.subplot(2,2,4)
plt.plot(hz, 2*np.abs(fc_np), alpha=0.5, color="blue")
plt.xlim([0, 10])
plt.ylabel("Amplitude")
plt.xlabel("Frequency, [Hz]")
plt.title("Signal in frequency domain (SciPy)")

plt.tight_layout()
plt.show()
