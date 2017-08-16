My experiments with various ML tools & algorithms

# Contents

* [Problem Types](#problem-types)
* [Tools](#tools)
  * [Data manipulation](#data-manipulation)
  * [Bayesian methods](#bayesian-methods)
  * [Python](#python)
  * [ML pipelines](#ml-pipelines)
  * [R](#r)
  * [Spark](#spark)
  * [Deep Learning](#deep-learning)
  * [ML-as-a-Service](#mlaas)

# Problem Types
| Problem type | scikit-learn | PySpark-MLlIB | SparkR | R |
| ----- | ----- | ----- | ----- | ----- |
| [Dimensionality Reduction](dimensionality-reduction) | | N/A| | |
| [Density Estimation](density-estimation) | | KDE | | |
| [Clustering](clustering) | | KMeans, GMM, PIC| | |
| Classification | | | | |
| [Regression](regression) | | | | |
| [Frequent Pattern Mining](association-rules) | | | | |
| [Recommender Systems](recommender-systems) | | | | |
| NLP | | LDA | | `tm` |


# Tools

## Data manipulation
| Topic | NumPy | pandas | PySpark | SparkR |
| ----- | ----- | ----- | ----- | ----- |
| Creation | [NumPy](numpy/numpy-array-creation.ipynb)  | [pandas](pandas-series-dataframe-creation.ipynb) |  |  |
| Indexing / Slicing | [NumPy](numpy-indexing-slicing.ipynb) | [pandas](pandas-indexing.ipynb) |  |  |
| Grouping / Aggregation | | [pandas](pandas-grouping-aggregation.ipynb) |  |  |
| Merging / Reshaping | [NumPy](numpy-reshaping.ipynb) | [pandas](pandas-merging-reshaping.ipynb) |  |  |
| Sorting | [NumPy](numpy-sorting.ipynb) | [pandas](pandas-sorting.ipynb) |  |  |
| Searching | [NumPy](numpy-search.ipynb) | [pandas]() |  |  |
| RNG / sampling | [NumPy](numpy-random.ipynb) |  |  |  |

## Python
| Topic | Comments |
| ----- | ----- |
| [NumPy](numpy/) | Efficient storage for large multi-dimensional arrays & vectorized functions operating on these arrays |
| [pandas](pandas/) | Labeled access to column-oriented data frames & series |
| [scikit-learn](scikit-learn/) | Machine learning in Python (single machine only) |
| [matplotlib/Seaborn](#matplotlib-seaborn-notes.ipynb) | High-level (Seaborn) & low-level (matplotlib) visualization libraries |
| [iPython/Jupyter](jupyter-notes.ipynb) | Notebooks for interactive computing, prototyping and reporting |
| SciPy | Numerical routines |
| statsmodels | Statistical models & tests |
| [xgboost](xgboost/) | Scalable gradient boosting (typically used with decision trees) with interfaces to Python & R |
| Dask | Parallel computing with task scheduling |
| Numba | Convert Python code to LLVM code that is JIT compiled to machine code |
| Cython | Extend Python with C-like properties to generate C code that can be compiled into machine code with Ahead-Of-Time compilation. |


**Notes**
* Rendered Jupyter notebooks can be viewed on GitHub by clicking on the notebook file or at http://nbviewer.jupyter.org/github/niranjv/ml/
* [DMTK](https://www.dmtk.io/)
* [Scikit-learn tutorial](http://nbviewer.jupyter.org/github/jakevdp/sklearn_tutorial/blob/master/notebooks/Index.ipynb)
* [Data science ipython notebooks](https://github.com/donnemartin/data-science-ipython-notebooks)

