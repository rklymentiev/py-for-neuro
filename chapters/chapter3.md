---
title: 'Chapter 3: Packages for Data Manipulation'
description:
  'We will introduce two main packages for working with data. We are going to see how we can use NumPy to perform linear algebra calculations and how to perform data manipulations on tabular data using Pandas.'
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="How to import the package">

To import any package we use `import` statement. Let's consider package NumPy for example. We could import it in several ways:

```python
# option 1
import numpy

x = numpy.sqrt(4)
```


```python
# option 2 (most commonly used)
import numpy as np

x = np.sqrt(4)
```
```python
# option 3
import numpy as CraZy_NaMe

x = CraZy_NaMe.sqrt(4)
```

Option 1 is pretty straightforward. You import the whole package to the workspace and later you can access its content using `numpy.` prefix, for example `numpy.sqrt()`.

You might wonder what is that `as np` doing in the option 2. This is what is called "aliasing". Most of the packages have the "short" alias name, that is commonly used. In this way, we specify that we are going to load the NumPy library and will store it in `np` object. All the functions from the package will be called using `np.` prefix, for example `np.sqrt()`.

Basically, you could also import the package as in option 3 and later you would call any function from it as `CraZy_NaMe.sqrt()`. Such a method is not recommended since it can be difficult for others to follow the code.

It can happen that you don't need the whole package imported into the workspace (due to the memory limitations for example). You can also import desired functions or modules (you can think of a module as "mini package" inside the package with functions) from the package in the following way:

```python
from numpy import sqrt, linalg

x = sqrt(4)
```

In this way we import function `sqrt()` and module `linalg` (which has multiple function inside, such as `linalg.matrix_power()`). Note that we don't use `numpy.` prefix in such case.

</exercise>

<exercise id="2" title="NumPy" type="slides">

<slides source="chapter3_01_numpy">
</slides>

</exercise>

<exercise id="3" title="NumPy exercises">

**Question**. What is **not the right way** to import `numpy` package?

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
We use `from ___ import ___` when we want to import a specific module or function from a package. This would be a valid line of code, if `numpy` package had a `np` module/function.
</opt>
</choice>

**Exercise**. You have a sample from EEG data from Cavanagh et al. (2019) study. This sample consists of around 10 seconds of data measurements sampled at 500 Hz frequency and measured at 66 channels.

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

* `eeg['ch_names']`: numpy array of shape (66,). Represents the channel names.
* `eeg['data']`: numpy array of shape (66, 50001). Represents the actual data in a (channel, time) format.
* `eeg['srate']`: int. Represents the sampling rate [Hz].
* `eeg['times']`: numpy array of shape (50001,). Represents the time vector [s].

Your task is:

