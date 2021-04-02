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

**Exercise 1**. Given a string `my_sting` count all word characters, digits, and special symbols.

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

<exercise id="6" title="Improving functions" type="slides">

<slides source="chapter2_03_more_functions">
</slides>

</exercise>

<exercise id="7" title="Functions practice (3): assert and docstring">

**Exercise 5**. Remember the `variance()` function you created recently? What if input list holds any non-numeric object? In this case function will also fail. Check that **all** the values in the input lists are numeric (`int` or `float`) using `assert` statement.

Also, degrees of freedom should be a positive integer or 0. Raise an error if that's not true.

<codeblock id="02_08">

- one of the ways to do this is by help of `map()` and `lambda()` functions. You can check that type of each value in a list is either `int` or `float` by calling `in` operator in `lambda()`\'s expression.
- `sum([True, False, True])` equals 2, since `True` = 1, `False` = 0;
- if sum (or we can call it count) of numeric values in a list doesn't equal the length of a list, what does it tell us?

</codeblock>

**Exercise 6**. Update the function with a dosctring, so other users can understand what this function is about.

<codeblock id="02_09">

- you are free to write anything you want inside the docstring. But keep in short and informative!

</codeblock>

</exercise>

<exercise id="8" title="Code style guidelines" type="slides">

<slides source="chapter2_04_pep8">
</slides>

</exercise>
