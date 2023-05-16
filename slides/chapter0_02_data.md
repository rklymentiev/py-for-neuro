---
type: slides
---

# Data sets used in the course

Notes: All the files can be downloaded from the [GitHub page](https://github.com/rklymentiev/py-for-neuro/tree/binder/exercises/data).

---

# fMRI data

Path to the file: `"exercises/data/fmri_data.csv"`

<center><img src="imgs/fmri_data.png"></center>

Credits: Waskom, M. L., Frank, M. C., & Wagner, A. D. (2016). Adaptive Engagement of Cognitive Control in Context-Dependent Decision Making. *Cerebral Cortex*, bhv333. https://doi.org/10.1093/cercor/bhv333

Notes: Description: fMRI data from parietal and frontal regions from context-dependent decision making.

Found in the Seaborn package's datasets (`sns.load_dataset("fmri")`).

---

# Dementia data set

Path to the file: `"exercises/data/oasis_cross-sectional.csv"`

<center><img src="imgs/oasis.png"></center>

Credits: Marcus, D. S., Wang, T. H., Parker, J., Csernansky, J. G., Morris, J. C., & Buckner, R. L. (2007). Open Access Series of Imaging Studies (OASIS): Cross-sectional MRI Data in Young, Middle Aged, Nondemented, and Demented Older Adults. *Journal of Cognitive Neuroscience, 19*(9), 1498–1507. https://doi.org/10.1162/jocn.2007.19.9.1498

Notes: Description:  This set consists of a cross-sectional collection of 416 subjects aged 18 to 96. The subjects are all right-handed and include both men and women. 100 of the included subjects over the age of 60 have been clinically diagnosed with very mild to moderate Alzheimer’s disease (AD). Additionally, a reliability data set is included containing 20 nondemented subjects imaged on a subsequent visit within 90 days of their initial session.

Found at [Kaggle](https://www.kaggle.com/jboysen/mri-and-alzheimers).

---

# Breast cancer Wisconsin (diagnostic) data set

Path to the file: `"exercises/data/breast_cancer.csv"`

<center><img src="imgs/breast_cancer.png"></center>

Credits: Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. *SPIE Proceedings*. https://doi.org/10.1117/12.148698

Notes: Description: Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe the characteristics of the cell nuclei present in the image.

Even though this data is not brain-related, it is still a nice example of the numerical values extracted from the image data.

Found at [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29).

---

# H1 neuron's firing rate

Path to the file: `"exercises/data/H1_neuron.mat"`

```out
{'__globals__': [],
 '__header__': b'MATLAB 5.0 MAT-file, Platform: LNX86, Created on: Thu Feb 15 15:13:45 2001',
 '__version__': '1.0',
 'rho': array([0, 0, 0, ..., 0, 0, 0], dtype=uint8),
 'stim': array([-111.94824219,  -81.80664062,   10.21972656, ...,    9.78515625,
          24.11132812,   50.25390625])}
```

Credits: de Ruyter, R., & Bialek, W. (2002). Timing and Counting Precision in the Blowfly Visual System. *Models of Neural Networks IV*, 313–371. https://doi.org/10.1007/978-0-387-21703-1_8

Notes: Description: Data from a fly H1 neuron responding to an approximate white-noise visual motion stimulus. Data were collected for 20 minutes at a sampling rate of 500 Hz.

Found at [Theoretical Neuroscience Book](http://www.gatsby.ucl.ac.uk/~dayan/book/exercises.html) exercises (Dayan and Abbott).

Dayan, P., & Abbott, L. F. (2005). *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems (Computational Neuroscience Series)* (1st ed.). The MIT Press.

---

# Sample of the EEG data

Path to the file: `"exercises/data/eeg_sample.pickle"`

```out
{'ch_names': array(['Fp1', 'Fpz', 'Fp2', 'AF3', 'AF4', 'F7', 'F5', 'F3', 'F1', 'Fz',
        'F2', 'F4', 'F6', 'F8', 'FT7', 'FC5', 'FC3', 'FC1', 'FCz', 'FC2',
        ...,
        'CP6', 'TP8', 'M2', 'P7', 'P5', 'P3', 'P1', 'Pz', 'P2', 'P4', 'P6',
        'P8', 'PO7', 'PO5', 'PO3', 'POz', 'PO4', 'PO6', 'PO8', 'CB1', 'O1',
        'Oz', 'O2', 'CB2', 'HEOG', 'VEOG'], dtype='<U4'),
 'data': array([[-1.12866123e-05, -2.65288681e-05, -3.23824174e-06, ...,
          6.55850833e-05,  7.62328967e-05,  7.86320545e-05],
        [-9.48798291e-05, -9.65151415e-05, -8.66185865e-05, ...,
          4.31979958e-05,  5.25620877e-05,  5.46391135e-05],
        ...,
        [ 3.65203953e-05,  3.22641733e-05,  3.86147172e-05, ...,
         -1.63223759e-04, -1.51976764e-04, -1.50407239e-04],
        [-8.10325504e-04, -8.49075174e-04, -8.20144940e-04, ...,
         -2.83902613e-04, -2.62110763e-04, -2.61275838e-04]]),
 'srate': 500,
 'times': array([0.0000e+00, 8.0000e-03, 1.6000e-02, ..., 9.9976e+01, 9.9984e+01,
        9.9992e+01])}
```

Credits: Cavanagh, J. F., Bismark, A. W., Frank, M. J., & Allen, J. J. B. (2019). Multiple Dissociations Between Comorbid Depression and Anxiety on Reward and Punishment Processing: Evidence From Computationally Informed EEG. *Computational Psychiatry, 3*, 1–17. DOI: http://doi.org/10.1162/CPSY_a_00024

Notes: Description: THe sample consists of around 10 seconds of data measurements sampled at 500 Hz frequency and measured at 66 channels from one subject.

Found at [PREDiCT](http://predict.cs.unm.edu/): Petient Repository for EEG Data + Computational Tools.

---

# Let's start!
