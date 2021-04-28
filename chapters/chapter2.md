---
title: 'Chapter 2: Programming Fundamentals'
description:
  'In this chapter we are going to look at programming concepts, such as working with loops, writing custom functions and dealing with errors.'
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="Automating the routine" type="slides">

<slides source="chapter2_01_loops">
</slides>

</exercise>

<exercise id="2" title="Time to practice">

**Exercise 1**. Given a string `my_sting` count all word characters, digits, and special symbols in it. For example, string `"h336^"` has 1 word character, 3 digits and 1 special symbol.

<codeblock id="02_01">

- there are the methods to check whether consist of alphabetical symbols (`.isalpha()`) or numeric symbols (`.isnumeric()`). Whatever is left must be a symbol;
- you might want to set the counter initially to zero and then increase by 1 when the appropriate condition is met in the `for` loop;
- you cn also use the `+=` trick;

</codeblock>

**Exercise 2**. Write a code to get the Fibonacci series. The Fibonacci Sequence is the series of numbers: `0, 1, 1, 2, 3, 5, 8, 13, 21, ...`. Every next number is found by adding up the two numbers before it.

Keep just first 10 digits for simplicity.

<codeblock id="02_02">

- add a condition to check the length of the lists (you want the final list to be of length 10);
- you can take last `n` values from the list by indexing `[-n:]`.

</codeblock>

**Exercise 3**. You performed a learning task and got accuracy (number of correct trials divided by total number of trials) for 10 subjects stored in a dictionary. Which 3 subjects performed the best?

<codeblock id="02_03">

- you can use the function `sorted(list_object, reverse=True)` to sort the list in descending order and cut the first `n` observations with the help of slicing `[:n]`;

</codeblock>

</exercise>

<exercise id="3" title="Writing custom functions" type="slides">

<slides source="chapter2_02_functions">
</slides>

</exercise>

<exercise id="4" title="Functions practice (1): custom functions">

**Question 1**. Keep in mind that if your function holds non-default and default arguments at the time, you have to place **all** the default arguments at the end in the function header (`def function_name(arguments)`) after the non-default arguments. Given that, which of the function headers you think is **incorrect**?

<choice>
<opt text="def func(a, b, c=1)">
It has one default argument `c` which stats at the end. So that's a correct header.
</opt>

<opt text="def func(a=1, b, c=1)" correct="true">
All non-default arguments should be put before default arguments. The correct header would be `def func(b, a=1, c=1)`
</opt>

<opt text="def func(a=1, b=1, c=1)">
There is nothing wrong with having all the arguments as default.
</opt>

<opt text="def func(a, b, c)">
There is nothing wrong with having all the arguments as non-default.
</opt>

</choice>

**Exercise 1**. Write a function that takes a list of numbers as an input and returns a variance of that list.

Population variance can be approximated as:

<center><img src="https://latex.codecogs.com/gif.latex?s^2&space;=&space;\frac{\sum{(x-\bar{x}})^2}{N}" title="s^2 = \frac{\sum{(x-\bar{x}})^2}{N}" /></center>

* <img src="https://latex.codecogs.com/gif.latex?\bar{x}" title="\bar{x}" /> - the average value,

* <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> - number of observations.

<codeblock id="02_04">

- *sending cheer up vibes*

</codeblock>

**Exercise 2**. When we are dealing with the **sample variance** we have to subtract 1 degree of freedom in the denominator.

<center><img src="https://latex.codecogs.com/gif.latex?s^2&space;=&space;\frac{\sum{(x-\bar{x}})^2}{N-1}" title="s^2 = \frac{\sum{(x-\bar{x}})^2}{N-1}" /></center>

Update your function by adding `df` argument that will specify how many degrees of freedom we want to subtract. Set the default value to 1 (meaning that by default it will use the formula for the sample variance).

<codeblock id="02_05">

- remember to put `df` at the end of the arguments list in the header, since it has a default value;

</codeblock>

</exercise>

