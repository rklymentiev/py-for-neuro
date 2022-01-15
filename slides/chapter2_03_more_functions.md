---
type: slides
---

# Improving your functions

---

# Checking the inputs

```python
def get_pi(circumference, diameter, digits_to_round=2):
    pi = circumference/diameter
    return round(pi, digits_to_round)


print(get_pi(circumference=22, diameter=7))
```
```out
3.14
```
```python
# use a string as an function input
print(get_pi(circumference=22, diameter="some number"))
```
```out
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

Notes: Recall the function to calculate the pi value. This was a pretty simple function and we know that we should use numeric objects for an input. But what if you decide to pass a string for example as a diameter value? In such case you get an Error since operation `22/"some number"` is not supported (and doesn't make so much sense either). There is a way to check your values using `assert` statement.

---

# `assert` statement

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

Notes: `assert` works somewhat similar to `if` statement. We check a condition. If it's `True` nothing happens and function executes according to the script. If the condition if `False`, then you get an `AssertionError` with the message you specified and function **is not** executed.

You might wonder, why do we need to bother with this if we still got an error at the end? Imagine you have more sophisticated function with dozens of code lines and you have one input object that is used at the very end of the function. You wouldn't want to wait for the very end of the function execution to realize that you used a wrong input value, right? Life would be so much easier, if you knew it from the beginning and didn't execute your function until you provide appropriate input values.

Note that the `\` symbol is used for splitting the line in the assert statement for visual purpose. You don't have to use it if your line is not that long.

---

# Helping other to understand your function

```python
def get_pi(circumference, diameter, digits_to_round=2):
    """ Function returns pi value based on the circumference and diameter values of a circle.

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
        resulting pi value. """

    assert type(circumference) in [int, float], "Check the type of the circumference argument."
    assert type(diameter) in [int, float], "Check the type of the diameter argument."
    assert type(digits_to_round) == int, "Check the type of the digits_to_round argument."

    pi = circumference/diameter
    return round(pi, digits_to_round)
```

Notes: What if you publish your function or send it to someone so that can use it? Usually, people don't want to read all the code inside the function to understand how to use it. So it's nice to provide a brief documentation (a doc-string) along with your function. You can see example on the left. You start right after the function header and use a string (``"""this is still a string"""``) to write down some short explanations on how to use this function and what are the inputs/outputs. Although there are several ways of docsctring formats, you are free to write whatever you want.

You can earn more about docstring formats [here](http://daouzli.com/blog/docstring.html).

---

# Let's code!
