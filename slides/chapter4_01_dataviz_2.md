---
type: slides
---

# What can plots tell us, part 2

Notes: # Outline

* pie chart
* scatter plot
* bubble chart
* boxplot
* heatmap

---

# Pie chart

<center><img src="data_viz/piechart_demo.png" width="500"></img></center>

Notes: A **pie chart** (or a **circle chart**) is a circular statistical graphic, which is divided into slices to illustrate numerical proportion. In a pie chart, the arc length of each slice (and consequently its central angle and area), is proportional to the quantity it represents. While it is named for its resemblance to a pie that has been sliced, there are variations on the way it can be presented.

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Pie_chart)*

Simply saying pie chart shows the normalized proportion of a categorical variable.

Despite the fact that pie charts are very widely used in the mass media, they are often criticized in the "data world". It may be difficult to compare different sections of a given pie chart or to compare data across different pie charts. Pie charts can be replaced in most cases by other plots such as the bar chart, box plot, dot plot, etc.

---

# Example of a pie chart

<center><img src="data_viz/pie_chart_example.jpg" width="450"></img></center>

*Callard et al., 2013*

Notes: Pie chart illustrating the different categories that form the focus of mind wandering research papers over the last decade. The categories were identified by one author (Jonathan Smallwood) and were derived from papers’ keywords.

As you can see, it may be hard to say which category of research papers has the greater value or how big is the difference, for example between "Consciousness" and "Performance" categories.

---

# Scatter plot

<center><img src="data_viz/scatter_plot_demo.png" width="600"></img></center>

Notes: A **scatter plot** (also called a **scatterplot**, **scatter graph**, **scatter chart**, **scattergram**, or **scatter diagram**) is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data. If the points are coded (color/shape/size), one additional variable can be displayed. The data are displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Scatter_plot)*

* x axis - numerical variable
* y axis - numerical variable
* extra numerical variable can be added as a **size** of a point.
* extra categorical variable can be added as a **color/shape** of a point.

---

# Bubble chart (with different size)

<center><img src="data_viz/bubble_chart_size_demo.png" width="600"></img></center>

Notes: A bubble chart is a type of chart that displays three dimensions of data. Each entity with its triplet of associated data is plotted as a disk that expresses two of the values through the disk's xy location and the third through its size. Bubble charts can facilitate the understanding of social, economical, medical, and other scientific relationships.

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Bubble_chart)*

In this case, we added a new **numerical** variable (that is different from X and Y axis variables). The size and the color of the point are dependent on the value of this new variable, so now we can analyze the relationship among several variables at once.

---

# Bubble chart (with different shapes)

<center><img src="data_viz/bubble_chart_shape_demo.png" width="600"></img></center>

Notes: In this case we have added a new **categorical** variable and now the shape of each point is dependent on its value. We could also use colors in this case.

---

# Example of a scatter plot

<center><img src="data_viz/scatter_plot_example.jpg" width="500"></img></center>

*Charpentier et al., 2016*

Notes:  Relation between individual choice behavior and weight difference in feelings associated with losses and gains. The left column shows correlations between loss aversion and the loss-gain weight difference for expected feelings (top) and experienced feelings (bottom). The right column shows correlations between the propensity to gamble and loss-gain weight difference for expected feelings (top) and experienced feelings (bottom). Best-fitting regression lines are shown for each set of data. Asterisks indicate that linear correlations were significant (p < .05). These correlations indicate that the greater weight a participant put on feelings associated with a loss relative to a gain when making a decision, the more loss averse (and less likely to gamble) they were.

---

# Example of a bubble chart (with different colors)

<center><img src="data_viz/bubble_plot_example.jpg" width="650"></img></center>

*Farinelli et al., 2013*

Notes: Scatter plot showing the correlation between ANPS-SEEKING and HADS-Depression scores of control (black circles) and stroke (empty circles) groups. Corresponding linear trends are also shown with the relevant regression equations.

* ANPS: Affective Neuroscience Personality Scales.
* HADS: Hospital Anxiety and Depression Scale.

---

# Example of a bubble chart (with different size)

<center><img src="data_viz/bubble_plot_example2.jpg" width="650"></img></center>

*Nivard et al., 2016*

Notes: Bubble plot showing the effect of age on the association between schizophrenia polygenic risk score (PRS) and childhood psychopathology, split per disorder. Circles indicate the observed effect sizes in the univariate regression analyses (ALSPAC in blue, NTR in red). The size of the circles is proportional to the inverse of the variance, and thus larger circles reflect more accurate estimates. The solid line reflects the meta-regression fitted effect size and the dashed lines indicate the upper and lower 95% confidence interval a round the meta-regression line.

