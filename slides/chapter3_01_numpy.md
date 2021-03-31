---
type: slides
---

# Numerical operations with NumPy

---

# Welcome `numpy`

NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

[Official Website](https://numpy.org/) || [Documentation](https://numpy.org/doc/)

**Importing `numpy`**:

```python
import numpy as np

# square root function
print(np.sqrt(4))
```

```out
2.0
```

Notes: `numpy` is one of the most fundamental packages for numerical computing in Python. It has hundreds of functions which is impossible to memorize. In this chapter we will not go through all of them. The main goal is to introduce the main idea of working with `numpy` so you can continue exploring package's possibilities on yourself.

To import any package we use `import` statement. You might wonder what is that `as np` doing there. This is what called "aliasing". Most of the packages have the "short" alias name, that is commonly used. In this way we specify that we are going to load the `numpy` library and will store it in `np` object. All the functions from the package will be called using `np.` prefix.

Basically you could also import package as `import numpy as FunnY_NamE` and later you would call any function from it as `FunnY_NamE.sqrt()`. There is also nothing wrong to not use any alias names at all (`import numpy`).

---

# Arrays

`numpy` is great for doing vector arithmetic. A `numpy` array is a grid of values, all of the same type, and is indexed by a tuple of non-negative integers.

```python
a = np.array([1, 3, 5])
print(type(a))
```
```out
numpy.ndarray
```

```python
b = np.array([1, 2, "hello"])
print(b)
```

```out
['1' '2' 'hello']
```

```python
c = np.array(
    [[1,2],
     [3,4]]
    )
print(c.shape)
```

```out
(2,2)
```

Notes: Array is the basic `numpy` type which has lots of benefits over lists. Important to remember, that objects in array should be **in the same type**. If it's not the case (like in `b` array), `numpy` will convert all object to one data type it finds most convenient. For the `b` case it converted all the objects to the string, since there was already one string. Usually we don't work with strings in `numpy` so our array are numeric most (if not 100\%) of the time.

Just as lists, `numpy` array can have nested structure. `c` array is 2 dimensional array with the shape 2x2, meaning it has two rows and two columns.

---

# Vector operations

**Convert values in a list from Celsius to Fahrenheit**:

```python
# lists
temperature = [18.0, 21.5, 21.0, 21.0, 18.8, 17.6, 20.9, 20.0]
temperature = list(map(lambda x: x * 9/5 + 32, temperature))
print(temperature)
```
```out
[64.4, 70.7, 69.8, 69.8, 65.84, 63.68, 69.62, 68.0]
```

```python
# numpy array
temperature_array = np.array([18.0, 21.5, 21.0, 21.0, 18.8, 17.6, 20.9, 20.0])
temperature_array = temperature_array * 9/5 + 32
print(temperature_array)
```
```out
[64.4, 70.7, 69.8, 69.8, 65.84, 63.68, 69.62, 68.0]
```

Notes: You can a simple example of numeric operations on lists vs arrays. `numpy` makes life easier and we can apply those operations directly on an array (in the same way we would apply them on a vector) without calling any mapping functions, loops or so on.

---

# 3-D arrays

| Image as we see it | Image as Python sees it |
|:-:|:--|
| <img src="brain_photo.jpg" width="300"> |  <code> import numpy as np<br>from skimage import io<br>IMG_URL = 'brain_photo.jpg'<br>image = io.imread(IMG_URL)<br>image.shape</code><br><code>(500, 667, 3)</code> |

<span>Photo by <a href="https://unsplash.com/@natcon773?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Natasha Connell</a> on <a href="https://unsplash.com/s/photos/brain?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

Notes: The best way to visualize the multidimensional array is through image. We don\'t care at the moment how we imported image in Python. The most important is that now image is a 3-D array `array` with the shape `(500, 667, 3)`, meaning that now we have original image had 500 pixel height, 667 pixels width and 3 layers (red, green and blue). The array is filled with values in a range [0, 255] that correspond to pixel intensity of each layer. In the next slide you will see how slicing affects the image.

---

# Slicing

<img src="brain_slice.png" width="1000">

Notes: On the first plot you see the Python visualization of the array without any slicing.

On the second plot we took `100:200` values from the first dimension (*height*), all values (`:`) from the second dimension (*width*) and all values (`:`) from the third dimension (*layers*).

On the third plot we took all values (`:`) from the first dimension (*height*), `300:400` values from the second dimension (*width*) and all values (`:`) from the third dimension (*layers*).

On the fourth plot we took `100:350` values from the first dimension (*height*), `200:500` values from the second dimension (*width*) and all values (`:`) from the third dimension (*layers*).



---

# Linear algebra (1)

```python
A = np.array(
    [[6, 1, 1],
     [4, -2, 5],
     [2, 8, 7]]
    )

print("Rank of A:", np.linalg.matrix_rank(A))
print("\nTrace of A:", np.trace(A))
print("\nDeterminant of A:", np.linalg.det(A))
print("\nInverse of A:\n", np.linalg.inv(A))
```

```out
Rank of A: 3

Trace of A: 11

Determinant of A: -306.0

Inverse of A:
 [[ 0.17647059 -0.00326797 -0.02287582]
  [ 0.05882353 -0.13071895  0.08496732]
  [-0.11764706  0.1503268   0.05228758]]
```

Notes: The Linear Algebra module of NumPy offers various methods to apply linear algebra on any numpy array. One can find:

* rank, determinant, trace, etc. of an array.
* eigen values/vector of matrices
* matrix and vector products (dot, inner, outer,etc. product), matrix exponentiation
* solve linear or tensor equations and much more!

---

# Linear algebra (2)

**Solving the equation**:

<img src="https://latex.codecogs.com/png.latex?\left\{\begin{matrix}&space;1&space;x_1&space;&plus;&space;2&space;x_2&space;=&space;10&space;\\&space;3&space;x_1&space;&plus;&space;4&space;x_2&space;=&space;20&space;\end{matrix}\right." title="\left\{\begin{matrix} 1 x_1 + 2 x_2 = 10 \\ 3 x_1 + 4 x_2 = 20 \end{matrix}\right." />
<br>
<img src="https://latex.codecogs.com/png.latex?\mathbf{A}&space;\mathbf{x}&space;=&space;\mathbf{B}" title="\mathbf{A} \mathbf{x} = \mathbf{B}" />

```python
A = np.array(
    [[1,2],
     [3,4]])

B = np.array([10, 20])

x = np.linalg.solve(A,B)
print(x)
```

```out
[0. 5.]
```

Notes: Example of solving the linear equations.

---

# Let's code!