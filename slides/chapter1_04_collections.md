---
type: slides
---

# Collecting objects together

Notes: So far you have seen how to work with variables that hold a single object (like `age = 20` or `DNA = "ATGC"`). But wouldn't it be great if you could store multiple objects in one variable (for example, variable with all participants' age)?

There are 4 commonly used collection types in Python that you will see in the next slides:

* Lists
* Tuples
* Sets
* Dictionaries

---

# Lists

List is a collection which is ordered and changeable. Allows duplicate members.

```python
age = [15, 25, 45, 16, 18, 20, 25]
print(type(age))
```

```out
list
```

```python
age[:5])   # returns [15, 25, 45, 16, 18]
age[3:7])  # returns [16, 18, 20, 25]
age[::-1]  # returns [25, 20, 18, 16, 45, 25, 15]
age[-2]    # returns 20
print(age) # object stayed unchanged
```

```out
[15, 25, 45, 16, 18, 20, 25]
```

Notes: Remember the slicing we did for the strings? Exactly the same idea applies to the lists. And no matter what type of slicing you do, as long as you don't rewrite your variable, it will stay unchanged.

---

# Basic operations with lists

```python
age = [15, 25, 45, 16, 18, 20, 25]

len(age) # returns 7
min(age) # returns 15
max(age) # returns 45
sum(age) # returns 164

avg_age = sum(age) / len(age)
print(round(avg_age,2))
```

```out
23.43
```

**Lists can hold objects of different types**:

```python
i_am_valid_list = [1, "Hello", [1,2,False], True-0, 42<3.14]
print(i_am_valid_list)
```

```out
[1, 'Hello', [1, 2, False], 1, False]
```

Notes: There are some trivial built-in functions like `sum()`, `max()`, `min()` that could be applied to lists. There is no built-in `avg()` or `mean()` function, but you could easily calculate it yourself.

Keep in mind, that list can hold objects of different type, even another lists. Some functions like `sum()` wouldn't work in that case since you cannot take sum of string and number for obvious reasons.

---

# method == function?

```python
participants = ['Bob', 'Bill', 'Sarah', 'Max', 'Jill']
# methods that modify the initial list
participants.append('Jack') # append one element to the end
# ['Bob', 'Bill', 'Sarah', 'Max', 'Jill', 'Jack']
participants.extend(['Anna', 'Bill']) # append multiple elements to end
# ['Bob', 'Bill', 'Sarah', 'Max', 'Jill', 'Jack', 'Anna', 'Bill']
participants.insert(0, 'Louis') # insert element at index 0 (shifts everything to the right)
# ['Louis', 'Bob', 'Bill', 'Sarah', 'Max', 'Jill', 'Jack', 'Anna', 'Bill']
participants.remove('Jill') # searches for first instance and removes it
# ['Louis', 'Bob', 'Bill', 'Sarah', 'Max', Jack', 'Anna', 'Bill']
participants.pop(1) # removes the element at index 0 and returns it
# ['Louis', 'Bill', 'Sarah', 'Max', Jack', 'Anna', 'Bill']

# not a method, but in this way you can change the value(s) of the list
participants[2] = 'Ben' # replace element at the index 2
# ['Louis', Bill', 'Ben', 'Max', Jack', 'Anna', 'Bill']
```

```python
# methods that don't change a sting and return a new object
print(participants.count('Bill')) # returns the number of instances;
print(participants.index('Max'))  # returns index of first instance;
```

```out
2
3
```

Notes: You heard terms "method" and "function" already and most of the times they were be used interchangeably. Confusing, isn't it? Think of methods as a function, that could be applied only for specific data type. Whereas function `len()` for example can be applied on strings, lists and many other objects. We call function by `function(object)` and method by `object.method()`.

On this slide you can see some of the methods, that are unique for the lists.  It's important to note that all of these methods change the initial string. You can see how the string changes in comment lines.

If you run a code like this one, you will end up with `NoneType` object:

```python
l = [1,2,3]
l = l.append(4)
```

However, this is not always the case. Some methods don't change the method (or have an argument that allow to specify it). The best way to know whether method changes the object or returns a new objects is the documentation.

---

# Tuples

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

```python
colors = ("green", "black", "orange")
# or:
# colors_list = ["green", "black", "orange"]
# colors = tuple(colors_list)
print(type(colors))
```

```out
tuple
```

```python
my_tuple[0] = "pink"
```

```out
TypeError: 'tuple' object does not support item assignment
```


Notes: Another collection type in Python is tuple. We defined lists using the square brackets (`[1,2,3]`), but for tuples we use parentheses (`(1,2,3)`).

Tuples are quite boring, since they don't have so much methods that can be applied on them. But there is a reason for that. Tuples are **unchangeable**. This means that no function or method can change objects in the tuple.

---

# Sets

Set is a collection which is unsorted and un-indexed. No duplicate members.
```python
languages = {'python', 'r', 'java'} # create a set directly
snakes = set(['cobra', 'viper', 'python']) # create a set from a list
```

**Set operations**:
```python
languages & snakes # intersection, AND
```

```out
{'python'}
```

```python
languages | snakes # union, OR
```

```out
{'cobra', 'java', 'python', 'r', 'viper'}
```

```python
languages - snakes # set difference
```

```out
{'java', 'r'}
```

Notes: Figure brackets are the indicator for sets, another collection type. You cannot access items in a set by referring to an index, since sets are unordered and have **no index**. But you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword.

You can apply basic sets commands (like union or intersection). Note that we didn't get `'python'` twice for the union, since sets don't allow duplicate values. This fact can become handy used when looking for the unique values in a list.

---

# Dictionaries

Dictionaries are: unordered, iterable, mutable.

```python
my_dict = {'name': 'Bob', 'planet': 'X', 'age': 42}
print(my_dict['name'])
```

```out
Bob
```

```python
# add new key-value pair to the dictionary
my_dict['last_name'] = 'Smith'
print(my_dict)
```
```out
{'name': 'Bob', 'planet': 'X', 'age': 42, 'last_name': 'Smith'}
```

```python
my_dict.keys()
```
```out
['name', 'planet', 'age', 'last_name']
```

```python
my_dict.values()
```
```out
['Bob', 'X', 42, 'Smith']
```

Notes: Dictionaries are structures which can contain multiple data types, and is ordered with key-value pairs: for each (unique) key, the dictionary outputs one value. Keys can be strings, numbers, or tuples, while the corresponding values can be any Python object.

```python
dict_obj = {
    'key1': value1,
    'key2': value2,
    ...}
```
As you can see from the first example, you cannot access values of the dictionary by the indexes (like you did in lists). But you can access them by the key. Due to this feature dictionaries don't allow duplicated keys.

You can also access just the keys or just the indexes by `.keys()` and `.values()` methods.
---

# Let's code!
