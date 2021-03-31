---
title: 'Chapter 7: Case Studies'
description:
  " "
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

* everything you need is in the task;

</codeblock>

</exercise>
