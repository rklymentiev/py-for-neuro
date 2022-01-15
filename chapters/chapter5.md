---
title: 'Chapter 5: I/O'
description:
  "Now that we know how to work with data it's time to learn how to actually import the data from external sources and files into Python. We will see how to load files of different formats, such as txt, csv, mat, and how to create API requests."
prev: /chapter4
next: /chapter6
type: chapter
id: 5
---

<exercise id="1" title="Working with text files" type="slides">

<slides source="chapter5_01_text_files">
</slides>

</exercise>

<exercise id="2" title="Text files I/O">

**Exercise 1**.

1. `w`rite the string to a txt file
2. `a`ppend the file to add another string. **Note!** If you use method `"w"` instead of `"a"` the new string will **overwrite** the existing data in the file. So be careful when trying to add something to the file.
3. `r`ead in the file (you have to specify the appropriate method)

<codeblock id="05_01">

* everything you need is in the exercise description;

</codeblock>

**Exercise 2**. Now imagine that we want to save a list, not a string. This becomes a bit tricky. We want to save a txt file with each value from the list on the new line. This can be possible by writing each value separately in a `for` loop and adding a `"\n"` string to each value, which is responsible for creating a new line in the file.

<center><img src="io/txt.png"></img></center>

However, now if we read the file back into the Python using `read()` method it will save the result as a string, which will look like this:
```out
"malignant\nmalignant\nbenign\nmalignant\nmalignant\nbenign\nbenign\nbenign"
```

And that is clearly not the way we would like to see it. We can use `.readlines()` method which will return the list with the strings from each file line. The only problem that all values have the new line sign `"\n"` at the end (`['malignant\n', 'malignant\n', 'benign\n', 'malignant\n', 'malignant\n', 'benign\n', 'benign\n', 'benign\n']`). Can you fix it?



<codeblock id="05_02">

* you can remove `"\n"` parts from the string by replacing it by the empty string `""`;
* remember `lambda` functions?

</codeblock>

</exercise>

<exercise id="3" title="Working with CSV and Excel files" type="slides">

<slides source="chapter5_02_csv_files">
</slides>
</exercise>

<exercise id="4" title="CSV & Excel files I/O">

**Question**. Despite the name of file extension .csv which stands for Comma-Separated Values, you can use any delimiter you wish (like ';' or tabs).

<choice id="1">

<opt text="True" correct="true">
You can use literally any separator for a CSV file. But it's always a good idea to keep it as comma.
</opt>

<opt text="False">
Even though it's not very common, you *can* use any delimiter.
</opt>
</choice>

### Exercise. fMRI data set

1. Load in the data from fMRI experiment. Path to file `"exercises/data/fmri_data.csv"`. Note that columns in a file are separated by `;`.
2. Create a new DataFrame `parietal_df` with observations from the parietal region (`df["region"] == "parietal"`);
3. Save the resulting DataFrame as an Excel file.

<codeblock id="05_03">

* you can changes the separating character by adding `sep` argument into the reading function;
* to save the file you can use `.to_excel()` method

</codeblock>

</exercise>

<exercise id="5" title="Working with MATLAB fles">

<center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Matlab_Logo.png/800px-Matlab_Logo.png" width="300"></img></center>

MATLAB is a proprietary multi-paradigm programming language and numeric computing environment developed by MathWorks. MATLAB allows matrix manipulations, plotting of functions and data, implementation of algorithms, creation of user interfaces, and interfacing with programs written in other languages.

MAT-files are binary MATLAB files that store workspace variables.

