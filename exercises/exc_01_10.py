import matplotlib.pyplot as plt

N = 1000           # number of measurememnts (time points)
g_L = 0.7          # leak conductance [nS]
c_m = 20           # conductance [nF/mm^2]
tau_m = ___        # membrane time constant [ms]
i = 50             # input current [nA]
v_reset = -65      # reset potential [mV]
v_thresh = -50     # threshold [mV]
dt = 0.1           # time step
E_L = -75          # leak reversal potential [mV]
v = [v_reset]      # list of potential values, start at v_reset

for _ in range(___): # loop over all time points
    # increment of membrane potential
    dv = ___
    v_new = ___ + dv     # new membrane potential value
    if v_new ___ v_thresh:  # check if new value exceeds threshold
        v.___(___)  # add reset value, if true
    else:
        v.___(___)  # add new value to the list otherwise

plt.figure(figsize=(10,5), facecolor="white")
plt.plot(v, color='black', lw=4)
plt.axhline(
    v_thresh, linestyle='dashed',
    lw=1, label='Threshold',
    color='red')
plt.axhline(
    v_reset, linestyle='dashed',
    lw=1, label='Reset',
    color='blue')
plt.legend()
plt.xlabel('Time point')
plt.ylabel('V, [mV]')
plt.title('Membrane potential', fontsize=14, fontweight='bold')
plt.show()
