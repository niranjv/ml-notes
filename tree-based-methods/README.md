# Contents
* [Overview](#overview)
* [Investigations](#investigations)
* [References](#references)

## Overview
Explore regression in scikit-learn, R, Spark MLLib

## Investigations
* `ESL, Algorithm 15.1`: Implement RF algorithm, compare to `randomForests` in R
* `ESL, Eq 15.1`: Derive correlation for non-independent random variables
* `ESL, Fig 15.1`: Test error for RF, bagging, gradient boosting as a function of # trees
* `ESL, Fig 15.2`: Test error for RF, bagging, gradient boosting
* `ESL, Fig 15.3`: Test error for RF & gradient boosting for various parameters
* `ESL, Fig 15.4`: `OOB` error vs. test error
* Elaborate on `OOB` error vs. test error with k-fold cross validation
* `ESL, Fig 15.5`: Variable importance - Gini vs. randomization
* `ESL, Section 15.3.4`: Hypergeometric distribution to calculate P(relevant variable) when `m` variables are selected from `p` variables
* `ESL, Fig 15.7`: Test error as a function of # irrelevant variables for RF and gradient boosting for different numbers of relevant & irrelevant variables
* `ESL, Fig 15.8`: Test error as a function of tree size
* `ESL, Fig 15.9`: Correlations between tree pairs as a function of `m`
* `ESL, Fig 15.10`: Bias, Variance of single tree vs. RF
* `ESL, Fig 15.11`: RF vs. kNN (k = 1,2,3,...) on various data sets

* `ISLR Fig 8.1/8.2/8.4`: Partition `Hitters` data using decision tree
* `ISLR Fig 8.5`: MSE for `Hitters` data
* `ISLR Fig 8.6`: Decision tree for `Heart` data
* `ISLR Fig 8.8`: `OOB` vs. test error for bagging vs RF for `Heart` data
* `ISLR Fig 8.9`: Variable importance for `Heart` data
* `ISLR Fig 8.10`: Test error as a function of # trees for different values of `m`
* `ISLR Algorithm 8.2`: Implement boosting

## References
* [Wiki](https://github.com/niranjv/ml-notes/wiki/Tree-based-Methods)
