---
type: slides
---

# "Everything is an Object"

Notes: > "Everything in Python is an object". If you haven't heard this phrase already, you would probably hear it eventually anyway. It can make a little sense when you don't know much about programming. You can think of it in a way that **everything** you create in Python is going to be an object of a specific type. Integer `5` is an object, function `sum()` is an object, even the imported Excel sheet is also an object.

---

# Say goodbye to the calculator

You can use Python only as a calculator to perform math calculations of any type (and no-one will judge you for that):

```python
2+2*2
```

```out
6
```

Notes: Guess what is the type of `2`? Correct, that's an object of type `int` (integer) with some unique id (which you don't need to worry about). Guess what is the resulting `6` in the example on the left? Yes, that's another object of `int` type!

You will see later that each object type has its own properties and functions.

Another big note here is that math operations order in Python is the same as we think of it "in a real-life". Thus, the result is `6` and not `8`.

---

# Saving your objects

Save the result of a calculation:
```python
x = 2 + 2*2
print(x)
print(type(x))
```

```out
6
int
```

Use it later:

```python
y = x - 10
print(y)
```

```out
-4
```

Notes: Most of the times you will perform more complex tasks in Python than just `2*2` and you will want to save your resulting objects for the later usage. For example, imagine calculating the average values of some parameter among control and treatment groups and using these values to perform statistical test.

In the same way you do this in math, you do it in Python. `x = 5` means that you create a new variable called `x` that will hold an object `5`. Names of the variables are arbitrary, but should be meaningful for the code readability. We will get to the part of code style guidelines a bit later.

You can go bigger, and assign not just one object to a new variable `x`, but the result of an operation. `x` variable will stay in the memory (Python memory, not talking about the hippocampus here) as long as you don't delete it, so you can use it later.

---

# Built-in types

You have seen `int` type already. Here are some more:

```python
var = 5.5 # floating point number
print(type(var))
```

```out
float
```

```python
var = "Hello, Neuroscience" # string
print(type(var))
```

```out
str
```

```python
var = True # boolean
print(type(var))
```

```out
bool
```

Notes: Python has some built-in types, which you can see on this slide, but there are lots and lots more. As told before, each type has its own specific functions that can be applied to it and will go through them as we learn.

---

# Some of the cool stuff you can do with numbers

| Operation | Note |
|:-:|:-:|
| `x + y` | sum of `x` and `y` |
| `x - y` | difference of `x` and `y` |
| `x * y` | product of `x` and `y` |
| `x / y` | quotient of `x` and `y` |
| `x // y` | floored quotient of `x` and `y` |
| `x % y` | remainder of `x` / `y` |
| `-x` | `x` negated |
| `+x` | `x` unchanged |
| `abs(x)` | absolute value or magnitude of `x` |
| `pow(x, y)` | `x` to the power `y` |
| `x ** y` | `x` to the power `y` |

Notes: Most of the numeric operations are pretty straight-forward. However there are some surprises like `2^2`, which **is not** 2 to the power of 2.

---

# Let's code!
