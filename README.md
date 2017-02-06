My experiments with various ML tools & algorithms

**Contents**
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Problem Types](#problem-types)
- [Tools](#tools)
	- [Python](#python)
	- [R](#r)
	- [Spark](#spark)
	- [Deep Learning](#deep-learning)

<!-- /TOC -->

# Problem Types
| |
| --- |
| [Frequent Pattern Mining](association-rules) |
| Classification |
| [Clustering](clustering) |
| [Density Estimation](density-estimation) |
| [Dimensionality Reduction](dimensionality-reduction) |
| [Recommender Systems](recommender-systems) |
| [Regression](regression) |

# Tools

## Python
|   |  |
|--------|-------------|
| [NumPy](numpy/) | Efficient storage for large multi-dimensional arrays & vectorized functions operating on these arrays |
| [pandas](pandas/) | Labeled access to column-oriented data frames & series |
| [scikit-learn](scikit-learn/) | Machine learning in Python (single machine only) |
| [matplotlib/Seaborn](#matplotlib-seaborn-notes.ipynb) | High-level (Seaborn) & low-level (matplotlib) visualization libraries |
| [iPython/Jupyter](jupyter-notes.ipynb) | Notebooks for interactive computing, prototyping and reporting |
| SciPy | Numerical routines |
| statsmodels | Statistical models & tests |
| PyMC | Bayesian statistical model fitting with MCMC |
| [xgboost](xgboost/) | Scalable gradient boosting (typically used with decision trees) with interfaces to Python & R |
| Dask | Parallel computing with task scheduling |
| Numba | Convert Python code to LLVM code that is JIT compiled to machine code |
| Cython | Extend Python with C-like properties to generate C code that can be compiled into machine code with ahead-of-time compilation. |

## R

| | |
|--------|-------------|
| RStudio | IDE for R programming |
| R notebooks | Interactive R markdown doc with executable chunks (alternative to Jupyter notebooks for R) |
| data.table | Faster version of data.frame to handle large data sets (100s of GB) |
| caret | Classification & regression models |
| mlr | Machine learning in R  |
| forecast | Analyze univariate time series |
| metrics, MLmetrics | Common evaluation metrics in machine learning  |
| xgboost | Scalable gradient boosting (typically used with decision trees) with interfaces to Python & R |
| hadley-verse: dplyr, tidyr, stringr, httpr, knitr, devtools, feather, testthat, devtools, ggplot2 | Tools for data manipulation, unit testing, package development & plotting |
| Stan, RStan | Bayesian inference with Hamiltonian Monte Carlo, variational inference & penalized ML with interfaces to R & Python |

## Spark

| | |
|--------|-------------|
| Databricks notebooks | Interactive Jupyter-like notebooks for Spark programming in Python, R, etc. |
| MLLib | Spark's Scalable machine learning library with interfaces to Python & R |
| PySpark | Python interface to Spark |
| SparkR, `sparklyr` | R package to interface with Spark |
| Spark on AWS EMR | Run Spark clusters in AWS with access to S3 & Hive |

AWS ML - Machine learning as a service for creating and deploying models with support for linear & logistic regression

## Deep Learning

| | |
|--------|-------------|
| Keras + TensorFlow/Theano  | Python package to enable fast experimentation with deep learning frameworks like TensorFlow & Theano on CPUs & GPUs |
| mxnet | Deep learning library with interfaces to Python & R |


**Notes**
* Rendered Jupyter notebooks can be viewed on GitHub by clicking on the notebook file or at http://nbviewer.jupyter.org/github/niranjv/ml/
* [Scikit-learn tutorial](http://nbviewer.jupyter.org/github/jakevdp/sklearn_tutorial/blob/master/notebooks/Index.ipynb)
* [Data science ipython notebooks](https://github.com/donnemartin/data-science-ipython-notebooks)
