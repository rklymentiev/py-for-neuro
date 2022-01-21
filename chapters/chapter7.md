---
title: 'Chapter 7: More Examples'
description:
  "Miscellaneous examples of other awesome stuff you could do with Python to deal with \"real-world\" problems."
prev: /chapter6
next: null
type: chapter
id: 7
---

<exercise id="1" title="Spike-triggered average">

**Exercise from the textbook Theoretical Neuroscience by Dayan and Abbott (Chapter 1, exercise 8)**:

`H1_neuron.mat` file contains data collected and provided by Rob de Ruyter van Steveninck from a fly H1 neuron responding to an approximate white-noise visual motion stimulus. Data were collected for 20 minutes at a sampling rate of 500 Hz. In the file, `rho` is a vector that gives the sequence of spiking events or nonevents at the sampled
times (every 2 ms). When an element of rho is one, this indicates the presence of a spike at the corresponding time, whereas a zero value indicates no spike. The variable `stim` gives the sequence of stimulus values at the sampled times. Calculate and plot the spike-triggered average from these data over the range from 0 to 300 ms (150 time
steps). (Based on a problem from Sebastian Seung.)

The **spike-triggered average (STA)** is a tool for characterizing the response properties of a neuron using the spikes emitted in response to a time-varying stimulus. The STA provides an estimate of a neuron's linear receptive field.

<center><img src="cases/sta.png"></center>

Here are 9 random stimulus values that lead to the spike in the H1 neuron:

<center><img src="cases/neuron_resp.png"></center>
<br>
<codeblock id="07_01">

* to create an array with integers you can use [`np.arange()`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) function;
* to include only spike times you need to apply a condition where `rho` array values equal `1`;
* select only those times that are greater than `window`;

</codeblock>

</exercise>

<exercise id="2" title="Reducing the uncertainty with Decision Tree model">

**Decision tree learning** is one of the predictive modeling approaches used in statistics, data mining and machine learning. It uses a decision tree (as a predictive model) to go from observations about an item (represented in the branches) to conclusions about the item's target value (represented in the leaves). Tree models where the target variable can take a discrete set of values are called classification trees; in these tree structures, leaves represent class labels and branches represent conjunctions of features that lead to those class labels. Decision trees where the target variable can take continuous values (typically real numbers) are called regression trees. Decision trees are among the most popular machine learning algorithms given their intelligibility and simplicity.

