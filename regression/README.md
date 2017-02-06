# Contents
* [Overview](#overview)
* [Notebooks](#notebooks)

Approaches
* LARS
* Principal Components Regression
* Bayesian Regression
* Logistic Regression
* MARS
* LOESS
* Isotonic Regression
* Stochastic Gradient Descent

* [References](#references)

## Overview
Explore regression in scikit-learn, R, Spark MLLib

## Notebooks
* [OLS vs. Ridge Regression (CV) vs. LASSO (CV) vs. Elastic Net (CV)](OLS vs Ridge_CV vs LASSO_CV vs ElasticNet_CV.ipynb)
* Ridge Regression (CV) vs. Bayesian Linear Regression with Normal prior
* LASSO regression (CV) vs. Bayesian Linear Regression with double Exponential (Laplace) prior
* OLS vs. Principal Components Regression vs. Partial Least Squares Regression vs. Ridge Regression

* Least Angle Regression (LARS)
* Principal Component Regression (if features are correlated, run PCA first and then regress on a few PCs)
* Bayesian regression
* Logistic regression
* MARS
* LOESS

## Isotonic Regression
* Focus here is only on 1-d linear ordered isotonic regression, not general isotonic regression
* Non-parametric regression method to fit a non-decreasing function to data
* Similar to inexact smoothing splines except that monotonicity instead of smoothness is used to remove noise
* Fit a free-from line to a set of data s.t. line is non-decreasing everywhere and minimizes MSE on data
* No assumptions about target function (e.g., linearity like in a linear model)
* Can we weighted or unweighted (all weights must be > 0); no contradictory constraints

### Advantages
* Non-parametrics
* Fast
* Simple

### Disadvantages
* Points at ends of intervals can be noisy
* Works best when n > 10,000 (can smooth outcome to improve performance when `n` < 10,000)

### Applications
 * For fitting non-parametric model to data that is expected to be ordered
 * Improve calibration of probabilistic classifier - correct probabilities output by classifiers like random forests, boosted trees, SVMs, etc. (but not neural networks which are well calibrated)
 * Calibration of recommendation models
 * Non-metric multi-dimensional scaling - isotonic regression is used to find distance as a function of item-item similarity 
 
### Algorithms
* Linear ordered isotonic regression is solved using Pool Adjacent Violators Algorithm (PAVA)

### Implementations
* scikit-learn: `IsotonicRegression`
* R: `isoreg`, `Iso` package, `isotone` package, `isoMDS`
* Spark: ` IsotonicRegression`, ` IsotonicRegressionModel`

### References
* [Ad Click Prediction: a View from the Trenches](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41159.pdf), KDD 2013
* [Web-Scale Bayesian Click-Through Rate Prediction for Sponsored Search Advertising in Microsoft’s Bing Search Engine](https://www.microsoft.com/en-us/research/wp-content/uploads/2010/06/AdPredictor-ICML-2010-final.pdf), ICML 2010
* [Predicting Good Probabilities With Supervised Learning](http://www.cs.cornell.edu/~alexn/papers/calibration.icml05.crc.rev3.pdf)
* [Fastest Isotonic Regression Algorithms](http://web.eecs.umich.edu/~qstout/IsoRegAlg_1507.pdf)
* Kaggle: [Give Me Some Credit contest](https://www.kaggle.com/c/GiveMeSomeCredit)
* Platt Scaling - Calibration of probabilistics classifier using sigmoid functions). Better than isotonic regression for `n` < 5,000. Slower than isotonic regression for all `n`.

* Stochastic Gradient Descent

Notes:
* Ridge regression and LASSO are forms of penalized estimation. They introduce bias into estimation of model parameters to reduce variance of estimate. They have lower MSE than OLS when multi-collinearity is present. These methods are used mainly for prediction and not for inference since it is difficult to account for bias

## References
* [scikit-learn Generalized Linear Models](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model)
* [Wikipedia - Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)
* Numerical Python, Robert Johansson, APress, 2015
