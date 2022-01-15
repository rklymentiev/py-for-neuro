---
type: slides
---

# Working with MATLAB files

---

# MAT-files

<center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Matlab_Logo.png/800px-Matlab_Logo.png" width="300"></img></center>

MATLAB is a proprietary multi-paradigm programming language and numeric computing environment developed by MathWorks. MATLAB allows matrix manipulations, plotting of functions and data, implementation of algorithms, creation of user interfaces, and interfacing with programs written in other languages.

MAT-files are binary MATLAB files that store workspace variables.

Notes:

---

# Reading MAT files using scipy

```python
from scipy.io import loadmat
h1_data = loadmat(file_name="H1_neuron.mat", squeeze_me=True)
h1_data
```

```out
{'__globals__': [],
 '__header__': b'MATLAB 5.0 MAT-file, Platform: LNX86, Created on: Thu Feb 15 15:13:45 2001',
 '__version__': '1.0',
 'rho': array([0, 0, 0, ..., 0, 0, 0], dtype=uint8),
 'stim': array([-111.94824219,  -81.80664062,   10.21972656, ...,    9.78515625,
          24.11132812,   50.25390625])}
```

Notes: We can load MAT files into Python with the help of SciPy package. We are interested in `loadmat` function inside the `io` module.

The `squeeze_me` is responsible for squeezing unit matrix dimensions. For example, if MATLAB variable was stored in a shape (5,1,1), setting `squeeze_me=True` will import it with the shape (5,) to Python.

The resulting object is a dictionary. Each key represents saved variable from the MATLAB. Also, there are three additional keys with wile info.

[SciPy Website](https://www.scipy.org/)


---

#  Let's code!