Credits: [Wikipedia](https://en.wikipedia.org/wiki/Decision_tree_learning)

<center><img src="https://defme.xyz/post/how-do-cart-models-work/trees.jpg" width="500"></center>

Classification and regression trees (CART for short) models are not the first-choice models when it comes to **prediction** because they tend to overfit the data (in other words they can predict quite good on the training data, but much worse on the test data), but they are really good in **explaining** the data structure. If you are interested in the math behind the model, check out the links below. However, you don't need to know much to complete the exercise.

To build a classification tree we are going to use a [`tree`](https://scikit-learn.org/stable/modules/tree.html) module from the [scikit-learn](https://scikit-learn.org/stable/index.html) package (which is the most popular library for machine learning in Python).

### Exercise. What features can be associated with the dementia rating?

1. Read in the data with dementia cases (path to file: `"exercises/data/oasis_cross-sectional.csv"`);
2. Drop the redundant columns: `"ID"` (ID label shouldn't be a predictor of Alzheimer's, should it?), `"Hand"` (all observations are right-handed) and `"Delay"` (most of the values are missing) and save it in the new data frame `model_data` (even though the columns might be meaningless, it's a good idea to keep the raw data);
3. Drop the rows with missing values. Note, this is a sloppy solution for a missing data problem. There are several methods on how you can artificially replace the missing values and some new algorithms can handle missing data during modeling, however, this is beyond this exercise;
4. We are going to build a binary classification tree: `0` for no dementia (CDR is 0) and `1` for dementia status (CDR is 0.5, 1 or 2). Create new binary column `dementia` and drop the `"CDR"` column;
5. scikit-learn models don't allow string columns (unlike models in R), that's why we often have to perform some sort of feature engineering. In our case we just need to convert gender column `M/F` to numerical binary - `1` if female, `0` otherwise;
6. Split the `model_data` into data frame with independent variables (all features, `X`) and a series with the dependent variable (binary, `y`) for later use;
7. Build a model using entropy for split criteria and set the maximum depth of the tree to 3;
8. Fit the data to the model and make a plot.

Further readings:
* Blog post: [How do CART models work](https://defme.xyz/post/how-do-cart-models-work/)
* YouTube video: [StatQuest: Decision Trees](https://youtu.be/7VeUPuFGJHk)

<codeblock id="07_02">

* don't forget about `inplace=True` in pandas methods applied on data frames;

</codeblock>

You can read this plot from top to bottom. The very first node is the initial data (`X` and `y`). 61.6% of the observations have no dementia (`dementia` = 0). At this node, model splits the data according to the Mini-Mental State Examination score (`MMSE`). If it's less than 27.5 we go left, if it's greater we go right (the left arrow is `True`, the right arrow is `False` for the `MMSE <= 27.5` condition). At each node, you can see the entropy in the `y` variable, fraction of observations from total and ratio of two classes. Note that the tree could be even more complicated, but we reduced it to 3 splits (or levels).

What is the expected outcome for the 50-year-old subject with Mini-Mental State Examination score (`MMSE`) 28, normalized whole brain volume (`nWBW`) 0.65?

<choice id="1">
<opt text="Dementia (with probability 28.6%)" >
For these feature values we have 71.4% of subjects with No Dementia and 28.6% with Dementia, so No Dementia is the expected outcome.
</opt>

<opt text="No Dementia (with probability 71.4%)" correct="true">
Probability is based on 35.6% of total number of samples.
</opt>

<opt text="No Dementia (with probability 100%)">
We go right (MMSE > 27.5), left (nWBW) <= 0.787 and left (Age < 84.5)
</opt>
</choice>

</exercise>

<exercise id="3" title="Fourier Transform of the EEG signals">

In mathematics, the **discrete Fourier transform (DFT)** converts a finite sequence of equally-spaced samples of a function into a same-length sequence of equally-spaced samples of the discrete-time Fourier transform (DTFT), which is a complex-valued function of frequency.

<center><img src="https://upload.wikimedia.org/wikipedia/commons/8/8b/Fourier_transform_-_time_shifted_signal.gif" width="400"></center>

Credits: [Wikipedia](https://en.wikipedia.org/wiki/Discrete_Fourier_transform)

**Electroencephalography (EEG)** is an electrophysiological monitoring method to record electrical activity on the scalp that has been shown to represent the macroscopic activity of the surface layer of the brain underneath. It is typically non-invasive, with the electrodes placed along the scalp.

<center><img src="https://upload.wikimedia.org/wikipedia/commons/2/26/Spike-waves.png" width="400"></center>

Credits: [Wikipedia](https://en.wikipedia.org/wiki/Electroencephalography)

In this exercise, we will convert a signal at FpZ channel from the time domain to a frequency domain. Data represents a sample from Cavanagh et al. (2019) study. This sample consists of around 10 seconds of data measurements sample at 500 Hz frequency and measured at 66 channels.

1. Load the pickled dictionary. Path to the file `"exercises/data/eeg_sample.pickle"`. Dictionary has 4 values, `ch_names`: 1D array with channel names; `data`: 2D array with EEG measurements, shape of the array (66, 50001); `srate`: sampling rate (Hz); `times`: time points.
2. Find the index of `Fpz` channel from the channel names.
3. Get the total amount of observations (need for normalization of Fourier coefficients).
4. Pass the signal data from the `Fpz` channel to the `fft` functions. You can use both NumPy and SciPy functions that will produce the same results.
5. Plot the signal in time and frequency domains.

Dictionary `eeg` looks as follows:

```out
{'ch_names': array(['Fp1', 'Fpz', 'Fp2', 'AF3', 'AF4', 'F7', 'F5', 'F3', 'F1', 'Fz',
        'F2', 'F4', 'F6', 'F8', 'FT7', 'FC5', 'FC3', 'FC1', 'FCz', 'FC2',
        'FC4', 'FC6', 'FT8', 'T7', 'C5', 'C3', 'C1', 'Cz', 'C2', 'C4',
        'C6', 'T8', 'M1', 'TP7', 'CP5', 'CP3', 'CP1', 'CPz', 'CP2', 'CP4',
        'CP6', 'TP8', 'M2', 'P7', 'P5', 'P3', 'P1', 'Pz', 'P2', 'P4', 'P6',
        'P8', 'PO7', 'PO5', 'PO3', 'POz', 'PO4', 'PO6', 'PO8', 'CB1', 'O1',
        'Oz', 'O2', 'CB2', 'HEOG', 'VEOG'], dtype='<U4'),
 'data': array([[-1.12866123e-05, -2.65288681e-05, -3.23824174e-06, ...,
          6.55850833e-05,  7.62328967e-05,  7.86320545e-05],
        [-9.48798291e-05, -9.65151415e-05, -8.66185865e-05, ...,
          4.31979958e-05,  5.25620877e-05,  5.46391135e-05],
        [-1.21921364e-04, -1.29915695e-04, -1.07801338e-04, ...,
          2.84674664e-05,  3.79869374e-05,  4.41835641e-05],
        ...,
        [-1.64447760e-05, -3.41811068e-05, -3.15895534e-05, ...,
         -7.30873812e-06, -2.43853666e-05, -2.39186260e-05],
        [ 3.65203953e-05,  3.22641733e-05,  3.86147172e-05, ...,
         -1.63223759e-04, -1.51976764e-04, -1.50407239e-04],
        [-8.10325504e-04, -8.49075174e-04, -8.20144940e-04, ...,
         -2.83902613e-04, -2.62110763e-04, -2.61275838e-04]]),
 'srate': 500,
 'times': array([0.0000e+00, 8.0000e-03, 1.6000e-02, ..., 9.9976e+01, 9.9984e+01,
        9.9992e+01])}
```

Position of FpZ channel on a skull:

<center><img src="imgs/1020system.png" width="400"></center>

Cavanagh, J. F., Bismark, A. W., Frank, M. J., & Allen, J. J. B. (2019). Multiple Dissociations Between Comorbid Depression and Anxiety on Reward and Punishment Processing: Evidence From Computationally Informed EEG. *Computational Psychiatry, 3*, 1–17. DOI: http://doi.org/10.1162/CPSY_a_00024

<codeblock id="07_03">

* remember that pickle files are binary;
* [`np.where()`](https://numpy.org/doc/stable/reference/generated/numpy.where.html) functions takes a condition as an argument;
* select only data from FpZ channel by selecting the needed index from the first dimension of `data` array;

</codeblock>

This was obviously a very sloppy example and there are lots and lots more what you could do with signal data. If you are interested in EEG analysis, I highly recommend [**Complete neural signal processing and analysis: Zero to hero**](https://www.udemy.com/course/solved-challenges-ants/) course at Udemy by Mike X Cohen.

You can also check my blog post on working with this data using [MNE](https://mne.tools/stable/index.html) Python package: [Blog Post: EEG Data Analysis](https://defme.xyz/post/eeg-preprocessing-erp/).

</exercise>

<exercise id="4" title="Simulating the Reinforcement Learning agent">

Reinforcement Learning (RL) is a relatively new subfield of Machine Learning, but it has already provided huge help in computational neuroscience. RL models have been widely used in modeling humans' and animals' behavior and helped to reveal neuronal correlates of decision making.

<center><img src="imgs/reinforcement_learning.jpg" width="500"></center>

Credits: Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction (Adaptive Computation and Machine Learning series)* (second edition). A Bradford Book.

The basic idea of RL is that the *agent* interacts with the *environment* by making the *actions*. Each action results in the outcome *reward* and brings the agent to a new *state*. This is a continuous loop and throughout this interaction, agent learns what actions lead to the highest reward by updating his beliefs about the action-state pairs.

Imagine three slot machines, where each machine has a unique and unknown (to the agent) probability of reward (a.k.a. **Three-armed bandit task**).

<center><img src="https://i.ibb.co/L67QBBz/slotmachine.gif" width="200"><img src="https://i.ibb.co/L67QBBz/slotmachine.gif" width="200"><img src="https://i.ibb.co/L67QBBz/slotmachine.gif" width="200"></center>

Your task is to create the agent, who has to learn which option is more rewarding and maximize the total reward within the limited number of trials. For this, you are going to use the **Q-learning model**, which is most commonly used for decision-making modeling. There are several modifications of this model with different parameters, but in a simple form algorithm can be represented like this:

<img src="imgs/q_model.png" width="500">

* α is a *learning rate*, which lies in a range [0, 1] and controls the speed of updating the value function *Q*. The lower the value, the slower the learning process.
* β is an *inverse temperature*, with the lower non-inclusive bound 0. Controls the behavior of the agent - the lower the value, the more explorative the agent.
* *Q(a)* is a value function or expected reward of an action *a*.
* The softmax function transforms the value function values to probabilities of making an action. It does that by computing the exponential of each value divided by the sum of the exponentials of all the values, scaled by the inverse temperature. In Python it can be calculated using [`softmax()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.softmax.html) function from `scipy.special` module.

<codeblock id="07_04">

* remember that at each trial you are working only with the slice of value function;

</codeblock>

What statement is **true**?

<choice id="2">
<opt text="Total reward for the agent is around 100 (a.u.)" >
Look at the cumulative reward plot. Agent has ended up with reward of ~60.
</opt>

<opt text="Around 3/4 of agent's choices were suboptimal" >
Check how many time agent has chosen each arm on the bar chart. Option #3 (optimal choice) was selected around 55 times out of 100, which means that around 45/100 choices were suboptimal. Even though suboptimal choices don't guarantee the highest total reward, they are essential for learning.
</opt>

<opt text="Agent had the highest expectation for the 3rd arm until the 80th trial, then it was switching between options #2 and #3" correct="true">
Look at the value function plot. At trial ~80 agent didn't receive the expected reward, that's why the value function decreased and then agent was exploring between option #2 and #3.
</opt>
</choice>

Can you improve agent's performance by changing α and β parameters?

For more in-depth overview of RL check out these video series [Reinforcement Learning Course | DeepMind & UCL](https://www.youtube.com/playlist?list=PLqYmG7hTraZBKeNJ-JE_eyJHZ7XgBoAyb).

</exercise>
