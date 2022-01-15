---
type: slides
---

# Working with files

---

# Text files

You can access text file in Python with the help of built-in `open()` function. `mode` options are:

* `r`: Opens the file in read-only mode. Starts reading from the beginning of the file and is the default mode for the open() function.
* `rb`: Opens the file as read-only in binary format and starts reading from the beginning of the file. While binary format can be used for different purposes, it is usually used when dealing with things like images, videos, etc.
* `r+`: Opens a file for reading and writing, placing the pointer at the beginning of the file.
* `w`: Opens in write-only mode. The pointer is placed at the beginning of the file and this will overwrite any existing file with the same name. It will create a new file if one with the same name doesn't exist.
* `wb`: Opens a write-only file in binary mode.
* `w+`: Opens a file for writing and reading.
* `wb+`: Opens a file for writing and reading in binary mode.
* `a`: Opens a file for appending new information to it. The pointer is placed at the end of the file. A new file is created if one with the same name doesn't exist.
* `ab`: Opens a file for appending in binary mode.
* `a+`: Opens a file for both appending and reading.
* `ab+`: Opens a file for both appending and reading in binary mode.

Notes: It happens more often than we wish it to happen, but from time to time we still have to deal with .txt files, so we need to know how to import them. We can do this with the help of `open()` function. Here comes the trick that you should specify in what `mode` do you want to open the file. There are a lot of different options, but they are all kind of intuitive:

* `w`: Writing the file
* `a`: Appending the file
* `r`: Reading the file

---

# Writing a file

```python
my_string = "Hello, Python!"

with open("new_file.txt", mode="w") as file:
    file.write(my_string)
```

### Output file:

<img src="io/hello_txt.png"></img>

Notes: Without going into much details, we are using the `with` command here to prevent the open connection to the file. You can think of it as a `while` statement: "while we are opening the file and saving the resulting I/O object to the variable `file` we are `write`ing the file. When the `file.write()` is done we close the connection to the file".

Note that if file with such name doesn't exist, Python will create it. If file exists already, then Python will **overwrite** the existing data in the file with the new data. If you don't want to erase the data, but rather add new lines to the file, you should use append mode.

---

# Adding data to the file

```python
my_string = " How are you doing today, Python?"

with open("new_file.txt", mode="a") as file:
    file.write(my_string)
```

### Output file:

<img src="io/hello_txt2.png"></img>

Notes: To **add** new text into the file we use append mode (`mode='a'`). In this case Python will add new string to the very end of the file. The only thing that has changed here is the `mode`, we are still using the `.write()` method.

---

# Reading the file (1)

#### Input file:

<img src="io/hello_txt2.png"></img>

```python
with open("new_file.txt", mode="r") as file:
    output = file.read()

print(output)
```
```out
Hello, Python! How are you doing today, Python?
```

Notes: To read the file in we use `mode='r'` and `read()` method. Remember to assign the result to the new variable to save the resulting string.

---

# Reading the file (2)

### Input file:

<img src="io/hello_txt3.png"></img>

```python
with open("new_file.txt", mode="r") as file:
    output = file.readlines()

print(output)
```
```out
['id011\n', 'id225\n', 'id331\n', 'id410\n', 'id597\n', 'id109\n']
```

Notes: It happens quite often that we have data in the text file separated by new lines (for example IDs of subjects). To read this type of file we can use `readlines()` method.

---

#  Let's code!
