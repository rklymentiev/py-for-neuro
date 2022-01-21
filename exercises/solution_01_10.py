import matplotlib.pyplot as plt

N = 1000           # number of measurememnts (time points)
g_L = 0.7          # leak conductance [nS]
c_m = 20           # conductance [nF/mm^2]
tau_m = c_m / g_L  # membrane time constant [ms]
i = 50             # input current [nA]
v_reset = -65      # reset potential [mV]
v_thresh = -50     # threshold [mV]
dt = 0.1           # time step
E_L = -75          # leak reversal potential [mV]
v = [v_reset]      # list of potential values, start at v_reset

for _ in range(N): # loop over all time points
    # increment of membrane potential
    dv = (-(v[-1] - E_L) + i/g_L) * dt / tau_m
    v_new = v[-1] + dv     # new membrane potential value
    if v_new >= v_thresh:  # check if new value exceeds threshold
        v.append(v_reset)  # add reset value, if true
    else:
        v.append(v_new)    # add new value to the list otherwise

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
