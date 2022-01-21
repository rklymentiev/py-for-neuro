---
type: slides
---

# Numerical operations with NumPy

---

# Welcome `numpy`

NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

[Website](https://numpy.org/) || [Documentation](https://numpy.org/doc/)

### Importing NumPy:

```python
import numpy as np

# square root function
print(np.sqrt(4))
```

```out
2.0
```

Notes: NumPy is one of the most fundamental packages for numerical computing in Python. It has hundreds of functions, but in this chapter, we will not go through all of them. The main goal is to introduce the main idea of working with NumPy so you can continue exploring the package's possibilities on your own.
---

# Arrays

NumPy is great for doing vector arithmetic. A NumPy array is a grid of values, all of the same type, and is indexed by a tuple of non-negative integers.

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

Notes: The array is the basic NumPy type which has lots of benefits over lists. Important to remember, that objects in the array should be **the same type**. If it's not the case (like in `b` array), NumPy will convert all objects to one data type it finds most convenient. For the `b` case it converted all the objects to the string since there was already one string. Usually, we don't work with strings in NumPy so our arrays consist of numeric values most (if not 100\%) of the time.

Just as lists, numpy array can have a nested structure. `c` array is a 2-dimensional array with the shape 2x2, meaning it has two rows and two columns.

---

# Vector operations

### Convert values in a list from Celsius to Fahrenheit:

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

Notes: You can see a simple example of numeric operations on lists vs arrays. NumPy makes life easier through [vectorization](https://blog.paperspace.com/numpy-optimization-vectorization-and-broadcasting/). We can apply operations directly on an array (in the same way we would apply them on a vector) without calling any mapping functions, loops, or so on.

---

# 3-D arrays

| Image as we see it | Image as Python sees it |
|:-:|:--|
| <img src="imgs/brain_photo.jpg" width="300"> |  <code> import numpy as np<br>from skimage import io<br>IMG_URL = 'brain_photo.jpg'<br>image = io.imread(IMG_URL)<br>image.shape</code><br><code>(3024, 4032, 3)</code> |

<span>Photo by <a href="https://unsplash.com/@natcon773?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Natasha Connell</a> on <a href="https://unsplash.com/s/photos/brain?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

Notes: The best way to visualize the multidimensional array is through an image. We don\'t care at the moment how we imported this image in Python. The most important is that now the image is a 3-D array `array` with the shape `(3024, 4032, 3)`, meaning that the original image had 3024 pixel height, 4032 pixels width and 3 layers (red, green and blue). The array is filled with values in a range [0, 255] that correspond to a pixel intensity of each layer. You will see how slicing affects the image in the next slide.

---

# Slicing

<center><img src="imgs/brain_slice.png" width="500"></center>

Notes: On the first plot, you see the Python visualization of the array without any slicing.

On the second plot, we took `100:1200` values from the first dimension (*height*), all values (`:`) from the second dimension (*width*), and all values (`:`) from the third dimension (*layers*).

On the third plot, we took all values (`:`) from the first dimension (*height*), `1300:2400` values from the second dimension (*width*) and all values (`:`) from the third dimension (*layers*).

On the fourth plot, we took `1100:1350` values from the first dimension (*height*), `1200:1500` values from the second dimension (*width*) and all values (`:`) from the third dimension (*layers*).

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

* rank, determinant, trace, etc. of an array;
* eigenvalues/vectors of matrices;
* matrix and vector products (dot, inner, outer product), matrix exponentiation;
* solve linear or tensor equations, and much more!

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

Notes: Example of solving the linear equations. Here we distinguished that *x1* = 0, *x2* = 0.5.

---

# Let's code!
