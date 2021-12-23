---
title: 'Chapter 6: Statistics in Python'
description:
  "We will look at how to perform statistical analysis such as ANOVA or Chi-squared test using mainly scipy.stats module and pingouin package. "
prev: /chapter5
next: /chapter7
type: chapter
id: 6
---

<exercise id="1" title="Disclaimer">

The main goal of this chapter is not "how to perform a statistical analysis", but rather "how to perform a statistical analysis in Python, given that you are familiar with the math". If you are not familiar with some of the topics, you can check the tutorials/videos I include below. If you are familiar with statistics, you may be annoyed with the oversimplification. I skip most of the assumptions checking, data manipulation, etc. since that's not the goal here.

Also, we are not really interested in the study designs and how exactly the observations were collected in given data sets. All the results should not be taken seriously and no generalization should be applied.

Further reading:

* Blog post: [Null Hypothesis Significance Testing, part 1](https://defme.xyz/post/null-hypothesis-significance-testing-part-1/): Inference for a population mean: *t*-tests & ANOVA;
* Blog post: [Null Hypothesis Significance Testing, part 2](https://defme.xyz/post/null-hypothesis-significance-testing-part-2/): Inference for a population proportion: binomial test, Chi-squared test;
* Blog post: [Null Hypothesis Significance Testing, part 3](https://defme.xyz/post/null-hypothesis-significance-testing-part-3/): Power of the Test, Sample Size and Effect Size;
* YouTube channel: [StatQuest with Josh Starmer](https://www.youtube.com/user/joshstarmer) (I can recommend literally every single video);
* Coursera specialization: [Statistics with R by Duke University](https://www.coursera.org/specializations/statistics).

</exercise>

<exercise id="2" title="Packages for statistical analysis">

## SciPy

<center><img src="https://www.fullstackpython.com/img/logos/scipy.png" width="300"></img></center>

There are several Python packages with statistical functions but `stats` module in SciPy package probably is the most commonly used. It consists of functions to work with the variety of continuous/discrete random variables (such as Normal distribution), functions for summary statistics (such as skewness), functions to perform statistical tests (such as Shapiro-Wilk test for normality) and many more possibilities.

[SciPy website](https://www.scipy.org/) || [Documentation](https://docs.scipy.org/doc/scipy/reference/index.html#) || [Stats module documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Pingouin

<center><img src="https://pingouin-stats.org/_images/logo_pingouin.png" width="400"></img></center>

Another quite new but powerful package is Pingouin. It has much more informative output when it comes to statistical tests.

[pingouin website](https://pingouin-stats.org/) || [Documentation](https://pingouin-stats.org/api.html)

</exercise>

<exercise id="3" title="Working with distributions">

As told before, SciPy has built functions to work with distribution of random variables, either discrete or continuous. Distributions represent a separate classes with usefule methods for manipulation. Here is the example for Normal distribution:

### Population distribution

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats # we are loading only the `stats` module


# set population parameters
pop_mean = 100 # mean
pop_std = 15   # standard deviation

# create an array of 300 numbers from 50 to 150
# equally separated from each other
x = np.linspace(start=50, stop=150, num=300)
# find values of probability density function that correspond to the x values
population = stats.norm.pdf(x=x, loc=pop_mean, scale=pop_std)

plt.figure(figsize=(10,5))
sns.lineplot(x=x, y=population) # PDF plot
plt.axvline(
    x=pop_mean, color="red",
    linewidth=1, linestyle="dashed",
    label="mean")
plt.xlabel("X")
plt.title("Population PDF", fontsize=18)
plt.show()
```

<center><img src="stats_pop.png" width="500"></img></center>

What is the value of survival function at point 120? Or in other words, what is the probability that random variable *X* will be greater than 120?

<center><img src="https://latex.codecogs.com/gif.latex?P(X>120)&space;=&space;?" title="P(X>120) = ?" /></center>

```python
prob_x = stats.norm.sf(x=120, loc=pop_mean, scale=pop_std)
print(f"P(X>120) = {prob_x:.2f}")
```
```out
P(X>120) = 0.09
```

### Sample distribution

```python
sample_n = 100
# draw a sample of n values from a population
sample = stats.norm.rvs(loc=pop_mean, scale=pop_std, size=sample_n, random_state=1)

plt.figure(figsize=(10,5))
sns.histplot(sample, bins=15)
plt.xlabel("X")
plt.title("Histogram of sample distribution", fontsize=18)
plt.show()
```

<center><img src="stats_sample.png" width="500"></img></center>

</exercise>

<exercise id="4" title="Distributions practice">

### Exercise 1. Binomial distribution

SSRI (Selective Serotonin Reuptake Inhibitor) is one of the most prescribed classes of antidepressants (for example, Prozac) for patients with major depressive disorder (MDD). However, studies suggest that around 38% of patients have experienced at least one side effect (like sexual dysfunction, sleepiness or weight gain). You have prescribed SSRI antidepressants to 65 new patients.

1. What is the probability that 25 or more will experience at least one side effect?
2. In fact, 20 patients of 65 have experienced side effects. What is the probability of such an event?
3. Plot the probability mass function (PMF) of the random variable *X*, where *X* is the number of patients who can experience at least one side effect.

<codeblock id="06_04">

* survival function (`sf`) shows the probability that random variable *X* is **greater** (not greater or equal) a certain value;
8 probability mass function (`pmf`) shows the probability that random variable *X* equals a certain value;
* sample space consists of all the values from 0 to `n` (65). Or in other words, out of 65 patients 0 can get a side effect, 1 can get a side effect, 2 can get side effect and so on;

</codeblock>

### Exercise 2. *t* distribution

You have performed a learning task on 20 animals and obtained accuracy values. You believe that the animals' performance is below the chance level (50%), so you want to run a *t*-test to check your hypothesis.

* Null distribution: average value of accuracy scores is not different from 0.5, <img src="https://latex.codecogs.com/gif.latex?\bar{x}&space;=&space;\mu_0&space;=&space;0.5" title="\bar{x} = \mu_0 = 0.5" />;
* Alternative distribution:  average value of accuracy scores is below 0.5, <img src="https://latex.codecogs.com/gif.latex?\bar{x}<\mu_0" title="\bar{x}<\mu_0" />;
* Significance level (alpha) is 0.05.

Find (1) *t* score, (2) p-value, (3) *t* critical (the highest value of *t* distribution where you would still be able to reject to null hypothesis) using randomly generated values (in a [0, 1] range).

**Hints:**

<center><img src="https://latex.codecogs.com/gif.latex?t_\text{score}&space;=&space;\frac{\bar{x}&space;-&space;\mu_0}{SE}" title="t_\text{score} = \frac{\bar{x} - \mu_0}{SE}" /></center>
<center><img src="https://latex.codecogs.com/gif.latex?SE&space;=&space;\frac{s}{\sqrt{n}}" title="SE = \frac{s}{\sqrt{n}}" /></center>
<center><img src="https://latex.codecogs.com/gif.latex?\text{p-value}&space;=&space;P(t<t_\text{score})" title="\text{p-value} = P(t<t_\text{score})" /></center>
<center><img src="https://latex.codecogs.com/gif.latex?\alpha&space;=&space;P(t<t_\text{critical})" title="\alpha = P(t<t_\text{critical})" /></center>

<codeblock id="06_05">

* this is one-sided test (looking for an effect in one direction);
* by default `.std()` method in `numpy` returns the standard deviation for the population. To get the sample SD one needs to specify degrees of freedom (`ddof`) to subtract in the denominator;
* *t* distribution has one parameter - degrees of freedom (`df`) which equals `n-1`;
* p-value is the left tail of a distribution in our case, or a value of cumulative distribution function (CDF, *F(x)*) at the value *t* score;
* *F(x) = 1 - S(x)*, where *S(x)* is the survival function (`.sf()`);

</codeblock>

</exercise>

<exercise id="5" title="Significance testing: t-tests">

If you have done everything correct in exercise 2 in part 4, your results should look like this:

```out
t score=-2.36, p-val=0.01
```
<center><img src="stats_t.png" width="500"></img></center>

Now let's perform the *t*-test on the same data but in more convenient way using [`ttest_1samp()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html) function from `scipy.stats` module and [`ttest()`](https://pingouin-stats.org/generated/pingouin.ttest.html) function from `pingouin` package.

<codeblock id="06_06">

* this is a one-sided test and we are interested in a left tail (`"less"`);
* two perform a one-sample test using `ttest()` function pass a null distribution value as a `y` argument;

</codeblock>

What is the effect size (Cohen *d*) of the test?

<choice id="1">
<opt text="Small" >
d=0.2 value is usually referred as a small effect size.
</opt>

<opt text="Medium" correct="true">
d=0.5 value is usually referred as a medium effect size.
</opt>

<opt text="Large">
d=0.8+ values are usually referred as a large effect size.
</opt>
</choice>

To build more intuition about Cohen *d* effect size checkout this visualization: [Interpreting Cohen's d Effect Size](https://rpsychologist.com/cohend/).



</exercise>

<exercise id="6" title="Significance testing: ANOVA">

### Is there difference in the average normalized whole-brain volume (`"nWBW"`) among patients with different clinical dementia rating (`"CDR"`)?

* Null hypothesis: there are no differences between average values of nWBW among groups;
* Alternative hypothesis: there is a difference and at least one pair is significantly different;
* Significance level: alpha = 0.05.

ANOVA is a simple *F* test that measures a ratio:

<center><img src="https://latex.codecogs.com/gif.latex?F&space;=&space;\frac{\text{Explained&space;Variability}}{\text{Unexplained&space;Variability}}" title="F = \frac{\text{Explained Variability}}{\text{Unexplained Variability}}" /></center>

* <img src="https://latex.codecogs.com/gif.latex?df_{\text{total}}&space;=&space;n&space;-&space;1" title="df_{\text{total}} = n - 1" />
* <img src="https://latex.codecogs.com/gif.latex?df_{\text{group}}&space;=&space;k&space;-1" title="df_{\text{group}} = k -1" />
* <img src="https://latex.codecogs.com/gif.latex?df_{\text{error}}&space;=&space;df_{\text{total}}&space;-&space;df_{\text{group}}" title="df_{\text{error}} = df_{\text{total}} - df_{\text{group}}" />
* *n* - total number of observations;
* *k* - number of groups.

Your task:

1. Read in the data with dementia cases (path to file: `"exercises/data/oasis_cross-sectional.csv"`);
2. Make a boxplot with `CDR` levels on `x` axis and `nWBW` on the `y` axis to check the distribution. You will see that there are just two observations with `CDR = 2`. Filter them out from the DataFrame so they don't affect the result.
3. Perform the ANOVA and establish the p-value.

There is a function in `scipy.stats` module [`f_oneway()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html) which performs one-way ANOVA. However, the result is just two objects: test statistic (*F*) and p-value. Alternative to that, there is an [`anova()`](https://pingouin-stats.org/generated/pingouin.anova.html) function (from `pingouin` package) which returns a much more detailed outcome. Include them all to compare the output and make a decision about the test.

<codeblock id="06_02">

* ANOVA function from `scipy` package works in a way that you have to add samples of you groups separately into the function (`f_oneway(sample1, sample2, ..., sampleN)`);
* ANOVA function from `pingouin` package is a bit more sophisticated. You can pass the whole data set as `data` and then specify the column names of your dependent variable and grouping variable(s);
* to filter out observations from the DataFrame you can use the following structure: `df[df["column_name"] <condition>]`;

</codeblock>


What does the result of ANOVA test tell us in context of a problem?

<choice id="1">
<opt text="Grouping observations by dementia rating helps to increase the variance in nWBW" >
p-value was << 0.001, meaning that by grouping we can explain variance in nWBW.
</opt>

<opt text="The average values from all groups are significantly different from each other" >
We don't know that yet. All we know is that at lest one pair is significantly different.
</opt>

<opt text="Grouping observations by dementia rating helps to reduce the variance in nWBW" correct="true">
At lest one pair is different.
</opt>
</choice>

</exercise>

<exercise id="7" title="Significance testing: pairwise t-tests">

Now that we have seen that ANOVA showed a significant result we can perform *t*-tests for each pair of groups to see what groups are actually significantly different. How many combinations of groups will be there?

<choice id="1">
<opt text="2" >
Remember that we have three groups CDR = (0, 0.5, 1).
</opt>

<opt text="3" correct="true">
(CDR=0 vs CDR=1) & (CDR=0 vs CDR=0.5) & (CDR=0.5 vs CDR=0.1).
</opt>

<opt text="6">
Did you count CDR=2 as well?
</opt>
</choice>

1. Read in the data with dementia cases (path to file: `"exercises/data/oasis_cross-sectional.csv"`);
2. Run pairwise comparison. The easy way to do this is to run [`pairwise_ttests()`](https://pingouin-stats.org/generated/pingouin.pairwise_ttests.html) function from `pingouin` package;
3. Set effect size to Cohen d and adjust the p-value using Bonferroni correction;
4. Make a conclusions.

<codeblock id="06_03">

* to filter out observations from the DataFrame you can use the following structure: `df[df["column_name"] <condition>]`;

</codeblock>

Given the significance level alpha = 0.05, what can we can about the groups?

<choice id="2">
<opt text="Only (CDR 0 vs CDR 0.5) & (CDR 0 vs CDR 01) showed statistical difference" >
This could be the case for alpha = 0.01.
</opt>

<opt text="All pairs are significantly different and have effect size above medium" correct="true">
Cohen's d 0.5+ is considered to be above medium effect size.
</opt>

<opt text="None of the groups showed a statistically significant difference">
Are p-values greater than alpha?
</opt>
</choice>

</exercise>

<exercise id="8" title="Significance testing: Chi-squared test">

### Does clinical dementia rating (`CDR`) depend on level of education (`Educ`)?

In order to do this, we can use a [Chi-squared test](https://en.wikipedia.org/wiki/Chi-squared_test).

* Null hypothesis: clinical dementia rating and level of education are **independent** of each other;
* Alternative hypothesis: clinical dementia rating and level of education are **dependent** (clinical dementia rating varies by level of education);
* Significance level: alpha = 0.05.

Test statistic:

<center><img src="https://latex.codecogs.com/gif.latex?\chi^2&space;=&space;\sum_{i=1}^k&space;\frac{(O-E)^2}{E}" title="\chi^2 = \sum_{i=1}^k \frac{(O-E)^2}{E}" /></center>

Degrees of freedom:

<center><img src="https://latex.codecogs.com/gif.latex?\text{df}&space;=&space;(R-1)(C-1)" title="\text{df} = (R-1)(C-1)" /></center>

* *O*: observed data in a “cell”
* *E*: expected data of a “cell”
* *k*: number of “cells”
* *R*: number of rows
* *C*: number of columns

In order to answer this question you have to:

1. Read in the data with dementia cases (path to file: `"exercises/data/oasis_cross-sectional.csv"`);
2. Create a cross table of counts of observations between education level (`"Educ"`) and clinical dementia rating (`"CDR"`). This can be done using [`pd.crosstab()`](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html) function;
3. Pass the resulted cross table into [`stats.chi2_contingency()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html) function. The function returns three values: test statistic, p-value of the test, degrees of freedom and expected frequencies;
4. Find the critical value of Chi-squared for these degrees of freedom and desired significance level;
5. Create values `x` and `y` to plot the null distribution;
6. Make a plot;
7. Fix the `if` statement to make a correct output.

<codeblock id="06_01">

* to find the critical value `threshold` you need to find such value X which has a following property: P(χ²<X) = 1-α or P(χ²>X) = α;

</codeblock>

What does the result of Chi-squared test tell us in the context of a problem?

<choice id="1">
<opt text="Clinical dementia rating varies by the level of education (they are not independent)" correct="true">
We rejected the null hypothesis since p-value was less than alpha.
</opt>

<opt text="Clinical dementia rating doesn't depend on the level of education (they are independent)">
Was the p-value greater than alpha?
</opt>
</choice>

</exercise>

<exercise id="9" title="Confidence intervals for the mean and bootstrapping">

In order to estimate the confidence interval (CI) for a continuous variable you can do it using *t* distribution for example:

<center><img src="https://latex.codecogs.com/gif.latex?\left(&space;\bar{x}&space;-&space;t_{\alpha/2,df}&space;\times&space;\text{SE};&space;\bar{x}&space;&plus;&space;t_{\alpha/2,df}&space;\times&space;\text{SE}&space;\right&space;)" title="\left( \bar{x} - t_{\alpha/2,df} \times \text{SE}; \bar{x} + t_{\alpha/2,df} \times \text{SE} \right )" /></center>

<center><img src="https://latex.codecogs.com/gif.latex?\text{SE}&space;=&space;\frac{s}{\sqrt{n}}" title="\text{SE} = \frac{s}{\sqrt{n}}" /></center>

Where *SE* is a standard error of the mean, alpha is a significance level and *t* is a quantile of a *t* distribution.

Quite often CIs are estimated using **bootstrapping** technique (especially when the sample size is small). Bootstrapping is any test or metric that uses random sampling with replacement (e.g. mimicking the sampling process), and falls under the broader class of resampling methods. Bootstrapping assigns measures of accuracy (bias, variance, confidence intervals, prediction error, etc.) to sample estimates. This technique allows estimation of the sampling distribution of almost any statistic using random sampling methods.

Credits: [Wikipedia](https://en.wikipedia.org/wiki/Bootstrapping_(statistics))

The easiest way to perform a bootstrap CI is with the help of [`compute_bootci()`](https://pingouin-stats.org/generated/pingouin.compute_bootci.html) function from `pingouin` package. The function allows estimating the CI for different statistics (such as Pearson correlation for bivariate data or standard deviation for univariate data) which is specified by `func` argument and returns a numpy array with lower and upper bounds.

Your task:

1. Read in the data with dementia cases (path to file: `"exercises/data/oasis_cross-sectional.csv"`);
2. Calculate a 95% CI for the average values of normalized whole brain volume (`nWBW`) for each level of clinical dementia rating (`CDR`) and save the results in a dictionary in the following way:

```python
{0: {'CI': array([0.7615, 0.777 ]), 'mean': 0.7692},
 0.5: {'CI': array([0.7213, 0.7376]), 'mean': 0.7294},
 1: {'CI': array([0.6952, 0.7177]), 'mean': 0.7062}}
```

Note that dictionary has a nested structure.

<codeblock id="06_07">

* each key of a `nwbv_estimation` dictionary is a `CDR` value (`0`, `0.5` or `1`). We don't include label `2` here since there are only two observations;
* each value of a `nwbv_estimation` dictionary is another dictionary with two keys: `"mean"`, which is a sample mean and `"CI"` with is the output of `compute_bootci()` function and represents lower and upper bounds;
* you need to `.update()` nested dictionary values;

</codeblock>

What statement is **incorrect** about the population mean of normalized whole brain volume for patients without dementia (CDR = 0)?

<choice id="1">
<opt text="Probability that the population mean is in a range [0.7613, 0.7769] is 95%" correct="true">
We are 95% confident, but it doesn't mean that we know the probability of occurrence of population mean in a CI.
</opt>

<opt text="Probability that the population mean is in a range [0.7613, 0.7769] is either 0 or 1" >
That is the correct way of interpretation. We either catch the population mean inside the CI or we didn't.
</opt>

<opt text="If we collect the data for similar samples (with the same size n) and build CI based on each of them, 95% of the CIs will catch the true population mean">
That is the correct way of interpretation.
</opt>
</choice>

Further reading:

* Interactive visualization: [Interpreting Confidence Intervals](https://rpsychologist.com/d3/ci/)
* YouTube video: [StatQuest: Confidence Intervals](https://www.youtube.com/watch?v=TqOeMYtOc1w)
* Jung, K., Lee, J., Gupta, V., & Cho, G. (2019). Comparison of Bootstrap Confidence Interval Methods for GSCA Using a Monte Carlo Simulation. *Frontiers in psychology*, 10, 2215. https://doi.org/10.3389/fpsyg.2019.02215

</exercise>

<exercise id="10" title="Outliers in the data">

<center><img src="outliers.png"></center>

In statistics, an **outlier** is a data point that differs significantly from other observations. An outlier may be due to variability in the measurement or it may indicate the experimental error; the latter are sometimes excluded from the data set. An outlier can cause serious problems in statistical analyses. There is no rigid mathematical definition of what constitutes an outlier; determining whether or not an observation is an outlier is ultimately a subjective exercise.

Credits: [Wikipedia](https://en.wikipedia.org/wiki/Outlier)

Outliers can occur due to the variety of reasons:

* mistakes during the **entering the data** results (manually put one extra zero for observation and, voilà!, you have an outlier);
* mistakes during the **measuring the data** or **experimental design** (if you want to measure the average sleep duration for subjects, but haven't specified the starting point of the recording, actual "falling" into sleep or time when subjects goes to the bed but still can spend some time conscious);
* **intentional outliers** (high-school students might to under-report the marijuana usage);
* mistakes during the **data processing** (forgot to convert to kilograms from pounds and now one value is 2.2 bigger than the others);
* **natural outliers** (that are not a mistake, but don't fit with the rest of the observations).

If you can step back and fix the mistake (for example, remove extra 0 from the observation so now the value is in a "normal" range), then you are good. However, if there is an extreme value(s) and you don't know why exactly it has occurred or/and how to fix it, then you might want to keep an eye on that observation so it doesn't affect your models/analysis. In the same way, there is no definite way what values should we call outliers, there is also no "golden standard" way of how to deal with them.

However, there are some common ways on how one could detect an outlier (note that cursive values are arbitrary and depend mostly on the observer):

1. Any value that is *two or more* standard deviation away from the mean (only for normal distribution);
2. Any value that is out of range of *5th* and *95th* percentile;
3. Any value that is beyond the range of *[Q1 - 1.5 IQR; Q3 + 1.5 IQR]*, where *Q1* - first quartile, *Q3* - third quartile, *IQR* - interquartile range (*Q3-Q1*).

The easiest way is to detect the outlier visually is through a **histogram** or a **boxplot**.

Your task is:

1. Read in the data with dementia cases (path to file: `"exercises/data/oasis_cross-sectional.csv"`);
2. Calculate the threshold values (save as `lower_bound` and `upper_bound` variables) for outliers detection using *mean ± 2std* method in the atlas scaling factor variable (`"ASF"`);
3. Make two plots, a histogram with vertical lines for threshold values and a boxplot;
4. Filter those observations that are beyond the threshold values that you calculated.

<codeblock id="06_08">

* to select specific values from the DataFrame you could use a structure like this: `df[df["<column>"] != <value>]`;

</codeblock>

What statement is **false**?

<choice id="1">
<opt text="There are no possible outliers according to the boxplot and 1.5IQR method" >
Note two points on the boxplot.
</opt>

<opt text="There are approximately more than 30 outliers using mean ± 2std method" >
outliers_df consists of 19 observations.
</opt>

<opt text="1.5IQR and mean±2std methods result in the same amount of possible outliers" correct="true">
mean±2std method resulted in a larger amount of possible outliers (19) compared to 1.5IQR method (2).
</opt>
</choice>

</exercise>
