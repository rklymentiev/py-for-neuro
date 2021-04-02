---
title: 'Chapter 3: Packages for Data Manipulation'
description:
  'Here we will introduce two main packages for working with data. We are going to see how can we use NumPy to perform linear algebra calculations and how to perform data manipulations on tabular data using Pandas.'
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="NumPy" type="slides">

<slides source="chapter3_01_numpy">
</slides>

</exercise>

<exercise id="2" title="NumPy exercises">

**Question 1**. What is **not the right way** to import `numpy` package?

<choice>
<opt text="import numpy">
This line of code is valid. You can import a package without any alias.
</opt>

<opt text="import numpy as np">
There is nothing wrong with that line. In fact, this is the most common way.
</opt>

<opt text="import numpy as neuroscience">
"neuroscience" alias name would be confusing for other people, but you can use it, if you like.
</opt>

<opt text="from numpy import np" correct="true">
We use `from ___ import ___` when we want to import a specific module or function. from a package This would be a valid line of code, if `numpy` package had a `np` module/function.
</opt>
</choice>

**Exercise 1**. You performed a learning task for subjects with anxiety (anxiety level was measured according to Speilberger Trait Anxiety Inventory (TAI)\*). Variable `X` is the corresponding TAI of each subject. Variable `y` is the accuracy score (0-100% range).

<center><img src="regression_anxiety.png" width="500"></center>

Build a linear regression model:

<center><img src="https://latex.codecogs.com/gif.latex?\text{Accuracy}&space;=&space;b_0&space;&plus;&space;b_1&space;\times&space;\text{TAI}" title="\text{Accuracy} = b_0 + b_1 \times \text{TAI}" /></center>

where *b0* is the intercept, *b1* is the slope parameter.

These b coefficients can be found as:

<center><img src="https://latex.codecogs.com/gif.latex?b&space;=&space;(X^T&space;X)^{-1}&space;X^T&space;y" title="b = (X^T X)^{-1} X^T y" /></center>

which will result in (2x1) matrix with (1,1) value of *b0* and (2,1) value of *b1*.



* Spielberger, C. D., Gorsuch, R. L., Lushene, R., Vagg, P. R., & Jacobs, G. A. (1983). *Manual for the State-Trait Anxiety Inventory*. Palo Alto, CA: Consulting Psychologists Press.

<codeblock id="03_01">

- transpose matrix can be found using method `.transpose()` or `.T`;
- inverse matrix can be found using `np.linalg.inv(<array>)`;
- matrix multiplication can be done using `np.matmul(<array1>, <array2>)` or `<array1>@<array2>`.

</codeblock>

**Exercise 2**. Now that you have found *b* coefficients, what is the value of root mean squared error (RMSE)?

<center><img src="https://latex.codecogs.com/gif.latex?\text{RMSE}&space;=&space;\sqrt{\sum_{i=0}^n&space;\frac{(y_{\text{pred}}&space;-&space;y_{\text{true}}&space;)^2}{n}}" title="\text{RMSE} = \sqrt{\sum_{i=0}^n \frac{(y_{\text{pred}} - y_{\text{true}} )^2}{n}}" /></center>

Value <img src="https://latex.codecogs.com/gif.latex?(y_{\text{pred}}&space;-&space;y_{\text{true}})" title="(y_{\text{pred}} - y_{\text{true}})" /> is called a **residual** (or error). Example of such value is shown in red on the plot below.

<center><img src="regression_anxiety_line.png" width="500"></center>

To find RMSE, you have to :

1. find the **predicted** value of accuracy (`y`) for each TAI score (`X`). Keep in mind, that `X` array has two columns, first column consists of ones and second columns is the actual TAI scores.
2. take the difference between the predicted and actual value of `y` (residuals) and square it
3. take the average of all squared residual values and get a square root of that value.

<codeblock id="03_02">

- predicted values can be found by *b0 + b1 X*;
- `np.mean()` and `np.sqrt()` functions might help.

</codeblock>

</exercise>

<exercise id="3" title="Pandas" type="slides">

<slides source="chapter3_02_pandas">
</slides>

</exercise>

<exercise id="4" title="Pandas exercises">

**Question 1**. How many missing values are in the socioeconomic status column (`SES`)?

