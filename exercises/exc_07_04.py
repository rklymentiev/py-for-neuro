import numpy as ___
import ___.pyplot as plt
from ___ import softmax

# specify random generator
rnd_generator = np.random.default_rng(seed=123)
# colors for the plot
colors_opt = ['#82B223', '#2EA8D5', '#F5AF3D']

n_arms = ___    # number of arms (slot machines)
opts = list(range(n_arms)) # option numbers (0, 1, ..., n_arms)
n_trials = 100  # number of trials
alpha = 0.3     # learning rate
beta = 2        # inverse temperature
rew_prob = [0.2, 0.4, 0.8]  # probability of reward for each arm

# arrays that will hold historic values
# selected option at each trial
actions = np.zeros(shape=(n_trials,), dtype=np.int32)
# observed reward at each trial
rewards = np.zeros(shape=(n_trials,), dtype=np.int32)
# value function for each option at each trial
Qs = np.zeros(shape=(n_trials+1, n_arms))
# note that before the first trial agent has already expectations of each
# option (0s in our case). That means that on the trial t we are going to
# uodate the Q for the (t+1) trial. To update the value function on the last
# trial we include `+1` in the Q array shape

for t in range(___): # loop over all trials

    # choose the action based of softmax function
    prob_a = softmax(___ * ___) # probability of selection of each arm
    a = rnd_generator.choice(a=opts, p=___)  # select the option
    # list of actions that were not selected
    a_left = opts.copy()
    a_left.___(___) # remove the selected option
    # check if arm brigns reward
    if rnd_generator.random() < ___[___]:
        r = 1
    else:
        r = 0
    # value function update for the chosen arm
    Qs[t+1, a] = Qs[___, a] + ___ * (___ - ___)
    # update the values for non chosen arms
    for a_l in a_left:
        ___ = ___
    # save the records
    actions[t] = a
    rewards[t] = r

# calculate cumulative reward
cum_rew = rewards.___()
# count how many times each arm was chosen
unique, counts = np.unique(actions, return_counts=True)

plt.figure(figsize=(10,5), facecolor="white", )

plt.subplot(221)
for i in range(n_arms):
    plt.plot(
        Qs[:, i],
        color=colors_opt[i],
        lw=2,  #line width
        label=f'Arm #{i+1}'
    )
plt.xlabel('Trial')
plt.ylabel('Value Function')
plt.legend()

plt.subplot(223)
plt.plot(cum_rew, color='black')
plt.xlabel('Trial')
plt.ylabel('Cumulative Reward')

plt.subplot(122)
plt.bar((unique + 1).astype(str), counts, color=colors_opt)
plt.xlabel('Arm Number')
plt.ylabel('# of Times Chosen')

plt.suptitle('Agent\'s Performance', fontweight='bold')
plt.tight_layout()
plt.___()
