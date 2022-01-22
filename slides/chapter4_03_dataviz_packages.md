---
type: slides
---

# Packages for data visualization

---

# Matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

[Website](https://matplotlib.org/) || [Documentation](https://matplotlib.org/stable/contents.html) || [Gallery](https://matplotlib.org/stable/gallery/index.html)

**Importing `matplotlib`**:

```python
import matplotlib.pyplot as plt
```
Notes: Matplotlib must be the most commonly used package for data visualization in Python. If you have worked in MATLAB, you might see a lot of similarities in the plotting syntax  (hence the name). Matplotlib has a gallery with the possible graphs you can make, which makes it easy to adapt the code for your own problem.

Most of the time we don't need the whole package, but just a module `pyplot`, with the alias name `plt`.

---

# Anatomy of a figure

<center><img src="plt/anatomy.png" width="500"></center>

Notes: Here are some possible parameters you can change in the plot, such as title, legend, grid, axis labels, grid and so on.

---

# Syntax basics

```python
x = np.linspace(start=0, stop=6*np.pi, num=100)
y_sin = np.sin(x)

plt.figure() # start
plt.plot(x, y_sin)
plt.title("My First Plot")
plt.xlabel("This is x axis")
plt.ylabel("This is y axis")
plt.show()   # end
```

<img src="plt/example.png" width="400">

Notes: One of the way to think about the plotting syntax is in this way.

1. Start new figure with `plt.figure()`
2. Add parameters you need, such as line, bars, labels, legend, etc.
3. Stop figure creation by `plt.show()`

`plt.plot()` can be used to create a line plot (be default) or scatter plot (by adding `"o"`), so it is not a "universal" plotting function, as it could seen.

---

# Adding more objects to the figure

```python
y_cos = np.cos(x)

plt.figure() # start
plt.plot(x, y_sin, 'o--', color='r', label='Sine')
plt.plot(x, y_cos, color='black', label='Cosine')
plt.axhline(y=0, linewidth=1, color='#42f5b0', linestyle='dashed', label='Zero')
plt.title("My First Plot", fontsize=18)
plt.xlabel("This is x axis")
plt.ylabel("This is y axis")
plt.legend()
plt.show()   # end
```

<img src="plt/line2.png" width="400">

Notes: Here is an example of how you can add more objects to the figure. Note that order is not important, as long as you keep all the new plotting objects between `plt.figure()` and `plt.plot()`.

Some explanations:

* `'o--'` in `plt.plot()` is a shortcut to make a scatter plot connected with a dashed line;
* `color` can be in a string format with a full word (`"green"`), with one letter (`"g"`, meaning green), HEX color (`"#ffffff"`) or RGB color as a list (`(0.1, 0.2, 0.5)`) (and maybe even more other options);
* `label` is responsible for assigning a name to an object on a legend. In order to show the legend we need to add `plt.legend()`;
* `plt.axhline()` creates a `h`orizontal `line` through the `ax`is. There is also `plt.axvline()`.

---

# Area chart

```python
plt.figure()
plt.plot(x, y_sin, x, y_cos)
plt.fill_between(x, y_sin, alpha=0.5)
plt.fill_between(x, y_cos, alpha=0.5)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("Sine/Cosine Area Chart", fontsize=18)
plt.show()
```

<img src="plt/area.png" width="400">

Notes: One of the ways to create an area chart is to use `plt.fill_between()` function. `alpha` is responsible for opacity (`0`: object is transparent, `1`: full color).

---

# Bar plot

```python
df = pd.DataFrame(
    {"month": ["Jan", "Feb", "Mar", "Apr", "May"],
     "value": [100, 130, 200, 120, 140]})
df.sort_values(by="value", ascending=False, inplace=True)

plt.figure()
plt.bar(df["month"], df["value"])
plt.title("Bar Chart", fontsize=18)
plt.xlabel("Month")
plt.ylabel("Value")
plt.show()
```

<img src="plt/bar.png" width="350">

Notes: `plt.bar()` displays the bar in a given order from the DataFrame/list. So if you want to represent bars in a specific order (for example, descending as on the example), you have to perform some manipulations on the DataFrame before calling the plot function.

---

# Matplotlib & Seaborn = perfect combo

Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

[Website](https://seaborn.pydata.org/) || [Documentation](https://seaborn.pydata.org/api.html) || [Gallery](https://seaborn.pydata.org/examples/index.html)

**Importing `seaborn`**:

```python
import seaborn as sns
```

Notes: Even though Matplotlib is great, it works better in a combination with a Seaborn. You can think of Seaborn as a "wrapper" over Matplotlib functions. Both packages have its own advantages or disadvantages, and some plots are easy to create in one package, some in another.

---

# Scatter plot

```python
df = pd.DataFrame(
    {"height": [167, 189, 170, 175, 190, 183],
     "weight": [65, 78, 60, 68, 79, 72]})

plt.figure()
sns.scatterplot(data=df, x="height", y="weight")
plt.title("Height vs Weight", fontsize=18)
plt.show()
```

<img src="plt/scatter.png" width="400">

Notes: Even though we are using Seaborn to create a scatter plot, we still need Matplotlib to call layout functions, like `plt.title()`.

Note that we didn't call `plt.xlabel()` or `plt.ylabel()`, Seaborn takes the axis labels from column names (score another one for Seaborn). Also, you have two options on how to specify `x` and `y` arguments inside the Seaborn functions. The first method is represented on the left, by specifying the `data` and then calling `x` and `y` as column names. Or you could do this in a Matplotlib style:

```python
sns.scatterplot(
    x=df["height"],
    y=df["weight"]
)
```

---

# Subplots

```python
df = pd.DataFrame(
    {"height": [167, 189, 170, 175, 190, 183],
     "weight": [65, 78, 60, 68, 79, 72],
     "gender": ["M", "F", "F", "F", "M", "M"]})

 plt.figure(figsize=(10,4))
 plt.subplot(1,2,1)
 sns.scatterplot(data=df, x="height", y="weight", hue="gender")
 plt.title("Height vs Weight", fontsize=18)

 plt.subplot(1,2,2)
 sns.barplot(data=df, x="weight", y="weight")
 plt.title("Average Height by Gender", fontsize=18)
 plt.show()
```

<img src="plt/subplot.png" width="500">

Notes: Matplotlib also allows to created a combined graphs using `plt.subplot()` function. Inside the subplot function we specify three values:

1. total number of rows for the final plot;
2. total number of columns for the final plot;
3. index of the plot that is currently modified. Ordering goes left to right, top to bottom.

In this example, we specified that the final plot will consist of `1` row and `2` columns (meaning that we will have two different plots on the same row). For the first plot, we are adding the scatter plot, for the second plot we are adding the bar plot.

Some comments:

* `hue` allows adding a grouping variable;
* we don't have to calculate the average to `weight` in order to pass the values to the [`sns.barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html) function since Seaborn does this for us. In fact, we can change the function to another one using the `estimator` argument.
* [Matplotlib subplots and axes objects](http://www.math.buffalo.edu/~badzioch/MTH337/PT/PT-matplotlib_subplots/PT-matplotlib_subplots.html)

---

# Let's plot!
