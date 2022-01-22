---
type: slides
---

# Automating the routine

---

# `if` statement

**General form**:
```python
if condition is True:
    do something
elif another condition is True:
    do something
else:
    do something else
```

```python
x = 100
y = 500

if x > y:
    print('X is greater than Y')
elif x == y:
    print('X equals Y')
else:
    print('X is smaller than Y')
```

```out
X is smaller that Y
```

Notes: We have looked at the comparisons in a previous chapter (like `==`, `!=` or `<`). Now we want to take some actions which will depend on the outcome of the comparison.

The form is pretty straightforward. `if` something is `True`, take one action, if something else (`elif`) is true, take another action. If none of the statements were true, do something else (`else`). You can see the trivial example by comparing `x` and `y` variables.

A couple of comments:

1. 4 spaces at the beginning of the line are there for a reason. They tell Python that this line corresponds to the `if` statement body. There can be more than one line;
2. You can skip `else` statement in case you don't want to take any actions when the above conditions were false;
3. You can add as many `elif` statements as you want to make a sophisticated pattern or you can skip it at all;
4. You can combine multiple comparisons, like `if (x>5) & (y<10)`.

---

# `while` loop

Using the `while` loop we execute the set of statements as long as condition is `True`.

**General form**:

```python
while condition is True:
    do something
```

```python
x = 0

while x < 4:
    x += 1 # which is the equivalent of `x = x + 1`
    print(x)
```

```out
1
2
3
4
```

Notes: You can also say that you want to keep on taking some actions as long as condition is `True` using `while` loop.

Breaking down the steps for `while` loop from the example:

* *Step 1*. Check if `x` (which is initially `0`) is less than `4`. This is `True`, go into the loop body. Increase `x` by `1` (now `x` is `0+1=1`). Print `x` on the screen.
* *Step 2*. Check if `x` (which is `1`) is less than `4`. This is `True`, go into the loop body. Increase `x` by `1` (now `x` is `1+1=2`). Print `x` on the screen.
* *Step 3*. Check if `x` (which is `2`) is less than `4`. This is `True`, go into the loop body. Increase `x` by `1` (now `x` is `2+1=3`). Print `x` on the screen.
* *Step 4*. Check if `x` (which is `3`) is less than `4`. This is `True`, go into the loop body. Increase `x` by `1` (now `x` is `3+1=4`). Print `x` on the screen.
* *Step 5*. Check if `x` (which is `4`) is less than `4`. This is `False`, so exit the loop.

---

# `for` loops

A `for` loop is used for iterating over a sequence (like lists, tuples, dictionaries, sets, strings).

```python
my_list = ['data', 'science', 'rocks']

for word in my_list:     # iterate over all values in the list
    print(word.upper())  # change to upper register and print out the value
```

```out
DATA
SCIENCE
ROCKS
```

```python
stdev = [2, 4, 1.5, 2, 4]     # list of standard deviations

variances = []                # initialize the empty list that will hold variances
for val in stdev:             # iterate over all values in the list
    variances.append(val**2)  # append the variances list with squared value

print(variances)
```

```out
[4, 16, 2.25, 4, 16]
```

Notes: Unlike `while` loops, `for` loops don't require any condition. But they require an iterable object (like a list). Even though `for` loops can be really computationally slow, they are really helpful in some applications.

In the first example, we were iterating over the list `my_list`, which consists of three strings. At each step of the loop, we defined a temporary variable `word` (name `word` is arbitrary, you can call it as you wish) as a value from the lists.

* *Step 1*. `word` = `'data'`
* *Step 2*. `word` = `'science'`
* *Step 3*. `word` = `'rocks'`
* Since no more objects left in the list, exit the loop.

The second example shows how you can get take every number to the power of two using `for` loop.

---

# Breaking the loops

<center><img src="https://i.ibb.co/Wfs3ZMP/photo-2019-10-26-16-00-54.jpg" width="500"></center>

Notes:
* If you need to break the loop before it has looped through all the items (in the `for` loop) or even if the statement is still `True` (in the `while` loop) you can use the `break` statement.
* With the `continue` statement you can stop the current iteration of the loop and continue with the next one.

---

# `break` vs `continue`

```python
stdev = [2, 4, 0, 1.5, 2, 4]
```
```python
variances = []
for val in stdev: # example 1
    if val == 0:
        continue  # exit the current step of the loop
    variances.append(val**2)
print(variances)
```
```out
[4, 16, 2.25, 4, 16]
```

```python
variances = []
for val in stdev: # example 2
    if val == 0:
        break  # exit the entire loop
    variances.append(val**2)
print(variances)
```
```out
[4, 16]
```

Notes: As in the previous example, we want to get the variances from the list of standard deviations. However, we see that now we have a value of `0` in the list, which doesn't make so much sense. We have two different scenarios:

1. We want to square **all the values except for `0`**. In such a case, we can use `continue` statement. When condition `val==0` is true, Python ends the current step of the loop and starts a new one. So we omit the code with the appending in our example.

2. We want to square **all the values before the `0`**. Who knows, maybe something went wrong in the calculations and we cannot trust all the values after the zero. When condition `val==0` is true, the `break` statement ends the whole loop, even if more steps could be performed.

---

# List comprehensions

List comprehensions provide a concise way to create lists.

```python
stdev = [2, 4, 0, 1.5, 2, 4]
variances = [val**2 for val in stdev]
print(variances)
```
```out
[4, 16, 0, 2.25, 4, 16]
```

```python
variances = [val**2 for val in stdev if val != 0]
print(variances)
```
```out
[4, 16, 2.25, 4, 16]
```

```python
variances = [val**2 if val != 0 else "wrong value" for val in stdev]
print(variances)
```
```out
[4, 16, "wrong value", 2.25, 4, 16]
```

Notes: List comprehensions allow creating a new list in a shorter way using `for` loops directly inside the list. However, sometimes such lines of codes become "harder" to read.

You can even add `if`/`else` statement. Note the difference in the order of statements with and without `else`.

---

# Time to automate!