---

# Boxplot

<center><img src="data_viz/boxplot_demo.png" width="400"></img></center>

Notes: In descriptive statistics, a **box plot** or **boxplot** is a method for graphically depicting groups of numerical data through their quartiles. Box plots may also have lines extending from the boxes (whiskers) indicating variability outside the upper and lower quartiles, hence the terms **box-and-whisker plot** and **box-and-whisker diagram**. Outliers may be plotted as individual points.

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Box_plot)*

* For the **vertical** boxplot:
    * x axis - categorical (can be either just one or multiple groups)
    * y axis - numerical
* For the **horizontal** boxplot:
    * x axis - numerical
    * y axis - categorical

---

# How to read the boxplot

<center><img src="data_viz/boxplot_expl.png" width="600"></img></center>

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Box_plot)*

Notes: This image perfectly illustrates how to read the boxplot. Lower edge of the "box" is the first quartile *Q1*, meaning that *P(X≤Q1)=0.25*. THe upper edge of the "box" is the third quartile *Q2* (*P(X≥Q3)=0.75*). So "box" holds 50% of the data. The bold line is the **median**, or *Q2*. The difference *Q3-Q1* is called Interquartile Range (*IQR*).

If some observations are not in the range [*Q1 - 1.5IQR; Q3 + 1.5IQR*] they will be plotted as dots and can be considered as **outliers**.

The average (mean) value can be also plotted as a dot.

Further reading:

* [Quartile](https://en.wikipedia.org/wiki/Quartile)
* [Outlier](https://en.wikipedia.org/wiki/Outlier)
---

# Example of a boxplot (1)

<center><img src="data_viz/boxplot_example.jpg" width="650"></img></center>

*Casey et al., 2018*

Notes: Reaction times are presented as function go and stop trials.

* SSRT: stop signal reaction time;
* SSD: stop signal delay.

---

# Example of a boxplot (2)

<center><img src="data_viz/boxplot_example2.jpg" width="550"></img></center>

*Meghdadi et al., 2021*

Notes: P200 amplitude at channel C3 for 4 groups.

* HC: healthy control participants.

This is a slight modification of a boxplot and called **Notched boxplot**. The idea here stays the same, but we can also show the 95% confidence interval for the median by the concave region (the "notch").

Further reading:

* [Notched Box Plots, Davids Statistics aticle](https://sites.google.com/site/davidsstatistics/home/notched-box-plots)
* [StatQuest: Confidence Intervals, YouTube Video](https://www.youtube.com/watch?v=TqOeMYtOc1w)

---

# Heatmap

<center><img src="data_viz/heatmap_demo.png" width="600"></img></center>

Notes: A **heat map** (or **heatmap**) is a data visualization technique that shows magnitude of a phenomenon as color in two dimensions. The variation in color may be by hue or intensity, giving obvious visual cues to the reader about how the phenomenon is clustered or varies over space.

* x axis - categorical variable
* y axis - categorical variable
* z axis - numerical variable (z is the intersection value between x and y axis)

---

# Example of a heatmap (1)

<center><img src="data_viz/heatmap_example.png" width="500"></img></center>

*Schiro et al., 2011*

Notes: Heat map of gene activation in wild-type and mutant Smad3-expressing C2C12 cells. Expression levels are shown as a percentage of wild-type expression after averaging duplicates. Genes and cells are ordered according to average-linkage hierarchical clustering, as implemented in the heatmap.

This funny looking lines outside the heatmap represent the hierarchical clustering results.

Further reading:

* [StatQuest: Hierarchical Clustering, YouTube Video](https://www.youtube.com/watch?v=7xHsRkOdVwo)

---

# Example of a heatmap (2)

<center><img src="data_viz/heatmap_example2.jpg" width="800"></img></center>

*Tobias et al., 2015*

Notes: Unique temporal contributions of vmPFC to EEG signal. vmPFC cluster (**A**) revealed a temporally elongated activity (B) becoming active at ∼250 ms after feedback (shaded area depicts cluster-corrected significance) and uniquely processing information until ∼400 ms after feedback with a midcentral topography (**C**; red indicates electrodes Fz and FCz used for time plot **B**). **D**, Source estimation localized center of topography into vmPFC again (peak at MNI: x = −8, y = 40, z = −14). E, Time-frequency decomposition revealed that vmPFC mainly operates in the alpha band, from 8 to 12 Hz (thick black line; p < 0.05 using cluster permutation test). The colors indicate the effect of single-trial fMRI responses on the EEG power rather than pure EEG power signals.

---

# Excited to create your first plot?
