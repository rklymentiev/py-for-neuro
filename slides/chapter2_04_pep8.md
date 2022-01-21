---
type: slides
---

# Code style guidelines

Notes: It's important to keep your code "organized" so it is easy for other people in your team to go through it. The most common guide for Python code style guidelines is **PEP 8**. Here we will look at some points on how to make your code readable. If you want to learn more, check out these links:

* [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Blog post on [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)

---

# Naming Conventions

| Type | Naming Convention | Examples |
|:--|:--|:--|
| Function | Use a lowercase word or words. Separate words by underscores to improve readability. | `function`, `my_function` |
| Variable | Use a lowercase single letter, word, or words. Separate words with underscores to improve readability. | `x`, `var`, `my_variable` |
| Class | Start each word with a capital letter. Do not separate words with underscores. This style is called camel case. | `Model`, `MyClass` |
| Method | Use a lowercase word or words. Separate words with underscores to improve readability. | `class_method`, `method` |
| Constant | Use an uppercase single letter, word, or words. Separate words with underscores to improve readability. | `CONSTANT`, `MY_CONSTANT`, `MY_LONG_CONSTANT` |
| Module | Use a short, lowercase word or words. Separate words with underscores to improve readability. | `module.py`, `my_module.py` |
| Package | Use a short, lowercase word or words. Do not separate words with underscores. | `package`, `mypackage` |

Notes: Here you see the recommendations on how to call the variables in your Python code. For example, if you see a variable named `IMG_SIZE` in someone's code you can assume that it refers to some constant value (like the size of images you want to load into array), but not the function.

---

# Names should be meaningful

<center><img src="imgs/names_meme.jpg" width="400"></center>

Notes: There is nothing wrong with calling your variables `test`, `x`, or `my_func` when performing some quick task, but try to keep names as clear as possible when you are working on a code for a broader audience (after several days even you probably will not remember the purpose of the functions you created). If you saw a function `get_average_size()` in someone's code, you could assume that it has to do something with array size. But what could `function_version_1_test_fixed()` function do?

---

# Maximum line length

```python
from mypkg import example1, \
    example2, example3
```

#### Example of breaking before a binary operator:
```python
# recommended
total = (first_variable
         + second_variable
         - third_variable)

# not recommended
total = (first_variable +
         second_variable -
         third_variable)
```

Notes: PEP 8 suggests lines should be limited to **79 characters**. If it is impossible to use implied continuation, then you can use backslashes to break lines instead.

---

# Indentations (1)

#### Not recommended
```python
# arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

#### Recommended
```python
# aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

Notes: The indentation level of lines of code in Python determines how statements are grouped together. Use 4 spaces per indentation level.

Continuation lines should align wrapped elements either vertically using Python's implicit line joining inside parentheses, brackets and braces, or using a hanging indent. When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line.

---

# Indentations (2)

#### Recommended
```python
# hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

my_list = [
    1, 2, 3,
    4, 5, 6
    ]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f'
    )
```

Notes: The closing brace/bracket/parenthesis on multiline constructs may either line up under the first non-whitespace character of the last line of list.

**Spaces** are the preferred indentation method. Tabs should be used solely to remain consistent with code that is already indented with tabs. Python 3 disallows mixing the use of tabs and spaces for indentation.

---

# Whitespace around binary operators (1)

```python
# recommended
y = x**2 + 5
z = (x+y) * (x-y)

# not recommended
y = x ** 2 + 5
z = (x + y) * (x - y)
```


#### However:
```python
# recommended
def function(default_parameter=5):
    pass

# not recommended
def function(default_parameter = 5):
    pass
```


Notes: Surround the following binary operators with a single space on either side:

* Assignment operators (`=`, `+=`, `-=`, and so forth)
* Comparisons (`==`, `!=`, `>`, `<`. `>=`, `<=`) and (`is`, `is not`, `in`, `not in`)
* Booleans (`and`, `not`, `or`)

---

# Whitespace around binary operators (2)

```python
# recommended
if x>5 and x%2 == 0:
    print('x is larger than 5 and divisible by 2!')

# not recommended
if x > 5 and x % 2 == 0:
    print('x is larger than 5 and divisible by 2!')

# definitely do not do this!
if x >5 and x% 2== 0:
    print('x is larger than 5 and divisible by 2!')
```

Notes: Keep in mind, that most of the recommendations described in this presentation don't affect the performance of your code. Or in other words, your code will still run as supposed to, but by following PEP-8 guidelines you make your code more friendly for other people.  

---

# This is it for now!
