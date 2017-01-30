## Task
Explore regression in scikit-learn

## Topics
* [OLS vs. Ridge Regression (CV) vs. LASSO (CV) vs. Elastic Net (CV)](OLS vs Ridge_CV vs LASSO_CV vs ElasticNet_CV.ipynb)
* Ridge Regression (CV) vs. Bayesian Linear Regression with Normal prior
* LASSO regression (CV) vs. Bayesian Linear Regression with double Exponential (Laplace) prior
* Least Angle Regression (LARS)
* Principal Component Regression (if features are correlated, run PCA first and then regress on a few PCs)
* Bayesian regression
* Logistic regression
* Stochastic Gradient Descent

Notes:
* Ridge regression and LASSO are forms of penalized estimation. They introduce bias into estimation of model parameters to reduce variance of estimate. They have lower MSE than OLS when multi-collinearity is present. These methods are used mainly for prediction and not for inference since it is difficult to account for bias

## References
* [scikit-learn Generalized Linear Models](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model)
* [Wikipedia - Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)
* Numerical Python, Robert Johansson, APress, 2015
