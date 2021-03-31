---
title: 'Chapter 4: Data Visualization'
description:
  'Making plots from the raw data is powerful and somewhat underestimated tool that could give you a better understanding of what is going on in your data and some interesting insights. In this chapter we will look at the main plot types and how to create them in Python using Matplotlib and Seaborn packages.'
prev: /chapter3
next: /chapter5
type: chapter
id: 4
---

<exercise id="1" title="What can plots tell us, part 1" type="slides">

<slides source="chapter4_01_dataviz_1">
</slides>

</exercise>

<exercise id="2" title="What can plots tell us, part 2" type="slides">

<slides source="chapter4_01_dataviz_2">
</slides>

</exercise>

<exercise id="3" title="Check yourself" >

**Question 1**. Which combination of County and Year has the greatest value?

<center><img src="data_viz/heat_map_test.png" width="500"></center>

<choice id="1">

<opt text="(STATEN ISLAND, 2010)">
Check the colorbar on the right.
</opt>

<opt text="(BROOKLYN, 2017)">
Is it the darkest cell though?
</opt>

<opt text="(BROOKLYN, 2016)" correct="true">
The darker the color, the greater the value.
</opt>

<opt text="It cannot be defined from this chart">
Why not? Check the colorbar on the right.
</opt>
</choice>

**Question 2**. What are the guidelines for creating clear and human readable chart?

<choice id="2">

<opt text="Describe chart with titles, labels and annotations" correct="true">
Help people easily understand what you tried to show on the plot.
</opt>

<opt text="Include as many different colors as you can">
This would be true, if you want to create an eye hell.
</opt>
</choice>

**Question 3**. [...] are often being criticized since it can be difficult to compare different sections of a given chart, or to compare data across different charts.

<choice id="3">
<opt text="Bar charts">
In fact bar plots are very good for comparison multiple groups at once.
</opt>

<opt text="Line plots">
The range of the y axis makes it easy to compare different groups/labels.
</opt>

<opt text="Pie charts" correct="true">
Check out this plot: https://en.wikipedia.org/wiki/Pie_chart#/media/File:Badpie.png
</opt>
</choice>

**Question 4**. Which months have possible outlier values?

<center><img src="data_viz/boxplot_outliers.png" width="500"></center>

<choice id="4">
<opt text="All of them">
Do all the boxplots have values outside the [Q1 - 1.5IQR; Q3 + 1.5IQR] range?
</opt>

<opt text="None of them">
Look closer.
</opt>

<opt text="6 & 7" correct="true">
There are one possible outlier for the 6th month and 2 possible outliers for the 7th month.
</opt>

<opt text="5 & 8 & 9">
They might have some "extreme" values for sure, that we cannot see them from this plot.
</opt>
</choice>

</exercise>

<exercise id="4" title="Data Viz Hacking" type="slides">

<slides source="chapter4_02_dataviz_hacking">
</slides>

</exercise>

<exercise id="5" title="What went wrong here?">

**Question 1**. Is this plot done correctly?

<center><img src="data_viz/pie_chart_quiz.jpg" width="500"></center>

<choice id="1">
<opt text="Yes, there is nothing wrong with this plot">
Compare the numerical values and the actual circle proportion.
</opt>

<opt text="No, proportion and numerical values do not agree" correct="true">
42& looks more like 33%.
</opt>

<opt text="No, total sum is not 100%">
Well, that's true, but that could be caused by a rounding error and it's not the biggest problem of the plot.
</opt>
</choice>

**Question 2**. What about this one?

<center><img src="data_viz/bad_bar_quiz.jpg" width="500"></center>

<choice id="2">
<opt text="Yes, there is nothing wrong with this plot">
Check the scale of the x axis.
</opt>

<opt text="No, this should have been a vertical bar plot" >
There is nothing wrong to use a horizontal bar chart in this case.
</opt>

<opt text="Scale is corrupted" correct="true">
Makati City and Quezon City have a huge numerical difference, but small "visual difference".
</opt>
</choice>

</exercise>

<exercise id="6" title="How to create a meaningful plot">

### Rule of thumb:

1. Think about what answer should you visualization answer.
2. Choose the right chart for your data.
3. Make it clear and human readable.
4. Don’t put to much information on one chart.
5. Describe it with titles, labels and annotations.
6. Don’t go crazy with colors.

