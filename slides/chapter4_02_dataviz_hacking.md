---
type: slides
---

# Data Viz Hacking

Notes: Even though we all (or at least most of us) understand how plots work and how to make them, we are still surrounded by false graphs that can alter our perception. I feel like this happens quite often in media area, especially when it comes to politics, but that could be just me and the way I notice it.

In this representation you will see some plots, that are not really that innocent. They are not brain or life science related, but still I think they can play as a good example of how to be critical when looking at the plots.

All the plots were found on reddit [r/dataisugly](https://www.reddit.com/r/dataisugly/).

---

# Same values, different heights?

<center><img src="data_viz/hack1.png" width="600"></img></center>

Notes: Given all of the things said about line chart, you would probably assume that when values have the same (or nearly the same) magnitude, they should be plotted on the same height of y axis. Well, this is not the case for this graph when we look at the last 4 observations. What should we trust, the dot height or the numerical value? Who knows.

Another note, some dates are missing on x axis. It may look like from 13 and 18 of March there was a huge increase in whatever-value-that-is, but if we plotted all the missing dates, it could have a different view.

---

# Who cares about the scale?

<center><img src="data_viz/hack2.png" width="700"></img></center>

Notes: Again, missing dates here. There is nothing wrong to drop some dates so they don't overload the graph. But if we do so, we have to keep the values at the same scale (distance between two days should be twice as small as distance between 4 days).

Scale of the y axis is also disrupted. It could be a logarithmic scale, but doesn't look like it.

---

# Once again, forget about the scale

<center><img src="data_viz/hack5.jpg" width="600"></img></center>

Notes: Do people from Philippines can reach only to the knees of people from Netherlands?

Yes, if we take a quick look at this graph.

No, if we take a look at the values of y axis.

---

# 51% is less than one half

<center><img src="data_viz/hack3.png" width="700"></img></center>

Notes: Something went wrong with the pie chart proportions. Visually it looks like less than half of Americans say they've tried marijuana, but it's not the case if we look at the actual values.

---

#  \*visible confusion\*

<center><img src="data_viz/hack4.png" width="700"></img></center>

Notes: It's hard to judge this graph since it a bit unclear what exactly went wrong - numerical labels of the bars or bars' height. Are people concerned about Zika virus? We still don't know.

---

# Is the difference really that great?

<center><img src="data_viz/hack6.png" width="500"></img></center>

Notes: By a quick glance at the plot it may look like Yang has a much large proportions of voters. But if we look at the actual values, it's not the case. Scale \*is\* important.

---

# 47.8 > 51.3?

<center><img src="data_viz/hack7.jpg" width="600"></img></center>

Notes: Nice example on how to make us feel that Biden had more votes than Trump, when in fact it was not true.

---

#  Don't let them fool you!
