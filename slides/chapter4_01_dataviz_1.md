---
type: slides
---

# What can plots tell us, part 1

Notes: # Outline

* line plot
* area chart
* stacked area chart
* bar chart
* grouped bar chart
* (normalized) stacked bar chart
* error bars
* line chart vs bar chart

---

# Definition of "Data Visualization"

<q>Data visualization is the graphic representation of data. It involves producing images that communicate relationships among the represented data to viewers of the images. This communication is achieved through the use of a systematic mapping between graphic marks and data values in the creation of the visualization. This mapping establishes how data values will be represented visually, determining how and to what extent a property of a graphic mark, such as size or color, will change to reflect change in the value of a datum.</q>

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Data_visualization)*

Notes: Simply saying, data visualization is the set of techniques to create a graphical representation of raw data. I personally believe that a lot of data-/neuroscientists don't really appreciate the power of a simple plot. Making plots of the data can help you to find hidden patterns and insights before applying any fancy machine learning stuff.

---

# Line plot

<center><img src="data_viz/line_plot_demo.png" width="600"></img></center>

Notes: A **line chart** or **line plot** or **line graph** or **curve chart** is a type of chart which displays information as a series of data points called 'markers' connected by straight line segments. It is a basic type of chart common in many fields. It is similar to a scatter plot except that the measurement points are ordered (typically by their x-axis value) and joined with straight line segments.

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Line_chart)*

* x axis - time series
* y axis - numerical
* categorical variable can be introduced by adding more lines

It is important to note, that it doesn't make a lot of sense to use a line plot when x axis variable is not time-relevant. We will see examples of "bad" usage in a few slides.

---

# Example of a line plot

<center><img src="data_viz/line_chart_EEG.jpg" width="700"></img></center>

*Berthelsen et al., 2020*

Notes: A perfect example of line charts in a neuroscience world would be EEG data plots. Each line represents a different combination of stimuli, so in this case, you can compare three variables at once - how does the **potential changes** over **time** in the FCz electrode for a given **stimuli**?

There is also a topographical plot of brain activity on the right, but we will come back to it later.

---

# Area chart

<center><img src="data_viz/area_plot_demo.png" width="600"></img></center>

Notes: An **area chart** or **area graph** displays graphically quantitative data. It is based on the line chart. The area between axis and line is commonly emphasized with colors, textures, and hatchings. Commonly one compares two or more quantities with an area chart.

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Area_chart)*

* x axis - time series
* y axis - numerical
* categorical variable can be introduced by adding more lines

As you can see, by shading the area under the curve nothing exciting happens. The plot might look a bit "prettier", but it doesn't change its information and/or function. However, there is a special case of an area chart that we will introduce in the next slide.

---

# Stacked area chart

<center><img src="data_viz/stacked_area_plot_demo.png" width="600"></img></center>

Notes: As you could see, the previous example was not that different from the regular line plot. However, there is a modification of an area chart called **stacked area chart** that is way more useful. It is used to show the difference when two or more labels are included in the plot. When multiple attributes are included, the first attribute is plotted as a line with color fill followed by the second attribute, and so on.

It's important to understand that for the plot on the left total value of `Y` is 5 when `X` is 1.0, while the value for the blue category is around 1, for the yellow category is around 2 (**not 3**) and for the green category is around 2 (**not 5**). The values are **stacked** on top of each other.

In this case, we not only analyze the overall trend of `Y` over `X`, but also how the trend was changing across different categories/labels.

However, you should always check the legend/description of the plot to see whether the area chart is stacked or not.

---

# Example of a stacked area chart

<center><img src="data_viz/stacked_area_plot_example.jpg" width="800"></img></center>

*Bertolero et al., 2020*

Notes: This is a good example of stacked area chart usage, which shows the race of first and last authors of the papers published in neuroscience journals.

* **a**. The sum of probabilities of distinct racial/ethnic categories of the first and last authors of papers published in the top five neuroscience journals studied from 1995 to 2019.
* **b**. The percentage of the total author pool that is comprised of authors in the four racial and ethnic categories studied.

The data is the same for both plots, just a different way of representing it. On the left plot, we see the actual values of each author's race by year. On the right plot, we see the probability distribution of the races.  

---

# Bar chart

<center><img src="data_viz/bar_plot_h_demo.png" width="400"></img><img src="data_viz/bar_plot_v_demo.png" width="380"></img></center>

Notes: A **bar chart** or **bar graph** is a chart or graph that presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent. The bars can be plotted vertically or horizontally. A vertical bar chart is sometimes called a column chart.

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Bar_chart)*

* For the **horizontal** bar chart:
    * x axis - numerical variable
    * y axis - categorical variable
* For the **vertical** bar chart:
    * x axis - categorical variable
    * y axis - numerical variable
