Data set characteristics

* # samples
* # predictors

Response characteristics

* Continuous / Counts / Categorical
* Balanced / Unbalanced

Predictor characteristics

* Continuous / Counts / Categorical
* Correlated
* Mean-centered
* Different scales
* Missing values

Data transformation

* Reduce impact of data skewness, outliers, scale, etc.
* Tree-based methods are insensitive to data characteristics
* Methods like linear regression are not
* Some methods require predictors to be scaled and centered

Methods for individual predictors

* Mean-Centering - subtract mean
* Scaling - divide by std dev
* Used to improve numerical stability but lose interpretability of predictors
* Skewness - skewed data => highest value/lowest value > 20; measures include Pearson's moment coefficient of skewness, sample skewness. Fix by taking log, square root or inverse. Or use Box-Cox transformation which includes log, square-root, square, etc. as special cases. Can only use for predictors with all values > 0.

Methods for multiple predictors

* Outliers - tree-based methods & SVMs are resistant to outliers. Remove by methods like 'spatial sign'. Removing predictors after 'spatial sign' transform is problematic.
* Data Reduction - Unsupervised - PCA: find linear combinations of predictors that capture the most variation. 1st PC captures most variance of all possible linear combinations of predictors, etc. All PCs are uncorrelated with each other. Very useful for methods that required uncorrelated predictors. But PCA does not handle measurement scale or distribution characteristics, so might end up giving higher weights to predictors on a measurement scale with higher variability, which is more a function of measurement scale than inherent variability of predictor. Same with skewness. So transform, center & scale predictors before PCA. Also, PCA does not consider response when summarizing variability.

How many PCs to retain? Use scree plot and also cross-validation. Plot PCs against each other and see if data clusters. Scale of PCs becomes smaller as they account for less variation.

Which predictors are associated with which components? Look at coefficient for predictor in component.

* Data Reduction - Supervised- Partial Least Squares:

Feature selection, Feature engineering

* Feature selection
* Feature engineering
* Feature learning: supervised, unsupervised

Missing data, censored data

* Missing - look at pattern of missing data. Usually affects only some predictors. Sometimes a few samples are affected. If cannot remove predictors or samples, use tree-based methods or impute missing data (use info in training set predictors to estimate values of other predictors). Resampling must include imputation.
K-nearest neighbors can be used to impute missing predictor values. Find samples in training set closest to sample with missing value; replace missing value with average of neighbors. Imputed data will be within training set range; entire training set is required to impute missing value; number of neighbors to use and 'closeness' metric are parameters. Can also use linear regression if predictor with missing values is highly correlated with another predictor with no missing values.

* Censored - missing value but something is known about its value. Make assumptions about censoring mechanism in model or use censoring limit as real value, use random value between 0 and limit, etc.

Data splitting

Need to split data into 3 disjoint sets:
* Training set - Used to building candidate model
* Test set - Used to evaluate performance of candidate model. Can be used repeatedly as candidate model is improved.
* Validation set - Used to select final model from candidate models. Not to be used for tuning model parameters.

* How much data to allocate into each of the above subsets?
* For small data sets, it is better to re-sample than to split the original data set.

Model evaluation

Evaluate model on test set to see how it will perform on previously unseen data
* Qualitative aspects: summary statistics like RMSE
* Quantitative aspects: plot obs. vs. pred. values; discover regions where model predictions are good or bad

Model selection

* Must select between model families (e.g. Linear regression vs. MARS) and within model families (e.g. tuning parameter/# segments in MARS)
* Select final model based on performance of all tuned candidate models on validation set (not test set, which is to be used only for tuning candidate models)
