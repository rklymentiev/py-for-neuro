---
type: slides
---

# Writing custom functions

Notes: A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

---

# Functions

#### General form:
```python
def my_new_function(some_argument1, some_argument2):
    do something
    return something
```
#### Example:
```python
def mean(input_list):
    nominator = sum(input_list)
    denominator = len(input_list)
    return nominator/denominator


l = [1,2,3,4,5]
print(mean(input_list=l))
```
```out
3.0
```
Notes: You have seen the examples of several built-in functions like `len()`, `max()`, `sorted()`, etc. These functions allow you to perform some desired calculations. But what if you want to make sophisticated calculations and there is no function for this? For example, you want to take an average value from the list. There is no built-in function for that, but you can create it yourself.

In the `mean()` function (again, the name of the function is your choice, but try to keep it meaningful) we specified that there is going to be just one argument (`input_list`). That will hold the value of an object we pass to the function when we call it.

In the function's body, we create two new variables that hold the values of sum and length. And at the end, we return the value of a division. The last step is very important since now `mean()` function returns an object, that could be passed to a variable and used later. Try creating a function without the `return` statement on your own and see what happens.

---

# Arguments of the function

```python
def get_pi():
    pi = 22/7
    return pi

print(get_pi())
```
```out
3.142857142857143
```

```python
def get_pi(circumference, diameter, digits_to_round=2):
    pi = circumference/diameter
    return round(pi, digits_to_round)

print(get_pi(circumference=22, diameter=7))
print(get_pi(circumference=22, diameter=7, digits_to_round=1))
```
```out
3.14
3.1
```

Notes: Functions can take no input arguments, like in the `get_pi()` example. In such a case, the result of the function will be always the same.

You can specify as many input arguments as you wish. Also, arguments can have default values (like `digits_to_round=2`). This means that if you don't specify its value in the function run, it will be taken from the default value.

`digits_to_round` was used inside the `round()` function and specified the numbers we want to keep after the coma. In the first run, we didn't specify `digits_to_round`, so it was set to `2`. In the first run, we set it to `1` in the function call.

---

# `map` and `filter` functions

#### General form:
```python
map(function, iterable_object)
filter(function, iterable_object)
```
#### Examples:
```python
def squared(x):
    return x**2

stdev = [2, 4, 1.5, 2, 4]
list(map(squared, stdev))
```
```out
[4, 16, 2.25, 4, 16]
```

```python
def greater_than_two(x):
    return x > 1

list(filter(greater_than_two, stdev))
```
```out
[4, 4]
```

Notes: `map()` function is used to apply a function on all the elements of specified iterable object and to return map object. Python map object is an iterator, so we can iterate over its elements. We can also convert a map object to a sequence object such as list, tuple etc.

In the first example, we applied function `squared` to **every** object from the list `stdev` and converted the result to a list.

The `filter()` function constructs an iterator from elements of an iterable for which a function returns true. In simple words, the `filter()` function filters the given iterable object with the help of a function that tests each element in the iterable to be true or not.

In the example we applied function `greater_than_two()` to **every** object from the list `stdev`. `greater_than_two()` returns `True` of `False` values and `filter()` filters out all the variables that have `False` response.
---

# `lambda` function

A `lambda` function is a small anonymous function. It can take any number of arguments, but can only have one expression.

#### General form:
```python
lambda arguments: expression
```
#### Examples:
```python
stdev = [2, 4, 1.5, 2, 4]
list(map(lambda x: x**2, stdev))
```
```out
[4, 16, 2.25, 4, 16]
```

```python
list(filter(lambda x: x>2, stdev))
```
```out
[4, 4]
```
Notes: On the previous slide, we created two new functions `squared()` and `greater_than_two()` that we used only once and will not need them later at all. This might look like not a big deal for now, but imagine you have 100 of such "temporary" functions that do its own one-time task. This can result in unnecessary memory usage. We can fix this with the help of `lambda` functions.

In the first example, we created a `lambda` function that takes `x` as an input and returns `x**2`. If you compare it to `square` function, you can notice that they are basically the same, but `lambda` function has no name and you cannot access it later since it's not saved in the environment.

In the second example, we created a `lambda` function that takes `x` as an input and returns the result of a comparison `x>2`.

---

# Let's code!