* For side-by-side comparison among different categorical variables you can use **grouped bar chart**.
* If you are interested in a proportion of categorical variable for each value on X axis (for vertical bar chart) you can use **stacked bar chart** (or **normalized stacked bar chart**).

---

# Grouped bar chart

<center><img src="data_viz/grouped_bar_plot_demo.png" width="600"></img></center>

Notes: In a **grouped bar chart**, for each categorical group, there are two or more bars. These bars are color-coded to represent a particular grouping. For example, a business owner with two stores might make a grouped bar chart with different colored bars to represent each store: the horizontal axis would show the months of the year and the vertical axis would show the revenue.

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Bar_chart)*

It is useful for side-by-side comparison among categories.

---

# Stacked bar chart

<center><img src="data_viz/stacked_bar_plot_demo.png" width="600"></img></center>

Notes: The stacked bar chart stacks bars that represent different groups on top of each other. The height of the resulting bar shows the combined result of the groups. However, stacked bar charts are not suited to data sets where some groups have negative values. In such cases, grouped bar charts are preferable.

Grouped bar graphs usually present the information in the same order in each grouping. Stacked bar graphs present the information in the same sequence on each bar.

*Credits: [Wikipedia](https://en.wikipedia.org/wiki/Bar_chart)*

The idea is similar to a stacked area chart. For each x value (or y if we use the horizontal bar chart) we stack the label's values on top of each other.

---

# Example of a bar plot

<center><img src="data_viz/bar_plot_example.png" width="450"></img></center>

*van Atteveldt et al., 2014*

Notes: Plot represents the average accuracy values for the different topics.

There is a choice to sort bars by the x axis (for example, alphabetically), or by the y axis values (for example, in descending order as shown in this example).

---

# Example of a grouped bar chart

<center><img src="data_viz/grouped_bar_chart_example.jpg" width="700"></img></center>

*Berthelsen et al., 2020*


Notes: Plots show average response time (left) and response accuracy (right) by groups (error bars represent standard deviations).

---

# Example of a stacked bar plot

<center><img src="data_viz/stacked_bar_plot_example2.jpg" width="650"></img></center>

*O'Connell et al., 2011*

Notes: Stacked bar chart of frequency of articles published in the media and specialized reviews per year.

---

# Example of a normalized stacked bar plot

<center><img src="data_viz/stacked_bar_plot_example.jpg" width="600"></img></center>

*Chataway et al., 2020*

Notes: Normalized stacked bar chart for change in Expanded Disability Status Scale (EDSS) score between different groups.

---

# Bar chart vs line chart

<center><img src="data_viz/bar_vs_line.png" width="650"></img></center>
<center><img src="data_viz/bar_vs_line2.png" width="650"></img></center>

Notes: There is one trick. We can transform each line plot to the bar plot, for example, transform plot **A** to plot **B**. All the information is saved, but just in a bit different way of representing. And can also switch back from plot **B** to plot **A**.

However, not every bar chart can be reasonably converted to a line chart. Plot **C** has a categorical x axis variable that is not really well suited for the line chart. Most of the time we read line charts from left to right, looking at the ups and downs in a trend. By we don't have an actual trend here and if we changed the order of the x axis labels the line would look completely different.

Another point is that we assume that we know (or can predict) the values at each point on the line even if it has no observed x value. For example, for the plot **A** we can assume that the value between March and April (~15 of March) was around 150. But what would be the actual meaning of the average between group B and group C on the plot **D**?

---

# Error bars

<center><img src="data_viz/dynamite.png" width="600"></img></center>

Credits: [Rapid7](https://blog.rapid7.com/2015/01/13/dynamite-plots-logs-the-joy-in-knowing/)

Notes: You might have noticed that sometimes there could be some extra line on top of the bars. This is called **error bars**. They can represent multiple metrics:

1. Standard error of a mean
2. Standard deviation of a sample
3. Confidence interval for the mean

There is no way to guess what exactly error bars represent at each plot, so you always have to check the legend for the clarification.

Further reading:

* [StatQuest: Confidence Intervals, YouTube Video](https://www.youtube.com/watch?v=TqOeMYtOc1w)
* [StatQuickie: Standard Deviation vs Standard Error, YouTube Video](https://www.youtube.com/watch?v=A82brFpdr9g)
* [Bozeman Science. Standard Error, YouTube Video](https://www.youtube.com/watch?v=BwYj69LAQOI)

---

# Example of a "bad" line chart

<center><img src="data_viz/bad_bar_chart.jpg" width="700"></img></center>

*Leung et al., 2021*

Notes: The average Evoked Response Potential (ERP) amplitudes in the parietal region for different conditions among controls and Schizotypy groups.

Disclaimer: My opinion of the "badness" here can be subjective, but I believe that grouped bar plot would fit much better here.

---

# This is it for now! 📊 📈