We can load MAT files into Python with the help of SciPy package. We are interested in [`loadmat()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html) function inside the `io` module.

```python
from scipy.io import loadmat
h1_data = loadmat(file_name="H1_neuron.mat", squeeze_me=True)
h1_data
```

```out
{'__globals__': [],
 '__header__': b'MATLAB 5.0 MAT-file, Platform: LNX86, Created on: Thu Feb 15 15:13:45 2001',
 '__version__': '1.0',
 'rho': array([0, 0, 0, ..., 0, 0, 0], dtype=uint8),
 'stim': array([-111.94824219,  -81.80664062,   10.21972656, ...,    9.78515625,
          24.11132812,   50.25390625])}
```

The `squeeze_me` is responsible for squeezing unit matrix dimensions. For example, if MATLAB variable was stored in a shape (5,1,1), setting `squeeze_me=True` will import it with the shape (5,) to Python.

The resulting object is a dictionary. Each key represents a saved variable from MATLAB. Also, there are three additional keys with the file info. `rho` is a vector that gives the sequence of spiking events or nonevents at the sampled times (every 2 ms). When an element of `rho` is one, this indicates the presence of a spike at the corresponding time, whereas a zero value indicates no spike. The variable `stim` gives the sequence of stimulus values at the sampled times.

[MATLAB Website](https://www.mathworks.com/products/matlab.html) || [SciPy Website](https://www.scipy.org/)

#### Exercise. H1 neuron's firing rate

1. Load in the MAT-file `H1_neuron.mat` that holds data from a fly H1 neuron response to an approximate white-noise visual motion stimulus. Path to the file: `"exercises/data/H1_neuron.mat"`;
2. Make a plot of a stimulus values (line plot) and add vertical lines for those time points when the spike occurred. Use only first 250 observations for this plot for simplicity.

<codeblock id="05_04">

* recall slicing `new_obj = old_obj[<start index>:<end index>]`;
* time points are just a range of values from 0 to `n`;
* to select only those time points when spike occurred you can use conditioning on `spikes` array;
* [`plt.vlines()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html) trick here is to add an array with desired time points. Lower and upper ends are just two values for line positioning. Why don't use minimum and maximum values of a stimulus, so  the vertical lines take over the whole height?

</codeblock>

</exercise>

<exercise id="6" title="Working with JSON files">

**JSON** (**JavaScript Object Notation**) is an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value). It is a very common data format, with a diverse range of applications.

