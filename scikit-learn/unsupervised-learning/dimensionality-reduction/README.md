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
* Orthogonal linear transformation to convert a set of possibly correlated features to a smaller set of linearly uncorrelated features called principal components
* Principal components best capture the variance of original set of features
* 1st principal component accounts for as much variance as possible
* 2nd principal component accounts for as much of the remaining variation as possible (subject to being orthogonal to the 1st component) and so on
* Number of principal components <= number of features
* Principal components form the orthogonal basis set of features
* Principal components are the eigen vectors associated with the largest eigen values of the covariance matrix; they can be used to re-construct most of the variance of the original data
* They are obtained via eigen value decomposition of covariance matrix or SVD of data matrix (after mean-centering & normalization)
* Kernel PCA is used to do non-linear dimensionality reduction
* Advantages:
 * ?
* Disadvantages:
 * Does not consider response while reducing dimension of features
 * Sensitive to relative scaling of original features

## Linear Discriminant Analysis (LDA)
* Generalizations of Fisher's linear Discriminant
* Finds a linear combination of features to separate 2 or more classes


## Manifold Learning
* Non-linear mapping of features to lower-dimensional space
* Many approaches available such as Isomap, Local Linear Embedding, Hessian Eigenmapping, Spectral Embedding, Local Tangent Space Alignment, t-distributed Stochastic Neighbor Embedding, etc.
* These approaches construct a lower-dimensional representation of data using a cost function that retains local properties of the data

## Random Projections
* ?

## Feature agglomeration
* ?