```out
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 436 entries, 0 to 435
Data columns (total 12 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   ID      436 non-null    object
 1   M/F     436 non-null    object
 2   Hand    436 non-null    object
 3   Age     436 non-null    int64  
 4   Educ    235 non-null    float64
 5   SES     216 non-null    float64
 6   MMSE    235 non-null    float64
 7   CDR     235 non-null    float64
 8   eTIV    436 non-null    int64  
 9   nWBV    436 non-null    float64
 10  ASF     436 non-null    float64
 11  Delay   20 non-null     float64
dtypes: float64(7), int64(2), object(3)
memory usage: 41.0+ KB
```

<choice id="1">
<opt text="436">
That's the total amount of observations in a column.
</opt>

<opt text="220" correct="true">
There are 436-216 = 220 missing values in a column.
</opt>

<opt text="216">
That's the total amount of *non-missing* observations in a column.
</opt>
</choice>

**Question 2**. Could you add more dimensions and make the DataFrame multi-dimensional?

<choice id="2">
<opt text="No" correct="true">
DataFrames can only have two dimensions (rows and columns).
</opt>
<opt text="Yes">
Could you imagine a 5D csv file?
</opt>
</choice>

**Exercise 1**. What is the average socioeconomic status (`SES`) for subjects without dementia? Do this in two methods (that will lead to the same outcome): through selection the column and filtering condition separately and by using `.loc` operator.

* Clinical Dementia Rating column (`CDR`) is represented in a following way: 0 = no dementia, 0.5 = very mild AD, 1 = mild AD, 2 = moderate AD.
* Socioeconomic status is assessed by the Hollingshead Index of Social Position and classified into categories from 1 (highest status) to 5 (lowest status).


<codeblock id="03_03">

- to get the `avg_ses1` you can select the column first, and then specify the filtering condition. After this is done you can apply `.mean()` function on a resulted Series;
- to get the `avg_ses2` you can specify the condition in a **row** selection (in other words, what columns should `.loc` take) and a column name in a **column** selection. This will result again in Series.

</codeblock>

**Exercise 2**. For each outcome of clinical dementia rating (`CDR`) get a count of observations and the median of the normalized whole-brain volume (`nWBV`). Rename the columns in aggregated DataFrame, so they are more representative.

* `<DataFrame>.rename()` methods takes an argument `columns` to change the column names. You should pass a dictionary in a dictionary `{"<old name>": "<new name>"}`. `inplace=True` will overwrite the DataFrame (save the new column names).

<codeblock id="03_04">

- to get the count you can choose a `ID` column and specify `"count"` function in a dictionary;
- note that `count` returns count of non-negative observations so results might be sometimes confusing.

</codeblock>

</exercise>

<exercise id="5" title="Joining data in Pandas" type="slides">

<slides source="chapter3_03_pandas_joins">
</slides>

</exercise>

<exercise id="6" title="Joining practice">

**Exercise 1**. You have two DataFrames loaded in. One has IDs of patients and the breast cancer status (malignant or benign). The other one has IDs of patients and some features for cell nucleus.

* `radius_mean`: mean of distances from center to points on the perimeter;
* `texture_mean`: standard deviation of gray-scale values;
* `perimeter`: mean size of the core tumor.

Is the average of `radius_mean` value is greater for malignant type?

| `table_1` | `table_2` |
|:-:|:-:|
| <center><img src="table1.png"></center> | <center><img src="table2.png" ></center> |

This is the sample of so called **Breast Cancer Wisconsin (Diagnostic) Data Set**.

Credits: W.N. Street, W.H. Wolberg and O.L. Mangasarian. Nuclear feature extraction for breast tumor diagnosis. IS&T/SPIE 1993 International Symposium on Electronic Imaging: Science and Technology, volume 1905, pages 861-870, San Jose, CA, 1993.

<codeblock id="03_05">

- basically any type of join would be appropriate here, since we are interested in matching breast cancer type with `radius_mean` and we could have missing values that don't affect calculations for the average value;
- keep in mind that joining column names are different;
- to get the average `radius_mean` you have to filter the data by a condition and then perform `.mean()` function on a selected column.

</codeblock>

**Exercise 2**. This time get all the features for cell nucleus and label with the type of cancer. When the cancer type is not specified mark it as "unknown". Don't change missing values in other columns.

You could also notice that now you joined DataFrame has two columns "id" and "ID" from both tables. Keep only the column that has all the parameters values.

*Hint! To replace the missing value you can use `.fillna()` method.*

<codeblock id="03_06">

- right join would be more appropriate here (or left join if you define the `table2` as the left one);
- to remove the column you can use `.drop()` method. Don't forget the specify the axis (0: rows, 1: columns);
- don't forget the rewrite the column `'diagnosis'` after you replace the missing values.

</codeblock>

</exercise>
