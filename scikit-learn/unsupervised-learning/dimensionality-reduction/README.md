## Overview
* Dimensionality reduction is the process of reducing the number of features under consideration to a set of principal features.
* The transformation can be linear (PCA) or non-linear (manifold learning)
* Advantages:
 * Reduce time and storage space required
 * Removal of multi-collinearity
 * Easier to visualize data
* Disadvantages:
 * Response variable is not always considered in feature extraction/dimensionality reduction

## Principal Components Analysis (PCA)
* Orthogonal linear transformation to convert a set of possibly correlated features to a smaller set of linearly uncorrelated variables all orthogonal to each other called principal components
* Focus of PCA is on variance of features (common & unique) and seeks to reproduce total variance of features; PCs best capture the variance of the features
* PCA's focus is on diagonal terms of correlation matrix
* 1st PC accounts for as much variance as possible
* 2nd PC accounts for as much of the remaining variation as possible (subject to being orthogonal to the 1st component) and so on
* Number of PCs <= number of features
* PCs form the orthogonal basis set of features
* PCs are functions of the the eigen vectors of the covariance matrix; they can be used to re-construct most of the variance of the original data
* They are obtained via eigen value decomposition of covariance matrix or SVD of data matrix (after mean-centering & normalization)
* Kernel PCA is used to do non-linear dimensionality reduction
* Multiple correspondence analysis is an equivalent of PCA for categorical data
* Advantages:
 * In regression, if large number of possibly correlated features are present, run PCA first and then regress on the first few PCs
 * If data is noisy, running PCA helps to concentrate more of total variance of data in first few PCs, which is proportionally higher than noise variance (which is same as in original data). This increases signal-to-noise ration of of the first few PCs.
 * Useful for visualization
* Disadvantages:
 * Does not consider response while reducing dimension of features
 * Sensitive to relative scaling of original features

## Linear Discriminant Analysis (LDA)
* Supervised dimensionality reduction (i.e., takes into account the response/label)
* Generalizations of Fisher's linear discriminant
* Finds a linear combination of features to separate 2 or more classes
* Looks for projections having highest correlation with dummy variables encoding group labels
* Special case of Canonical Correlation Analysis

## Factor Analysis
* Focus of Factor Analysis is on correlations
* FA generates new variables that are linear combinations of features and seeks to reproduce inter-correlation between variables
* Factors represent the common variance of features, excluding unique variance
* Focus is on off-diagonal terms of correlation matrix
* FA is used when purpose is detect data structure or for causal modeling


## Partial Least Squares
* Supervised dimensionality reduction
* Looks for projections having highest covariance with group labels

## Manifold Learning
* Non-linear mapping of features to lower-dimensional space
* Many approaches available such as Isomap, Local Linear Embedding, Hessian Eigenmapping, Spectral Embedding, Local Tangent Space Alignment, t-distributed Stochastic Neighbor Embedding, etc.
* These approaches construct a lower-dimensional representation of data using a cost function that retains local properties of the data

## Random Projections
* ?

## Feature agglomeration
* ?
