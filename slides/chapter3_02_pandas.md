---
type: slides
---

# Working with table data with Pandas

---

# Hello Pandas

`pandas` is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

[Website](https://pandas.pydata.org/) || [Documentation](https://pandas.pydata.org/pandas-docs/stable/)

### Importing Pandas:

```python
import pandas as pd
```

Notes: Even though NumPy is extremely useful when it comes to numerical operations, sometimes we are dealing with mixed data types and most of the time it comes in a tabular format. For these cases, NumPy is not really helpful, but Pandas comes into play.

To put it simply, Pandas allows you to work with the table data the same way you work with tables in Excel but with much more benefits!

The commonly used alias name for Pandas is `pd`.

---

# Pandas Series (1)

One-dimensional `ndarray` with axis labels, that need not be unique. The object supports both integer- and label-based indexing.

```python
import pandas as pd

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

Notes: Just like NumPy has its object data type `ndarray`, in the same way Pandas has two main data types which allow you to perform all the cool stuff. We start with Series.

Series are basically **one**-dimensional array, that has a name and index name. Names could be integers or strings, but they have to be unique. To put it simply, remember built-in lists objects? Lists consist of different values that could be called by an integer index. Series are almost the same, but they also allow usage of specified names instead of ordering index. We will look at the example of this a bit later. Another key difference is that Series don't allow mixed data types within one object.

In our example, we have a Series with the values of `float64` type and indexes from `0` to `7`.

---

# Pandas Series (2)

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

Notes: Pandas Series allow slicing like more of the objects with the `[<start index>:<end index>:<step>]` structure.

They also allow performing numerical operations in a simple "vectored" way without looping over all values.

And of course Series have their own unique methods that can be applied to them.

---

# Pandas DataFrame

```python
dementia_df = pd.read_csv("/content/oasis_cross-sectional.csv")
display(dementia_df)
```

<img src="imgs/dataframe.png" width="600">

Notes: The second data type is Pandas DataFrames. It is basically a collection of multiple Series that represent columns. DataFrames have column names and row names (indexes) and can be only **two** dimensional.

You can see an example of a csv file being uploaded into Python and converted into DataFrame. The data is from Vos et al. (2013) experiment and represents the data of patients with different levels of dementia.

Note that now the type is the same within each column but overall types can be different for the whole DataFrame. And that's what you would probably expect. Usually, each row represents a particular observation or subject data, whereas the column represents different features of that observation. So you would expect that for the column (feature) "Age" all subjects have numeric values and strings for the column "Name".

---

# What's inside

```python
print(dementia_df.info())
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

Notes: Calling the `.info()` method is always a good place to start working with your data. It gives you a brief overview of what's inside your DataFrame. As you can see, here we have 436 rows (observations) and 12 columns (features).

In the columns table you see the column name, how many non-null values are present (in other words, how many values are **not** missing), and what is the type of variables in each column. Note that Pandas marks strings as `object`.

We can already notice that column `Delay` has only 20 values, meaning that `436-20=416` values are missing. Missing values are represented as `np.NaN`, which stands for Non A Number.
---

# Selecting columns

#### Selecting one column, returns Series:

```python
dementia_df['Age']
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
dementia_df[['Age', 'Educ', 'SES']]
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

Notes: You can easily select any column to work with by specifying its name as a string inside the indexing brackets. In such a case, you get a `pandas` Series.

If you want to select two or more columns at a time, you can pass a list with column names inside the brackets. In this case, you get a Pandas DataFrame object.

---

# Indexing in pandas

<center><img src="https://shanelynnwebsite-mid9n9g1q9y8tt.netdna-ssl.com/wp-content/uploads/2016/10/Pandas-selections-and-indexing.png" width="600"></center>

*Image credit: [Shane Lynn](https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/)*

Notes: DataFrames have a bit specific way of indexing. Remember that you can index by the columns and rows at the same time. There are two options:

1. Index the the **index** (or `i`nteger-`loc`ation). In this case we use `<DataFrame>.iloc[<row position(s)>, <column position(s)>]`. You can specify one position as an integer, or multiple positions as a list or use slicing `<position1>:<position2>`. All the columns/rows will be selected (excluding the `position2`) in the slice.
2. Index by the **name** (or `loc`ation). In this case, we use `<DataFrame>.loc[<row name(s)>, <column name(s)>]`. You can specify one name as a string, multiple names as a list, or use slicing `<name1>:<name2>`. All the columns/rows will be selected (including the `name2`) in the slice. Also, you can specify the Boolean list index where all the rows/columns that correspond to the `True` value will be included.

---

# Filtering data

#### Filter a whole DataFrame by specific condition:
```python
condition = (dementia_df['M/F'] == 'F') & (dementia_df['Age'] > 60)
dementia_df[condition]
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
dementia_df['ID'][dementia_df['nWBV'].between(0.7, 0.8)]
```
```out
0      OAS1_0001_MR1
2      OAS1_0003_MR1
           ...      
421    OAS1_0117_MR2
432    OAS1_0353_MR2
Name: ID, Length: 162, dtype: object
```

Notes: To filter the data you have to specify the condition to filter on. In the same way, as we did before, you can combine multiple conditions with `&` (AND) or `|` (OR) operations.

In the first example, we are taking all the observations that meet the criteria: gender is female and age is greater than 60. Note that you don't have to create a separate object (`condition`), it was done only for a better visual representation.

In the second example, first, we take the column `ID` and then we filter the Series by the condition that normalized whole-brain volume (`nWBV`) should be in a range between 0.7 and 0.8.

---

# Data aggregation

```python
dementia_df.groupby(by=["CDR", "M/F"]).agg({"eTIV": "min", "nWBV": "mean"})
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

Notes: Another useful tool is the grouping and aggregation of the data. In this example, we want to see the minimum estimated total intracranial volume (`eTIV`) and average normalized whole-brain volume (`nWBV`) for each gender and clinical dementia rating (`CDR`). This line of code might seem a bit complicated, but we can split it into parts:

1. Group by a list of column names. If you wanted to split just by one column, you could specify just a string with a column name, for example, `by="CDR"`.
2. Right now we have a "grouped" DataFrame object, which is not that interesting. We apply aggregation method and specify a dictionary in a following way: `{"<column name>": "<aggregation function>"}`. If you wanted to apply multiple functions on the same column you could specify a list, for example, `{"eTIV": ["min", "max"]}`.

*Clinical Dementia Rating: 0 = no dementia, 0.5 = very mild AD, 1 = mild AD, 2 = moderate AD*

---

# Let's code!
