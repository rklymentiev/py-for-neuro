---
type: slides
---

# "Everything is an Object"

Notes: > "Everything in Python is an object". If you haven't heard this phrase already, you would probably hear it eventually anyway. It can make a little sense, when you don't know much about programming. You can think of it in a way that **everything** you create in Python is going to be an object of a specific type. Integer `5` is an object, function `sum()` is an object, even the imported Excel sheet to a `pandas` DataFrame is also an object.

---

# Say goodbye to the calculator

You can use Python as a calculator to perform math calculations of any type (and no-one will judge you for that):

```python
2+2*2
```

```out
6
```

Notes: Guess what is `2`? Correct, that's an object of type `int` (integer) with some unique id (which you don't need to worry about). Guess what is the resulted `6`? Also correct, that's another object of `int` type!

You will see later that each object type has its own properties and lots of possibilities to perform cool stuff with them.

Another big note here is that math operations order in Python is the same as we think of it "in real life". Thus, the result is `6` and not `8`.

---

# Saving your objects

Save the result of a calculation:
```python
x = 2+2*2
print(x)
print(type(x))
```

```out
6
int
```

Use it later:

```python
y = x-10
print(y)
```

```out
-4
```

Notes: Most of the times you will perform more complex tasks in Python than `2*2` and you want to save your objects for the later usage. For example, you calculated the average values of some parameter among control and treatment group and you want to use these values to perform statistical test.

The say way you do this in math, you do it in Python. `x = 5` means that you create a new variable called `x` that will hold an object `5`. Names of the variables are arbitrary, but should be meaningful though for readability of the code. We will get to this later.

You can go bigger, and assign not just one object to a new variable `x`, but the result of some operations. `x` variable will stay in the memory (Python memory, not talking about the hippocampus here) as long as you don't delete it, so you can use it later.

---

# Built-in types

You have seen `int` type already. Here are some more:

```python
var = 5.5
print(type(var))
```

```out
float
```

```python
var = "Hello, Neuroscience"
print(type(var))
```

```out
str
```

```python
var = True
print(type(var))
```

```out
bool
```

Notes: Python has some built-in types which you can see on this slide, but there are lots and lots more. As told before, each type has its own specific functions that can be applied to it.

---

# Some of the cool stuff you can do with numbers

Built-in numeric operations are:

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

Notes: Most of the numeric operations are pretty straight-forward. However there are some surprises like `2^2`, which is **not** 2 to the power of 2. 

---

# Let's code!