<exercise id="5" title="Functions practice (2): lambda functions">

**Exercise 3**. You performed a learning task and got accuracy (number of correct trials divided by total number of trials) for 10 subjects stored in a dictionary. Now you want to save the IDs of those participants whose score was above 0.6 in a separate list. How could you solve it using `filter` and `lambda` function?

<codeblock id="02_06">

- you might want to apply `filter` function on dictionary keys and use the value of the key in a `lambda` function for a comparison;

</codeblock>

**Exercise 4**. Your experiment had 5 subjects in a control group and 5 subjects in a treatment group. However, the labels were written in a funny way. Clean the `groups` list, so values are `"control"` and `"treatment"` using `map` and `lambda` functions.

Then using `for` loop and `if` statement separate IDs into control and treatment lists.

<codeblock id="02_07">

- to clean the groups list you can remove the last two characters with the help of `.replace()` method (or slicing everything but last two values) and apply `lower()` method;
- to iterate over indexes of the list you can use the structure `for i in range(len(list_obj))`. In that case `range()` function creates a list starting at 0 and ending at the value `n-1`, where `n` is the length of the given list;

</codeblock>

</exercise>

<!-- <exercise id="6" title="Improving functions" type="slides">

<slides source="chapter2_03_more_functions">
</slides>

</exercise> -->

<exercise id="6" title="assert statement">

