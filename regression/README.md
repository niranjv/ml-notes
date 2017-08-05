# Contents
* [Overview](#overview)
* [Notebooks](#notebooks)
* Topics
  * [Linear Regression](#linear-regression)
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

## Linear Regression

* **Is there a relationship between covariates & response?** - Fit a multiple linear regression model to the data and test `H_0`: model coefficients for all covariates are 0. Use F-statistic to reject `H_0`.
* **How strong is the relationship?** - Use `RSE` & `R^2` as a measure of strength of relationship
* **Which covariates affect response the most?** - Look at p-values of each covariate in the model
* **Effect of each covariate on the response?** - Look at value of model coefficients. Ideally, 95% CI for model coefficient should be narrow and far from 0. Collinearity can affect width of this interval, so look at `VIF` scores also.
* **How accurately can we predict future response values from new covariates?** - For mean response, use confidence interval. To predict response for a set of covariates, use prediction interval (will always be wider than CI due to irreducible error). 
* **Is the relationship linear?** Look at plots of (studentized) residuals vs. fitted values. Transform response or predictors to remove non-linearity
* **Any interaction effects?** Include interaction term and look at its p-value. Also examine increase in `R^2` and decrease in `RSE` of model.

### Assessing accuracy of coefficient estimates

* Need to estimate model coefficients s.t. resulting line is as close as possible to the data
* Most common measure of closeness if `least squares` => estimate model coefficients to minimize `residual sum of squares`
* Error term in model represents everything that the model does not account for - missing covariates, non-linearity, noise in data, etc. It is usually assumed to be independent of `X`
* Linear approximation to `f` is `Y = B_0 + B_1* X + e` and defines the `population regression line`. This line is the best linear approximation to the true relationship between `X` and `Y`. 
* Model coefficients determined by least squares regression determine the `least squares line`
* Least squares estimates of population mean & model coefficients are unbiased
* Variance of estimate of mean = `sigma^2/n`, when the observations are all uncorrelated
* Std errors of population mean & model coefficients ~ avg amount by which estimate differs from true value. Std error formula assumes errors of observations are uncorrelated.
* Variance of error (`RSS`) is estimated as `residual standard error = sqrt( RSS/(n-2) )`
* Std errors are used for hypothesis testing, typically between `H_0` (no relationship) vs. `H_1` (some relationship). Calculate t-statistic from std error and compare to t-distribution with `n-2` degrees of freedom to determine how far estimate is from 0. The resulting probability is called `p-value`, i.e., for a given model, assuming null hypothesis, it is the probability of getting a t-statistic value greater than or equal to the  computed t-statistic value due to chance. Reject null hypothesis if p-value < a threshold (typically 0.05).


### Assessing accuracy of model

* If model is plausible (i.e., model coefficients have low p-values), quantify extent to which model fits data
* This typically done using:
 * Residual standard error (RSE) - this is an estimate of the std deviation of error `e`. `RSE = sqrt(RSS/(n-2)`. It is a measure of lack of fit of the model. Large deviations of estimates from data will result in high RSE. It is measures in units of response.
 * `R^2` statistic is a measure of model fit, i.e., a measure of the linear relationship between response & predictors, similar to correlation. It is the `proportion of variance explained` by model. Is always between `0` and `1` and independent of scale of response. `R^2 = 1 - (RSS/TSS)`. Good `R^2` value depends on application. For simple linear regression, `R^2` = correlation, but not for multiple linear regression.
 
 
 * In multiple linear regression, model coefficient of a covariate represents the average effect on response of increasing the covariate by one unit *while holding all other covariates fixed*


### Problems

* **Non-linearity** - Use residual plots to identify non-linearity in relationship between response & covariates (Residuals (Y-axis) vs. Fitted values (X-axis). There should be no discernable pattern. If non-linear pattern exists, use a non-linear transformation like `log(X)`, `sqrt(X)`, `X^2`, etc. on covariates.
* **Correlated errors** - Std errors for model coefficients assume errors are uncorrelated. If errors are correlated, std errors of model coefficients will be underestimated and confidence/prediction intervals will be incorrectly narrower. usually occurs in time series data. To determine, plot residuals vs. observation (by time). There should be no discernable pattern.
* **Non-constant variance of errors** - Std errors, confidence intervals & hypothesis tests assume constant variance of errors. Again, plot residuals vs. fitted values. If funnel shape, transform response with concave function like `log(Y)` or `sqrt(Y)`. In other cases, can use weighted least squares.
* **Outliers** - Outlier := point far from the value predicted by model, i.e., response is unusual given covariates. To find outliers, plot residuals vs. fitted values. Alternatively, plot studentized residuals (residuals / std error) vs. fitted values. Points with |studentized residuals| > 3 are outliers.
* **High leverage** - Points with unusual values for covariates. Can affect regression line. Use `leverage statistic` to identify high-leverage points. This statistic is always between `1` & `1/n` and average is always `(p+1)/n`. Plot studentized residuals vs. leverage.
* **Collinearity** - 2 or more covariates are highly correlated. Increases std error of estimates of model coefficients and reduces power of hypothesis tests. Multicollinearity => 3 or more covariates are correlated. Use `variance inflation factor` to detect multicollinearity. To remove collinearity, drop of of the affected covariates or created a new covariates based on collinear covariates.

### Compare to non-parametric regression (like KNN regression)
* *Parametric* methods like linear regression assume a functional form for `f(X)`. Simplify the process of finding `f(X)` and only a few model coefficients need to be estimated. Can also be easy to interpret some times. But if assumed functional form is wrong, then model fit will be poor. Use parametric method if its form is close to true form of `f(X)`.
* *Non-parametric* methods do not assume any functional form and are therefore more flexible. But need a lot more data to get a good fit. E.g., K-nearest neighbor regression, where, given `K` and set of covariates `x_0`, get the `K` training data points with covariates closest to `x_0` and average their response to give response for new set of covariates. *Bias-variance trade-off* determines optimal value of `K`.
* `KNN` regression decreases in performance with increase in number of covariates `p`, since there might be no near neighbors, forcing KNN regression to use covariate sets far from the set for which response needs to be predicted. 
* Generally, parametric methods will outperform non-parametric methods when there is a small number of data points per covariate. Parametric methods can be easier to interpret even when a large amount of data is available.

### Ref
* ISLR, Chapter 3


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
