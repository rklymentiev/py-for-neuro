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

**Decision tree learning** is one of the predictive modelling approaches used in statistics, data mining and machine learning. It uses a decision tree (as a predictive model) to go from observations about an item (represented in the branches) to conclusions about the item's target value (represented in the leaves). Tree models where the target variable can take a discrete set of values are called classification trees; in these tree structures, leaves represent class labels and branches represent conjunctions of features that lead to those class labels. Decision trees where the target variable can take continuous values (typically real numbers) are called regression trees. Decision trees are among the most popular machine learning algorithms given their intelligibility and simplicity.

Credits: [Wikipedia](https://en.wikipedia.org/wiki/Decision_tree_learning)

<center><img src="https://defme.xyz/post/how-do-cart-models-work/trees.jpg" width="500"></center>

Classification and regression trees (CART for short) models are not the first-choice models when it comes to **prediction** because they trend to overfit the data (in other words they can predict quite good on the training data, but much worse on the test data), but they are really good in **explaining** the data structure. If you are interested in the math behind the model, check out the links below. However, you don't need to know much to complete the exercise.

To build a classification tree we are going to use a [`tree`](https://scikit-learn.org/stable/modules/tree.html) module from the [scikit-learn](https://scikit-learn.org/stable/index.html) package (which is the most popular library for machine learning in Python).

### Exercise. What features can be associated with the dementia rating?

1. Read in the data with dementia cases (path to file: `"exercises/data/oasis_cross-sectional.csv"`);
2. Drop the redundant columns: `"ID"` (ID label shouldn't be a predictor of Alzheimer's, should it?), `"Hand"` (all observations are right-handed) and `"Delay"` (most of the values are missing) and save it in the new data frame `model_data` (even though the columns might be meaningless, it's a good idea to keep the raw data);
3. Drop the rows with missing values. Note, this is a sloppy solution for a missing data problem. There are several methods on how you can artificially replace the missing values and some new algorithms can handle missing data during modelling, however this is beyond this exercise;
4. We are going to build a binary classification tree: `0` for no dementia (CDR is 0) and `1` for dementia status (CDR is 0.5, 1 or 2). Create a new binary column `dementia` and drop the `"CDR"` column;
5. scikit-learn models don't allow string columns (unlike models in R), that's why we often have to perform some sort of feature engineering. In our case we just need to convert gender column `M/F` to numerical binary - `1` if female, `0` otherwise;
6. Split the `model_data` into data frame with independent variables (all features, `X`) and a series with dependent variable (binary, `y`) for later use;
7. Build a model using entropy for split criteria and set maximum depth of the tree to 3;
8. Fit the data to the model and make a plot.

Further readings:
* Blog post: [How do CART models work](https://defme.xyz/post/how-do-cart-models-work/)
* YouTube video: [StatQuest: Decision Trees](https://youtu.be/7VeUPuFGJHk)

<codeblock id="07_02">

* don't forget about `inplace=True` in pandas methods applied on data frames;

</codeblock>

You can read this plot from top to bottom. The very first node is the initial data (`X` and `y`). 61.6% of the observations have no dementia (`dementia` = 0). At this node model splits the data according to the Mini-Mental State Examination score (`MMSE`). If it's less than 27.5 we go left, if it's greater we go right (left arrow is `True`, right arrow is `False` for the `MMSE <= 27.5` condition). At each node you can see the entropy in the `y` variable, fraction of observations from total and ratio of two classes. Note that tree could be even more complicated, but we reduced it to 3 splits (or levels).

What is the expected outcome for the 50 year old subject with Mini-Mental State Examination score (`MMSE`) 28, normalized whole brain volume (`nWBW`) 0.65?

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


Simply speaking, Fourier transform is used to convert a signal from the time domain to a frequency domain.

<codeblock id="07_03">


</codeblock>

</exercise>