Credits: [Wikipedia](https://en.wikipedia.org/wiki/JSON)

JSON files are useful for parameters specification. For example, all data sets on the [OpenNeuro website](https://openneuro.org/) have a JSON file with the description. Example of such file from Pavlov, Y. G., & Kotchoubey, B. (2021) data:

<center><img src="io/json.png"></img></center>

The structure of the file is always in a "key-value" format. For this example, we have data set parameters such as name, authors, and version. The values can be strings, lists, or another nested key-value object.

To read/write JSON files in Python we use `json` package, but the whole procedure is pretty the same as for working with text files. JSON files are loaded as a dictionary into Python.

```python
import json
```

#### To read JSON file:

```python
with open(file="path/to/the/file.json", mode="r") as file:
    output = json.load(fp=file)
```

#### To write JSON file:

```python
with open(file="path/to/the/file.json", mode="w") as file:
    json.dump(obj=<object to write>, fp=file)
```

[JSON Package Documentation](https://docs.python.org/3/library/json.html)

#### Exercise

1. Save a dictionary as a JSON file `"dataset_description.json"`.
2. Read in the file you just saved.
3. Save the name of the first author to a variable `first_author_name` by reaching to it through the `output` variable (do not just type it in).

Keep in mind that in this example value of the `Authors` key is a list with two dictionaries.

<codeblock id="05_05">

* you can reach to lower "layers" by specifying the keys of nested dictionaries or indexes of a nested lists, for example `<dict>["key1"]["key2"][<index of a list>]`

</codeblock>

</exercise>

<exercise id="7" title="API requests" type="slides">

<slides source="chapter5_03_api">
</slides>

</exercise>

<exercise id="8" title="API requests practice">

### Exercise 1. Open APIs From Space

**Open Notify** is an open-source project to provide a simple programming interface for some of NASA’s awesome data. I do some of the work to take raw data and turn them into APIs related to space and spacecraft.

[Open Notify Website](http://open-notify.org/)

There is an API that allows getting the number of people in space at the moment: [How Many People Are In Space Right Now](http://open-notify.org/Open-Notify-API/People-In-Space/). There is no authentication for this API, so we don't need any keys. Also, according to the documentation, we cannot specify any additional parameters.

API URL: `http://api.open-notify.org/astros.json`

<codeblock id="05_07">

* resulting dictionary has a key `"people"` with the list as a value. Each value from a list is a dictionary with two keys: `"craft"` and `"name"`

</codeblock>


### Exercise 2. Allen Brain Map

**The Allen Institute for Brain Science** uses a unique approach to generate data, tools and knowledge for researchers to explore the biological complexity of the mammalian brain. This portal provides access to high quality data and web-based applications created for the benefit of the global research community.

[Website](https://portal.brain-map.org/)

[Image download API](http://help.brain-map.org/display/api/Downloading+an+Image#DownloadinganImage-ImageDownloadService) serves whole and partial two-dimensional images presented on the Allen Brain Atlas Web site. Some images can be downloaded with expression or projection data. Glioblastoma images' color block and boundary data can also be downloaded.

API URL: `http://api.brain-map.org/api/v2/image_download/[SubImage.id]`

This API returns an image, not a JSON/XML file and can take several parameters, for example:

* `quality`: *integer*, the jpeg quality of the returned image. This must be an integer from 0, for the lowest quality, up to as high as 100.
* `downsample`: *integer*, number of times to downsample the original image. For example, `downsample=1` halves the number of pixels of the original image both horizontally and vertically.
* `width`: *integer*, number of columns in the output image, specified in tier-resolution (desired tier) pixel coordinates.
* `height`: *integer*, number of rows in the output image, specified in tier-resolution (desired tier) pixel coordinates.

Your task is to:

1. Get the image for the subject ID `69750516`.
2. Update the parameters of request: set the quality to 50%, set downsample to 2, the resulting image should have the size `(5000, 5000)`
3. Print the status code and plot the resulting image.

<codeblock id="05_08">

* note that API requires subject ID in the URL;

</codeblock>

</exercise>

<exercise id="9" title="Working with pickled files">

Imagine that you want to share a dictionary with your co-worker. When the dictionary is relatively "simple" you can just copy and paste it values into the chat or email. But what if your dictionary holds an array from EEG experiment with the shape `(64,1000,100)`. That's a lot of observations to copy. In such a case sharing an object as a **pickled** file might become helpful.

The `pickle` module implements binary protocols for serializing and de-serializing a Python object structure. "Pickling" is the process whereby a Python object hierarchy is converted into a byte stream, and "unpickling" is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as "serialization", "marshalling", or "flattening"; however, to avoid confusion, the terms used here are "pickling" and "unpickling".

Credits: [Python documentation](https://docs.python.org/3/library/pickle.html)

To put it in simple words: you can save mostly **any** Python in a pickle file for sharing or later use. However, there are some big disadvantages of pickled files:

1. **The pickle module is NOT secure**. Only unpickle data you trust.
2. It is Python-only: pickles cannot be loaded in any other programming language (unlike JSON files).

To read/write pickle files in Python we use `pickle` package.

```python
import pickle
```

#### To read pickle file:

```python
with open(file="path/to/the/file.pickle", mode="rb") as file:
    output = pickle.load(file=file)
```

#### To write pickle file:

```python
with open(file="path/to/the/file.pickle", mode="wb") as file:
    pickle.dump(obj=<object to write>, file=file)
```

Note the pickle files are binary, that's why we are using binary modes for writing and reading.

#### Exercise

1. Load in the dataset with fMRI data (`"exercises/data/fmri_data.csv"`). CSV file is separated by ";".
2. Create a new dictionary `frmi` with two keys: `"parietal"` that holds a DataFrame with observations only from the parietal region and `"frontal"` that holds a DataFrame with observations only from the frontal region.
3. Save the resulting dictionary to the pickle file `"frmi_dict.pickle"`.
4. Read in back the resulting pickle file and print the first 5 rows of each of the DataFrames in a dictionary.

<codeblock id="05_06">

* remember that pickle files are binary

</codeblock>

</exercise>

<exercise id="10" title="Finding local files">

Sometimes it can be useful to find files through Python. For example, you want to make sure that CSV file exists in a current directory you are in. You want to make some changes in the file and then save resulting file in a new folder. Of course, you can manually copy-paste the file into the directory and create a folder by hand. But also there is a way to do this in Python using `os` module (Miscellaneous operating system interfaces).

[Documentation](https://docs.python.org/3/library/os.html)

Some useful functions:

* `os.getcwd()` - get the current working directory (folder);
* `os.chdir(path)` - change directory;
* `os.listdir(path=".")` - return the content of a directory. If `path` is not specified, returns the content of current working directory;
* `os.mkdir(path)` - create a new directory();
* `os.rmdir(path)` - remove a directory;
* `os.remove(path)` - remove a file;
* `os.path.join(dirpath, name)` -  extend the path to the directory/file.

### Exercise

1. Get the current working directory and save it to a variable `cwd` (this will be a string).
2. Extend the current path (`cwd`) with `path_to_data` (the directory where all the data sets for the course are).
3. Change the CWD to the `new_cwd`.
4. Get the file names of a CWD and save it to the variable `fnames`.
5. Calculate how many CSV files are there in CWD save that count number to the variable `n_csv`.

<codeblock id="05_09">

* all the `os` functions needed are above;
* what does CSV file name `.endswith()`?

</codeblock>

Further reading:

* [OS Module in Python with Examples](https://www.geeksforgeeks.org/os-module-python-examples/)

</exercise>

<exercise id="11" title="Final check">

**Question 1**. You can store any Python object (dictionary, set, numpy array, etc.) as a pickle file on a disk so it can be used later without any information loss.

<choice id="1">

<opt text="True" correct="true">
</opt>

<opt text="False">
</opt>
</choice>

**Question 2**. Which function from the `os` package let you see the content of the current working directory?

<choice id="2">

<opt text="os.pwd()">
This function prints the working directory.
</opt>

<opt text="os.listdir()" correct="true">
This function will return a list of files in a specified folder.
</opt>

<opt text="os.printdir()">
This function doesn't even exist.
</opt>

<opt text="os.mkdir()">
This function creates a new folder.
</opt>
</choice>

**Question 3**. You have loaded a JSON file as a dictionary `sample_json` to the working space.

```python
{
    'quiz': {
        'maths': {
            'q1': {
                'answer': '12',
                'options': ['10', '11', '12', '13'],
                'question': '5 + 7 = ?'
            },
            'q2': {
                'answer': '4',
                'options': ['1', '2', '3', '4'],
                'question': '12 - 8 = ?'
            }
        },
        'sport': {
            'q1': {
                'answer': 'Huston Rocket',
                'options': ['New York Bulls', 'Los Angeles Kings',
                            'Golden State Warriros', 'Huston Rocket'],
                'question': 'Which one is correct team name in NBA?'
            }
        }
    }
}
```

What is the output of the following command?

```python
sample_json['sport']['q1']['options']
```
<choice id="3">
<opt text="['New York Bulls', 'Los Angeles Kings', 'Golden State Warriros', 'Huston Rocket']">
Check the keys hierarchy. Aren't we missing something?
</opt>

<opt text="{'sport': {'q1': {'options': ['New York Bulls', 'Los Angeles Kings', 'Golden State Warriros', 'Huston Rocket']}}}" >
Hm...
</opt>

<opt text="New York Bulls">
That would be the true if specified the index of a list at the end. But something else is also missing.
</opt>

<opt text="Key Error" correct="true">
"quiz" key is missing. The correct command would be `sample_json['quiz']['sport']['q1']['options']`
</opt>
</choice>


</exercise>