1. Find the index of the C1 electrode in `eeg['ch_names']` array.
2. Use the location of the C1 electrode and indexes `(1000:2001)` for the time axis to slice the signal for the channel C1 from 2s to 4s of recording. Note that the resulting array will have the shape (1, 1001).
3. Find the maximum, minimum, and mean values of the resulting array `c1_data`.
4. Find the indexes that correspond to these values in the `c1_data` array using [`np.where()`](https://numpy.org/doc/stable/reference/generated/numpy.where.html) function.
5. Print out the results using f-string. Convert values to micro Volts and round up to the 2nd digit.

<codeblock id="03_07">

- to filter out just one channel you can use the following structure: `<np.array>[<condition>]`;
- NumPy arrays have lots of useful methods for descriptive statistics, such as `<np.array>.var()`, `<np.array>.std()`, etc.

</codeblock>

You could notice that solution using `c1_data[0, :]` for finding the time points of max and min values. Why did we include only `0` value for the 1-st dimension in the slicing? Let's take a look at two cases:

```python
t_1 = np.where(c1_data == max_v)
t_2 = np.where(c1_data[0, :] == max_v)
print(t_1)
print(t_2)
```

```out
(array([0]), array([524]))
(array([524]),)
```

In the first case for `t_1`, function `np.where()` found the maximum value in the *whole* array and returned a tuple, which tells us that the maximum element is located on the 0th index for the first dimension and 524-th index for the second dimension. But since we know that our data doesn't have any other indexes in the first dimension, we can search for the index using `0` index as a slicing value to avoid redundant results as we did for `t_2` example. In this case, we also reshape the `c1_data` array from a 2-D array with the shape (1, 1001) to a 1-D array with the shape (1001,).

</exercise>

<exercise id="4" title="NumPy exercises: Linear Regression">

**Exercise 1**. You performed a learning task for subjects with anxiety (anxiety level was measured according to Speilberger Trait Anxiety Inventory (TAI)). Variable `X` is the corresponding TAI of each subject. Variable `y` is the accuracy score (0-100% range).

```python
import numpy as np

X = np.load("exercises/data/X.npy")
y = np.load("exercises/data/y.npy")
print(X)
```
```out
[[ 1.  54.1]
 [ 1.  40. ]
 [ 1.  53.1]
 [ 1.  66. ]
 [ 1.  31.1]
 [ 1.  46.8]
 [ 1.  47.6]
 [ 1.  33.6]
 [ 1.  44.8]
 [ 1.  50.8]
 [ 1.  51.9]
 [ 1.  50.8]
 [ 1.  39.8]
 [ 1.  46.3]
 [ 1.  33.7]
 [ 1.  34. ]
 [ 1.  44.8]
 [ 1.  49.4]
 [ 1.  32.5]
 [ 1.  37.7]]
```
```python
print(y)
```
```out
[53.9 42.8 52.9 43.3 77.5 39. 43.6 54.8 64.6 43.1 63. 35.4 42.6 60.8 60.6 59.8 64.6 57. 70.3 55.3]
```

<center><img src="imgs/regression_anxiety.png" width="500"></center>

Build a linear regression model using [Ordinary Least Squares method](https://en.wikipedia.org/wiki/Ordinary_least_squares):

<center><img src="https://latex.codecogs.com/gif.latex?\text{Accuracy}&space;=&space;b_0&space;&plus;&space;b_1&space;\times&space;\text{TAI}" title="\text{Accuracy} = b_0 + b_1 \times \text{TAI}" /></center>

where *b0* is the intercept, *b1* is the slope parameter.

These *b* coefficients can be found as:

<center><img src="https://latex.codecogs.com/gif.latex?b&space;=&space;(X^T&space;X)^{-1}&space;X^T&space;y" title="b = (X^T X)^{-1} X^T y" /></center>

which will result in (2x1) matrix with (1,1) value of *b0* and (2,1) value of *b1*.

Note that `X` array has (20,2) shape where the first column is column of ones. This is done to fit the intercept of the linear regression model. You can learn more about linear regression model here:

* Blog post: [A (not that) Simple Least Squares Regression](https://defme.xyz/post/least-squares-regression/)
* YouTube video: [StatQuest: Linear Models Pt.1 - Linear Regression](https://www.youtube.com/watch?v=nk2CQITm_eo)

<codeblock id="03_01">

- transpose matrix can be found using method `.transpose()` or `.T`;
- inverse matrix can be found using `np.linalg.inv(<array>)`;
- matrix multiplication can be done using `np.matmul(<array1>, <array2>)` or `<array1>@<array2>`.

</codeblock>

**Exercise 2**. Now that you have found *b* coefficients, what is the value of root mean squared error (RMSE)?

<center><img src="https://latex.codecogs.com/gif.latex?\text{RMSE}&space;=&space;\sqrt{\sum_{i=0}^n&space;\frac{(y_{\text{pred}}&space;-&space;y_{\text{true}}&space;)^2}{n}}" title="\text{RMSE} = \sqrt{\sum_{i=0}^n \frac{(y_{\text{pred}} - y_{\text{true}} )^2}{n}}" /></center>

Value <img src="https://latex.codecogs.com/gif.latex?(y_{\text{pred}}&space;-&space;y_{\text{true}})" title="(y_{\text{pred}} - y_{\text{true}})" /> is called a **residual** (or error). Example of such value is shown in red on the plot below.

<center><img src="imgs/regression_anxiety_line.png" width="500"></center>

To find RMSE, you have to :

1. Find the **predicted** value of accuracy (`y`) for each TAI score (`X`). Keep in mind, that `X` array has two columns, the first column consists of ones and the second column is the actual TAI scores.
2. Take the difference between the predicted and actual value of `y` (residuals) and square it.
3. Take the average of all squared residual values and get a square root of that value.

<codeblock id="03_02">

- predicted values can be found by *b0 + b1 X*, but remember that you need only the second column from `X` array;
- `np.mean()` and `np.sqrt()` functions might also help;

</codeblock>

</exercise>

<exercise id="5" title="Pandas" type="slides">

<slides source="chapter3_02_pandas">
</slides>

</exercise>

<exercise id="6" title="Pandas exercises">

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
Can you imagine a 5 dimensional csv file?
</opt>
</choice>

**Exercise 1**. What is the average socioeconomic status (`SES`) for subjects without dementia? Do this in two methods (that will lead to the same outcome): through selection of the column and filtering condition separately and by using `.loc` operator.

* Clinical Dementia Rating column (`CDR`) is represented in a following way: 0 = no dementia, 0.5 = very mild AD, 1 = mild AD, 2 = moderate AD.
* Socioeconomic status is assessed by the Hollingshead Index of Social Position and classified into categories from 1 (highest status) to 5 (lowest status).


<codeblock id="03_03">

- to get the `avg_ses1` you can select the column first, and then specify the filtering condition. After this is done you can apply `.mean()` function on a resulting Series;
- to get the `avg_ses2` you can specify the condition in a **row** selection (in other words, what columns should `.loc` take) and a column name in a **column** selection. This will result again in Series.

</codeblock>

**Exercise 2**. For each outcome of clinical dementia rating (`CDR`) get a count of observations and the median of the normalized whole-brain volume (`nWBV`). Rename the columns in aggregated DataFrame, so they are more representative.

**Hint!** [`<DataFrame>.rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) method takes an argument `columns` to change the column names. You should pass a dictionary in a dictionary `{"<old name>": "<new name>"}`. `inplace=True` will overwrite the DataFrame (save the new column names).

<codeblock id="03_04">

- to get the count you can choose a `ID` column and specify `"count"` function in a dictionary. Median function is `"median"` (surprisingly);
- note that `count` returns count of non-negative observations so results might be sometimes confusing.

</codeblock>

</exercise>

<exercise id="7" title="Joining data in Pandas" type="slides">

<slides source="chapter3_03_pandas_joins">
</slides>

</exercise>

<exercise id="8" title="Joining practice">

**Exercise 1**. You have two DataFrames loaded in. One has IDs of patients and the breast cancer status (malignant or benign). The other one has IDs of patients and some features for the cell nucleus.

* `radius_mean`: mean of distances from the center to points on the perimeter;
* `texture_mean`: standard deviation of gray-scale values;
* `perimeter`: mean size of the core tumor.

Is the average `radius_mean` value is greater for malignant type?

| `table_1` | `table_2` |
|:-:|:-:|
| <center><img src="imgs/table1.png"></center> | <center><img src="imgs/table2.png" ></center> |

<codeblock id="03_05">

- basically any type of join would be appropriate here since we are interested in matching breast cancer type with `radius_mean` and we could have missing values that don't affect calculations for the average value;
- keep in mind that joining column names are different;
- to get the average `radius_mean` you have to filter the data by a condition and then perform `.mean()` function on a selected column.

</codeblock>

**Exercise 2**. This time get all the features for the cell nucleus and label them with the type of cancer. When the cancer type is not specified mark it as "unknown". Don't change missing values in other columns.

The joined DataFrame will have two columns `"id"` and `"ID"`. Keep only the first column.

**Hint!** To replace the missing value you can use [`.fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html) method. It can be applied on Series or DataFrame.

<codeblock id="03_06">

- right join would be more appropriate here (or left join if you define the `table2` as the left one);
- to remove the column `"ID"` you can use [`.drop()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html) method. Don't forget the specify the `axis` (0: rows, 1: columns);
- don't forget the rewrite the column `'diagnosis'` after you replace the missing values.

</codeblock>

</exercise>