**[Cheat-sheet](http://2.bp.blogspot.com/-6D6p5m-iEsE/W5mMGKBa_xI/AAAAAAAABI4/9zF4sNy7V6QOy__CDFe-kY_xnLVKyijxgCK4BGAYYCw/s1600/98510-728109.jpg)** that can help with choosing the appropriate plot type.


</exercise>

<exercise id="7" title="Packages for data visualization" type="slides">

<slides source="chapter4_03_dataviz_packages">
</slides>

</exercise>

<exercise id="8" title="Make your plots">

**Exercise 1. Breast cancer diagnostic data set**

Sample for the data set:

<center><img src="breast_cancer.png"></center>

1. Load the data with breast cancer observations (path to the file `"exercises/data/breast_cancer.csv"`);
2. Make a **scatter plot** of `radius_mean` on the `x` axis against `texture_mean` on the `y` axis along with the **regression line**. You can do this in one line of code using `sns.regplot()` function. Specify standard deviation as an error (`x_ci="sd"`);
3. Add vertical line with average radius and horizontal line with average texture. Set both if them to be dashed, black and of width of 1.

<codeblock id="04_01">

* you can use a `.mean()` method to get the average value from pandas Series;

</codeblock>

What is the approximate correlation between `texture_mean` and `radius_mean`?

<choice id="1">
<opt text="Around -0.4">
What happens to texture_mean when radius_mean increases?
</opt>

<opt text="Around 0.4" correct="true">
To be more precise, it's 0.32.
</opt>

<opt text="Around 0">
Is there really no relationship between variables?
</opt>
</choice>

**Exercise 2**. It's always a good idea to check for relationship among variables in the data before applying Machine Learning algorithms. One of possible ways to do this is to check the correlation. Looking at the raw numbers of correlation may be not that productive and that's when **heatmap** becomes handy.

1. Load the data with breast cancer observations (path to the file `"exercises/data/breast_cancer.csv"`);
2. Select only columns the average values (with the `"mean"` in the name);
3. Create a correlation matrix and store it to `corr_matrix` variable;
4. Pass the `corr_matrix` into the `sns.heatmap()` function to create a heatmap.

<codeblock id="04_02">

* one of the possible ways to get only columns with `"mean"` in the name is to use `filter()` and `lambda` functions on the list of column names (`df.columns`);
* correlation matrix can be found by `df.corr()` method.

</codeblock>

What combination of variables can lead to problems during the modeling part (has high correlation)?

<choice id="2">
<opt text="texture_mean & smoothness_mean">
Correlation between these two variables is around -0.1.
</opt>

<opt text="texture_mean & perimeter_mean">
Correlation between these two variables is around 0.3.
</opt>

<opt text="area_mean & perimeter_mean" correct="true">
This shouldn't be that surprising. The higher the perimeter, the higher the area.
</opt>
</choice>

</exercise>

<exercise id="9" title="Exploratory Data Analysis">

In statistics, **exploratory data analysis** is an approach to analyzing data sets to summarize their main characteristics, often using statistical graphics and other data visualization methods. A statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task. Exploratory data analysis was promoted by John Tukey to encourage statisticians to explore the data, and possibly formulate hypotheses that could lead to new data collection and experiments.

<center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Data_visualization_process_v1.png/800px-Data_visualization_process_v1.png" width="600"></center>

Credits: [Wikipedia](https://en.wikipedia.org/wiki/Exploratory_data_analysis)

### Exercise 1. Dementia data set

Sample for the data set:

<center><img src="oasis.png"></center>

* Load the data with dementia patients observations (path to the file `"exercises/data/oasis_cross-sectional.csv"`).
* Create 4 grouped bar charts at the same figure (using `plt.subplot()`). Variables to plot:
    * `y` axis: age (`"Age"`), years of education (`"Educ"`), socioeconomic status (`"SES"`), Mini-Mental State Examination score (`"MMSE"`);
    * `x` axis: Clinical Dementia Rating (`"CDR"`)
    * group (`hue` argument) by gender (`"M/F"`)

CDR classification:

* 0 = Normal
* 0.5 = Very Mild Dementia
* 1 = Mild Dementia
* 2 = Moderate Dementia

Additionally create a `summary_stats` DataFrame with count of observations (`"ID"` column) and aggregated values (mean and standard deviation of these four variables).

<codeblock id="04_03">

* recall `plt.subplot(<total rows in a figure>, <total columns in a figure>, <current plot>)`;
* to create a DataFrame with summary statistics you can group by two variables (dementia rating and gender) and get the aggregated values for specific columns.

</codeblock>

What statement is correct:

<choice id="1">
<opt text="There are 2 people in the data set with moderate dementia and both are males">
There are 2 people with moderate dementia, 1 male and 1 female.
</opt>

<opt text="Age the dementia status (CDR) are positively correlated" correct="true">
On average people with more severe dementia are older.
</opt>

<opt text="Healthy controls (no dementia) have more variability for mini-mental state examination score compared to dementia patients.">
Look at the size of error bars.
</opt>
</choice>

### Exercise 2

Seaborn package is really powerful and it allows to create complex plots in a simple way. Let's look at the `sns.relplot()` (relational plot) for an example. By default it creates a scatter plot between two variables with possibility to add additional frouping variables.

1. plot the relationship between estimated total intracranial volume (`"eTIV"`) and normalized whole-brain volume (`nWBV`);
2. split plots to separate columns according to the clinical dementia rating (`"CDR"`) using `col` argument;
3. set the color of each point according to the gender (`"M/F"`) using `hue` argument;
4. set the size of a point according to the atlas scaling factor (`"ASF"`) using `size` column.

<codeblock id="04_04">

* everything you need is in the task;

</codeblock>

What statement is correct:

<choice id="2">
<opt text="On average females have greater total intracranial volume">
Look at the colors and x axis.
</opt>

<opt text="There is a strong positive relationship between eTIV and nWBV among different groups">
It looks like there is no relationship at all.
</opt>

<opt text="On average values of atlas scaling factor increase as the estimated total intracranial volume increases" correct="true">
Look at the size of the point and what's happening when we move along x axis.
</opt>
</choice>

</exercise>
