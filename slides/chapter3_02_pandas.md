---
type: slides
---

# Working with table data through Pandas

---

# Welcome `pandas`

`pandas` is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

[Official Website](https://pandas.pydata.org/) || [Documentation](https://pandas.pydata.org/pandas-docs/stable/)

**Importing `pandas`**:

```python
import pandas as pd
```

Notes: Even though `numpy` is extremely using when it comes to numerical operations, sometimes we are dealing with the mixed data types and most of the time it comes in a tabular format. For these cases `numpy` is not really helpful, but `pandas` comes into play.

To put it simply, `pandas` allows you to work with the table data the way you work with tables in Excel but with much more benefits!

Commonly used alias name for `pandas` is `pd`.

---

# `pandas` Series (1)

One-dimensional `ndarray` with axis labels, that need not be unique. The object supports both integer- and label-based indexing.

```python
temperature = [18.0, 21.5, 21.0, 21.0, 18.8, 17.6, 20.9, 20.0]
temperature_series = pd.Series(temperature)
print(temperature_series)
```
```out
0    18.0
1    21.5
2    21.0
3    21.0
4    18.8
5    17.6
6    20.9
7    20.0
dtype: float64
```

Notes: The same way `numpy` has its object data type `ndarray`, in the same `pandas` has two main data types which allow you to perform all the cool stuff. We start with Series.

Series are basically **one**-dimensional array, that has a name and index name. Names could be integers, strings or strings, but they have to be unique. To put it simple, remember built-in lists objects? Lists consists of different values that could be called by an integer index. Series are almost the same, but they also allow using specified names instead of ordering index. We will look at the example of this a bit later. Another key difference is that Series don't really allow mixed data types within one object.

On our example we have a Searies with the values of `float64` type and indexes from `0` to `7`.

---

# `pandas` Series (2)

```python
print(temperature_series[2:4]) # slicing
```
```out
2    21.0
3    21.0
dtype: float64
```

```python
temperature_series = temperature_series * 9/5 + 32 # numerical operations
print(temperature_series)
```
```out
0    64.40
1    70.70
2    69.80
3    69.80
4    65.84
5    63.68
6    69.62
7    68.00
dtype: float64
```

```python
print(temperature_series.mean()) # useful methods
```
```out
67.73
```

Notes: `pandas` Series allow slicing like more of the objects with the `[<start index>:<end index>:<step>]` structure.

They also allow performing numerical operations in a simple "vectored" way without looping all over all values.

And of course Series have their own unique methods that can be applied on them.

---

# `pandas` DataFrame

```python
oasis_df = pd.read_csv("/content/oasis_cross-sectional.csv")
display(oasis_df)
```

<img src="dataframe.png" width="600">

Notes: Second data type is `pandas` DataFrames. It is basically a collection of multiple Series that represent columns. DataFrames have column names and row names (indexes) and can be only **two** dimensional.

You can see example of a csv file being uploaded into Python and converted into DataFrame. The data is from Vos et al. (2013)\* experiment and represents the data of patients with Alzheimer's.

Note that now withing each column the type is the same but overall types are different for the whole DataFrame. And that's what you would probably expect. Usually, each row represents a particular observation or subject data, whereas column represent different features of that observation. So you would expect that for the column (feature) "Age" all subjects have a numeric values and for the column "Name" - strings.

\* Vos SJ, Xiong C, Visser PJ, Jasielec MS, Hassenstab J, Grant EA, Cairns NJ, Morris JC, Holtzman DM, Fagan AM. Preclinical Alzheimer's disease and its outcome: a longitudinal cohort study. *Lancet Neurol*. 2013 Oct;12(10):957-65. doi: 10.1016/S1474-4422(13)70194-7. Epub 2013 Sep 4. PMID: 24012374; PMCID: PMC3904678.

---

# What's inside

```python
print(oasis_df.info())
```
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

Notes: Calling a `.info()` method is always a good place to start working with your data. It gives you a brief overview what's inside your DataFrame. As you can see, here we have 436 rows (observations) and 12 columns (features).

In the columns table you see the column name, how many non-null values are present (in other words, how many values are **not** missing) and what are the type of variables in each column. Note that `pandas` marks strings as `object`.

We can already notice that column `Delay` has only 20 values, meaning that `436-20=416` values are missing. Missing values are represented as `np.NaN`, which stands for Non A Number.
---

# Selecting columns

#### Selecting one column, returns Series:

```python
oasis_df['Age']
```
```out
0      74
1      55
       ..
434    20
435    26
Name: Age, Length: 436, dtype: int64
```
#### Selecting multiple columns, returns DataFrame:

```python
oasis_df[['Age', 'Educ', 'SES']]
```
```out
     Age  Educ  SES
0     74   2.0  3.0
1     55   4.0  1.0
..   ...   ...  ...
434   20   NaN  NaN
435   26   NaN  NaN
[436 rows x 3 columns]
```

Notes: You can easily select any column to work with by specifying its name as string inside the indexing brackets. In such case you get a `pandas` Series.

If you want to select two or more columns at the time you can pass a list with column names inside the index. In this case you get a `pandas` DataFrame object.

---

# Indexing in pandas

<center><img src="https://shanelynnwebsite-mid9n9g1q9y8tt.netdna-ssl.com/wp-content/uploads/2016/10/Pandas-selections-and-indexing.png" width="600"></center>

*Image credit: [Shane Lynn](https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/)*

Notes: DataFrames have also another a bit specific way of indexing. Remember that you can index by the columns and rows at the same time. There are two options:

1. Index the the **index** (or `i`nteger-`loc`ation). In this case we use `<DataFrame>.iloc[<row position(s)>, <column position(s)>]`. You can specify one position as an integer, or multiple positions as a list or use slicing `<position1>:<position2>`. All the columns/rows will be selected (excluding the `position2`) in the slice.
2. Index by the **name** (or `loc`ation). In this case we use `<DataFrame>.loc[<row name(s)>, <column name(s)>]`. You can specify one name as a string, or multiple names as a list or use slicing `<name1>:<name2>`. All the columns/rows will be selected (including the `name2`) in the slice. Also you can specify the Boolean list index where all the rows/columns that correspond to the `True` value will be included.

---

# Filtering data

#### Filter a whole DataFrame by specific condition:
```python
condition = (oasis_df['M/F'] == 'F') & (oasis_df['Age'] > 60)
oasis_df[condition]
```
```out
ID M/F Hand  Age  Educ  ...  CDR  eTIV   nWBV    ASF  Delay
0    OAS1_0001_MR1   F    R   74   2.0  ...  0.0  1344  0.743  1.306    NaN
2    OAS1_0003_MR1   F    R   73   4.0  ...  0.5  1454  0.708  1.207    NaN
..             ...  ..  ...  ...   ...  ...  ...   ...    ...    ...    ...
413  OAS1_0455_MR1   F    R   61   2.0  ...  0.0  1354  0.825  1.297    NaN
415  OAS1_0457_MR1   F    R   62   3.0  ...  0.0  1372  0.766  1.279    NaN
[129 rows x 12 columns]
```
#### Select a column and filter by condition:

```python
oasis_df['ID'][oasis_df['nWBV'].between(0.7, 0.8)]
```
```out
0      OAS1_0001_MR1
2      OAS1_0003_MR1
           ...      
421    OAS1_0117_MR2
432    OAS1_0353_MR2
Name: ID, Length: 162, dtype: object
```

Notes: To filter the data you have to specify the condition to filter on. In the same way as we did before, you can combine multiple condition with `&` (AND) or `|` (OR) operations.

In the first example we are taking all the observations that meet the criteria: fender is female and age is greater than 60. Note that you don't have to create a separate object (`condition`), it was done only for a better visual representation.

In the second example first we take the column `ID` and then we filter the Series by the condition that normalized whole-brain volume (`nWBV`) should be in a range between 0.7 and 0.8.

---

# Data aggregation

```python
oasis_df.groupby(by=["CDR", "M/F"]).agg({"eTIV": "min", "nWBV": "mean"})
```
```out
          TIV      nWBV
CDR M/F                
0.0 F    1123  0.771722
    M    1301  0.762868
0.5 F    1171  0.732000
    M    1307  0.726161
1.0 F    1274  0.704474
    M    1419  0.709778
2.0 F    1401  0.703000
    M    1512  0.665000
```

Notes: Another useful tool is grouping and aggregation of the data. In this example we want to see the minimum estimated total intracranial volume (`eTIV`) and average normalized whole-brain volume (`nWBV`) for each gender and clinical dementia rating (`CDR`). This line of code might seem a bit complicated, but we can split it in parts:

1. Group by a list of column names. If you wanted to split just by one column, you could specify just a string with column name, for example `by="CDR"`.
2. Right now we have a "grouped" DataFrame object, which is not that interesting. We apply aggregation method and specify a dictionary in a following way: `{"<column name>": "<aggregation function>"}`. If you wanted to apply multiple functions on the same column you could specify a list, for example, `{"eTIV": ["min", "max"]}`.

*Clinical Dementia Rating (0 = no dementia, 0.5 = very mild AD, 1 = mild AD, 2 = moderate AD)*

---

# Let's code!
