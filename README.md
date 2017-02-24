My experiments with various ML tools & algorithms

# Contents

* [Problem Types](#problem-types)
* [Tools](#tools)
 * [Data manipulation](#data-manipulation)
 * [Bayesian methods](#bayesian-methods)
 * [Python](#python)
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

## Bayesian methods
| Topic | Comments |
| ----- | ----- |
| **R:** JAGS, OpenBUGS | Bayesian inference using Gibbs Sampling |
| **Python:** PyMC | Bayesian statistical model fitting with MCMC |
| **Stan:** RStan, PyStan | Bayesian inference with Hamiltonian Monte Carlo, variational inference & penalized ML with interfaces to R & Python |

## NLP
| Topic | Comments |
| ----- | ----- |
| **Python:** NLTK, Spacy, gensim | Tokenization, word vectors, speech tagger, dependency parser |
| **PySpark:** LDA | Topic modeling |
| **R:** `tm` | Text mining framework |

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

## R

| Topic | Comments |
| ----- | ----- |
| R notebooks | Interactive R markdown doc with executable chunks (alternative to Jupyter notebooks for R) |
| data.table | Faster version of data.frame to handle large data sets (100s of GB) |
| caret | Classification & regression models |
| mlr | Machine learning in R  |
| forecast | Analyze univariate time series |
| metrics, MLmetrics | Common evaluation metrics in machine learning  |
| xgboost | Scalable gradient boosting (typically used with decision trees) with interfaces to Python & R |
| hadley-verse: dplyr, tidyr, stringr, httpr, knitr, devtools, feather, testthat, devtools, ggplot2 | Tools for data manipulation, unit testing, package development & plotting |

## Spark

| Topic | Comments |
| ----- | ----- |
| Databricks notebooks | Interactive Jupyter-like notebooks for Spark programming in Python, R, etc. |
| PySpark | Python interface to Spark |
| MLlib | Spark's Scalable machine learning library with interfaces to Python & R |
| `spark-sklearn` | Train and evaluate multiple scikit-learn models in parallel with Spark |
| Mahout-on-Spark | R-like syntax, scalable machine learning algorithms |
| SparkSQL | SQL interface for structured data |
| SparkR, `sparklyr` | R package to interface with Spark |
| Spark on AWS EMR | Run Spark clusters in AWS with access to S3 & Hive |

## Deep Learning

| | |
| ----- | ----- |
| Keras + TensorFlow/Theano  | Python package to enable fast experimentation with deep learning frameworks like TensorFlow & Theano on CPUs & GPUs |
| mxnet | Deep learning library with interfaces to Python & R |
| Microsoft Cognitive Toolkit (CNTK) | Deep learning toolkit to describing, training & executing computational networks with support for Python & GPUs |

## MLaaS
* [AWS ML](https://aws.amazon.com/machine-learning/)
* [Azure ML](https://azure.microsoft.com/en-us/services/machine-learning/)
* [Google Prediction API](https://cloud.google.com/prediction/)
* [Algorithmia](https://algorithmia.com/)
* [BigML](https://bigml.com/)


**Notes**
* Rendered Jupyter notebooks can be viewed on GitHub by clicking on the notebook file or at http://nbviewer.jupyter.org/github/niranjv/ml/
* [Scikit-learn tutorial](http://nbviewer.jupyter.org/github/jakevdp/sklearn_tutorial/blob/master/notebooks/Index.ipynb)
* [Data science ipython notebooks](https://github.com/donnemartin/data-science-ipython-notebooks)
* [Databricks blog: SparkR - 10 things](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/8599738367597028/1792412399382575/3601578643761083/latest.html?utm_campaign=Open%20Source&utm_source=Databricks%20Blog)
