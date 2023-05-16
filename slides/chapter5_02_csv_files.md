---
type: slides
---

# Working with CSV/Excel files

---

# What CSV stands for

A **comma-separated values (CSV)** file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields.

Credits: [Wikipedia](https://en.wikipedia.org/wiki/Comma-separated_values)

<center><img src="io/csv_demo.png"></img></center>

Notes: Even though it's called **comma**-separated values file, in reality you can use any separator to save a CSV file (like ";" and "\t" (tab sign)).

You can see an example of a tabular CSV file in a "raw" view. Each line in the file represents an observation (in this particular case the very first line is a header with column names). Each column value is separated by the comma.

---

# Reading CSV files with numpy

#### Input file:

<center><img src="io/fmri_sample.png" width="600"></img></center>

```python
import numpy as np
frmi_smpl = np.loadtxt(fname="fmri_sample.csv", delimiter=",")
frmi_smpl.shape
```
```out
(14, 19)
```

Notes: To load the CSV file as a `numpy` array we can use `np.loadtxt()` function. `delimiter` argument specifies how observations are separated in the input file.

Keep in mind, that `np.loadtxt()` expects that **all** data in the input file is in numerical format and without headers/column names.

Example on the left represents the sample from the fMRI data for the observation from the frontal region. Each row represents a subject (14 in total). Each column represents a timepoint (19 in total).

---

# Writing CSV files with numpy

```python
np.savetxt(fname="one_subject.csv", X=frmi_smpl[0,:], delimiter=",")
```

#### Output file:

<center><img src="io/one_subj.png" width="600"></img></center>

Notes: To save `numpy` arrays to a CSV file we can use `np.savetxt()` where file name, input array and (optionally) delimiter need to be specified.

Here is the example of saving observations from one subject.

---

# Reading CSV/Excel files with pandas (1)

```python
oasis_df = pd.read_csv(filepath_or_buffer="oasis_cross-sectional.csv", sep=",") # CSV files
display(oasis_df.head())
```
```out
    ID           M/F Hand  Age  Educ  SES  MMSE  CDR  eTIV   nWBV    ASF  Delay
0  OAS1_0001_MR1   F    R   74   2.0  3.0  29.0  0.0  1344  0.743  1.306    NaN
1  OAS1_0002_MR1   F    R   55   4.0  1.0  29.0  0.0  1147  0.810  1.531    NaN
2  OAS1_0003_MR1   F    R   73   4.0  3.0  27.0  0.5  1454  0.708  1.207    NaN
3  OAS1_0004_MR1   M    R   28   NaN  NaN   NaN  NaN  1588  0.803  1.105    NaN
4  OAS1_0005_MR1   M    R   18   NaN  NaN   NaN  NaN  1737  0.848  1.010    NaN
```
```python
oasis_df = pd.read_excel(io="oasis_cross-sectional.csv", sheet_name=0) # Excel files
display(oasis_df.head())
```
```out
    ID           M/F Hand  Age  Educ  SES  MMSE  CDR  eTIV   nWBV    ASF  Delay
0  OAS1_0001_MR1   F    R   74   2.0  3.0  29.0  0.0  1344  0.743  1.306    NaN
1  OAS1_0002_MR1   F    R   55   4.0  1.0  29.0  0.0  1147  0.810  1.531    NaN
2  OAS1_0003_MR1   F    R   73   4.0  3.0  27.0  0.5  1454  0.708  1.207    NaN
3  OAS1_0004_MR1   M    R   28   NaN  NaN   NaN  NaN  1588  0.803  1.105    NaN
4  OAS1_0005_MR1   M    R   18   NaN  NaN   NaN  NaN  1737  0.848  1.010    NaN
```

Notes: To read a CSV file we can use a [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) function. As told before, even though CSV has "comma" in its name, other separators can be also used. In such case we have to specify the `sep` argument (default is `","`).

To read en Excel file (.xls, .xlsx) we can use [`pd.read_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) function. If Excel file has multiple sheets, the desired sheet can be specified by `sheet_name` argument by the actual name (as a string) or by a order number (as an integer).

---

# Reading CSV/Excel files with pandas (2)

#### URL with the file:

```python
URL = "https://raw.githubusercontent.com/rklymentiev/py-for-neuro/binder/exercises/data/oasis_cross-sectional.csv"
dementia_df = pd.read_csv(filepath_or_buffer=URL)
```

#### Compressed file:

<center><img src="io/csv_zip.png" width="600"></img></center>

```python
dementia_df = pd.read_csv(filepath_or_buffer="oasis_cross-sectional.zip")
```

Notes: The good part about Pandas is that it allows to load files directly from the internet by the direct URL to the file.

Also file can be compressed in an archive (for example, .zip or .7z) and we can open it in Pandas without extracting it.

---

# Writing CSV/Excel files with pandas

```python
dementia_df.to_csv(path_or_buf="dementia_df.csv", sep=",", index=True) # CSV file
```

#### Output file

<center><img src="io/index_csv.png" width="600"></img></center>

```python
dementia_df.to_excel( # Excel file
    excel_writer="dementia_df.xslx",
    sheet_name='Main Data',
    index=False)
```

Notes: To save a DataFrame into the CSV file we can use `.to_csv()` method. Note that `index` argument is responsible for saving the DataFrame index as a first column in the output file. If you don't want to save indexes, set `index=False`.

To save into the Excel file `.to_excel()` method can be used, where we can also specify the sheet name.

---

#  Let's code!