Recall the function to calculate the pi value. This was a pretty simple function and we know that we should use numeric objects for an input. But what if you decide to pass a string for example as a diameter value? In such case you get an Error, since operation `22/"some number"` is not supported (and doesn't make so much sense either).

```python
def get_pi(circumference, diameter, digits_to_round=2):
    pi = circumference/diameter
    return round(pi, digits_to_round)


# use a string as an function input
print(get_pi(circumference=22, diameter="some number"))
```
```out
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

There is a way to check your input values using `assert` statement. It works somewhat similar to `if` statement. We check a condition. If it's `True` nothing happens and function executes according to the script. If the condition if `False`, then you get an `AssertionError` with the message you specified and function **is not** executed.

#### General form:
```python
assert condition, "Message to add to an error in case the condition isn't true"
```

```python
def get_pi(circumference, diameter, digits_to_round=2):

    assert type(circumference) in [int, float], \
    "Check the type of the circumference argument. Should be numeric."
    assert type(diameter) in [int, float], \
    "Check the type of the diameter argument. Should be numeric."
    assert type(digits_to_round) == int, \
    "Check the type of the digits_to_round argument. Should be an integer."

    pi = circumference/diameter
    return round(pi, digits_to_round)


print(get_pi(circumference=22, diameter="some number"))
```
```out
AssertionError: Check the type of the diameter argument. Should be numeric.
```

You might wonder, why do we need to bother with this if we still got an error at the end? Imagine you have more sophisticated function with dozens of code lines and you have one input object that is used at the very end of the function. You wouldn't want to wait for the very end of the function execution to realize that you used a wrong input value, right? Life would be so much easier, if you knew it from the beginning and didn't execute your function until you provide appropriate input values.

Note that the `\` symbol is used for splitting the line in the assert statement for visual purpose. You don't have to use it if your line is not that long.

**Exercise**. Remember the `variance()` function you created recently? What if input list holds any non-numeric object? In this case function will also fail. Check that **all** the values in the input lists are numeric (`int` or `float`) using `assert` statement.

Also, degrees of freedom should be a positive integer or 0. Raise an error if that's not true.

<codeblock id="02_08">

- type of the `df` object should be an integer *and* it should be >= 0;
- one of the ways to do this is by help of `map()` and `lambda()` functions. You can check that type of each value in a list is either `int` or `float` by calling `in` operator in `lambda()`\'s expression.
- `sum([True, False, True])` equals 2, since `True` = 1, `False` = 0;
- if sum (or we can call it count) of numeric values in a list doesn't equal the length of a list, what does it tell us?

</codeblock>

</exercise>

<exercise id="7" title="Documenting the code using docstrings">

What if you publish your function or send it to someone so that can use it? Usually, people don't want to read all the code inside the function to understand how to use it. So it's nice to provide a brief documentation (a doc-string) along with your function. You can see example on the left. You start right after the function header and use a string (`"""this is still a string"""`) to write down some short explanations on how to use this function and what are the inputs/outputs. Although there are several ways of docsctring formats, you are free to write whatever you want.

You can earn more about docstring formats [here](http://daouzli.com/blog/docstring.html).

#### Examples:
```python
def get_pi(circumference, diameter, digits_to_round=2):
    """ Function returns pi value based on the circumference
    and diameter values of a circle.

    Parameters
    ----------
    circumference : int or float
        Circumference of the circle.
    diameter : int or float
        Diameter of the circle.
    digits_to_round : int
        Amount of digits to keep after the coma in a pi value.

    Returns
    ----------
    pi : float
        Resulted pi value. """

    assert type(circumference) in [int, float], \
    "Check the type of the circumference argument."
    assert type(diameter) in [int, float], \
    "Check the type of the diameter argument."
    assert type(digits_to_round) == int, \
    "Check the type of the digits_to_round argument."

    pi = circumference/diameter
    return round(pi, digits_to_round)
```

```python
def variance(input_list, df=1):
    """ Function returns the variance of a given lists.

    Parameters
    ----------
    input_list : list
        List of numeric values

    df : int, default is 1
        Degrees of freedom to subtract.
        When `df=0` formula is for the population variance.
        When `df=1` formula is for the sample variance.

    Returns
    ----------
    Variance: float
        Resulted variance.
    """

    # get the list of booleans that were a result of checking
    # if value from a list is either int or float
    is_type_numeric = map(lambda x: type(x) in [int, float], input_list)
    # if the sum of that list doesn't equal the length of an input list
    # that means, that one of more objects were not numeric
    assert sum(is_type_numeric) == len(input_list), \
    "Some of the values in the list are not numeric"
    assert (type(df) == int) & (df >= 0), \
    "Degrees of freedom should be a positive integer or 0"

    N = len(input_list)                # calculate the sample size
    x_bar = sum(input_list) / N        # calculate the average value

    numerator = []                     # empty list with the values from the numerator
    for x in input_list:               # iterate over all values in the given list
        numerator.append((x-x_bar)**2) # subtract average value from x,
                                       # square it, and add to the numerator list
    return sum(numerator) / (N-df)     # return the sum of the numerator divided by (N - df)
```

</exercise>

<exercise id="8" title="f-strings">

Imagine you running a loop over all values of the list and at each step you want to add each value to a string (for example to print out). You can do this using so called **f-strings** in a following way: `f"{<variable name>}"` which will **dynamically** paste the value of a given variable inside the string. For example:

```python
participants = ["id1", "id6", "id8"]

for val in participants:
    print(f"{val}")
```
```out
id1
id6
id8
```

When you pass the float number as a variable inside the f-string, you can also specify additional formatting style, such as rounding, in a way `f"{<float>: .<digits>f}"`:

```python
scores = [456.1341, 478.12451, 501.2345]

for val in scores:
    print(f"{val: .2f}")
```
```out
456.13
478.12
501.23
```

<br>

**Exercise**. Given the dictionary where key is a subject ID and value is accuracy for the task, print out the sting for each participant using `for` loop in a way: `"Accuracy for subject id1 is 0.27."`. Round the accuracy to two digits after the decimal point.

<codeblock id="02_09">

- you can iterate over keys and values of the dictionary in the same time. Remember that `<dict>.items()` method returns a list `[(key, value), (key, value), ...]`;

</codeblock>

If you want to know more about f-string and other formatting methods, check out this link: [PEP 498 -- Literal String Interpolation](https://www.python.org/dev/peps/pep-0498).

</exercise>

<exercise id="9" title="Code style guidelines" type="slides">

<slides source="chapter2_04_pep8">
</slides>

</exercise>
