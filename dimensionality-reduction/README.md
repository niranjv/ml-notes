# Contents
* [Overview](#overview)
* [Notebooks](#notebooks)
* [Principal Components Analysis](#principal-components-analysis)
* [Partial Least Squares](#partial-least-squares)
* [Factor Analysis](#factor-analysis)
* [Singular Value Decomposition](#singular-value-decomposition)
* [Projection Pursuit](#projection-pursuit)
* [Multi-Dimensional Scaling](#multi-dimensional-scaling)
* [Linear Discriminant Analysis](#linear-discriminant-analysis)
* [Partial Least Squares Discriminant Analysis](#oartial-least-squares-discriminant-analysis)
* [Mixture Discriminant Analysis](#mixture-discriminant-analysis)
* [Quadratic Discriminant Analysis](#quadratic-discriminant-analysis)
* [Regularized Discriminant Analysis](#regularized-discriminant-analysis)
* [Manifold Learning](#manifold-learning)
* [Random Projections](#random-projections)
* [Feature Agglomeration](#feature-agglomeration)
* [Non-Negative Matrix Factorization](#non-negative-matrix-factorization)
* [Independent Components Analysis](#independent-component-analysis)
* [Latent Dirichlet Allocation](#latent-dirichlet-allocation)
* [References](#references)

## Overview
* Dimensionality reduction is the process of reducing the number of features under consideration to a set of principal features.
* The transformation can be linear (PCA) or non-linear (manifold learning)
* Advantages:
 * Reduce time and storage space required
 * Removal of multi-collinearity
 * Easier to visualize data
* Disadvantages:
 * Response variable is not always considered in feature extraction/dimensionality reduction
 
## Notebooks
* PCA when `n` < `p` 

## Principal Components Analysis
* Orthogonal linear transformation to convert a set of possibly correlated features to a smaller set of linearly uncorrelated variables (*Principal Components*), all orthogonal to each other
* Re-express data set in the most meaningful basis that will filter out noise and reveal hidden structure
* **linear** combination of original basis => change of basis to a new basis
* `PX = Y` where row vectors of P are PCs of X
* row vectors of `P` are the eigen vectors of `XX'/n` => this diagonalizes covariance matrix of new variables
* Focus of PCA is on variance of features (common & unique) and seeks to reproduce total variance of features; PCs best capture the variance of the features
* PCA's focus is on diagonal terms of correlation matrix
* 1st PC accounts for as much variance as possible
* 2nd PC accounts for as much of the remaining variation as possible (subject to being orthogonal to the 1st component) and so on
* Number of PCs <= number of features
* PCs form the orthogonal basis set of features
* PCs are functions of the the eigen vectors of the covariance matrix; they can be used to re-construct most of the variance of the original data
* Kernel PCA is used to do non-linear dimensionality reduction
* Multiple correspondence analysis is an equivalent of PCA for categorical data
* **Assumptions:**
 * non-parametric
 * Linearity => change of basis for feature space
 * Large variances => PCs with large variances represent important structure in feature space => high SNR
 * Orthogonal components => Lower redundancy; easy way to calculate *P*
* **Solutions:**
  * PCA is always done on mean-centered features
  * via Eigenvector decomposition of covariance matrix of features
  * via Singular Value Decomposition of data matrix of features
* **Advantages:**
 * Minimize redundancy (based on covariance of feature matrix) by removing correlated features
 * Increase signal-to-noise ratio (based on variance of feature matrix)
 * In regression, if large number of possibly correlated features are present, run PCA first and then regress on the first few PCs
 * If data is noisy, running PCA helps to concentrate more of total variance of data in first few PCs, which is proportionally higher than noise variance (which is same as in original data). This increases signal-to-noise ration of of the first few PCs.
 * Useful for visualization
* **Disadvantages:**
 * Only removes 2nd order dependencies (which is sufficient for data sets with Gaussian distribution); does not remove higher-order dependencies (in non-Gaussian data); need to use kernel PCA or ICA for this
 * Does not consider response while reducing dimension of features
 * Sensitive to relative scaling of original features
* **Implementations**
 * scikit-learn: Exact PCA, Incremental PCA, Kernel PCA, Sparse PCA, Mini Batch Sparse PCA
 * R: `prcomp()`, `princomp()`, `psych.principal()`
 * Spark: PCA

## Partial Least Squares
 * Supervised dimensionality reduction
 * Looks for projections having highest covariance with group labels

## Factor Analysis
* Focus of Factor Analysis (FA) is on correlations
* FA generates new variables that are linear combinations of features and seeks to reproduce inter-correlation between variables
* Factors represent the common variance of features, excluding unique variance
* Factors are latent unmeasured variables that express themselves through their relationship with other measured variables
* FA is a measurement model of a latent feature (different from PCA which is just a linear combination of features)
* FA allows for investigation of relationship between variables
* As many factors as there are variables; select the factors with the largest eigenvalues as they explain more of the variance than the remaining factors
* Factor loadings measure strength of relationship between a measured variable and the unmeasured latent variable
* Focus is on off-diagonal terms of correlation matrix
* FA is used when purpose is detect data structure or for causal modeling
* Both PCA & FA estimate a Gaussian with a low-rank covariance matrix (with Gaussian priors on the latent variables). Non-gaussian priors on latent variables leads to Independent Component Analysis.
* Advantage over PCA: can model variance of every component independently which leads to better approximation of original data when components have different variances
* Components generated by FA have no general structure (i.e., don't have to be orthogonal like PCA)
* Assumptions:
 * Multiple measured variables have similar patterns because of their correlation with an unmeasured latent variable
 * **Implementations**
  * scikit-learn: factor-analysis
  * R: `stats.factanal`, `psych.factor.pa`, `FactoMineR` package, `GPARotation` package

## Independent Components Analysis
 * Non-linear decomposition of mixed signal into additive components
 * Typically used for separating mixed signals, not dimension reduction
 * No noise term in model, so whitening must be applied
 * **Implementations**
  * scikit-learn: Fast ICA


## Singular Value Decomposition
* **Implementations**
 * scikit-learn: TruncatedSVD
 * Spark: SVD

## Projection Pursuit
* ?

## Multi-Dimensional Scaling
* ?

## Linear Discriminant Analysis
* Supervised dimensionality reduction (i.e., takes into account the response/label)
* Generalizations of Fisher's linear discriminant
* Finds a linear combination of features to separate 2 or more classes
* Looks for projections having highest correlation with dummy variables encoding group labels
* Special case of Canonical Correlation Analysis

## Partial Least Squares Discriminant Analysis
* ?

## Mixture Discriminant Analysis
* ?

## Quadratic Discriminant Analysis
* ?

## Regularized Discriminant Analysis
* ?

## Manifold Learning
* Non-linear mapping of features to lower-dimensional space
* Many approaches available such as Isomap, Local Linear Embedding, Hessian Eigenmapping, Spectral Embedding, Local Tangent Space Alignment, t-distributed Stochastic Neighbor Embedding, etc.
* These approaches construct a lower-dimensional representation of data using a cost function that retains local properties of the data

## Random Projections
* ?

## Feature Agglomeration
* ?

## Non-Negative Matrix Factorization
* **Implementations**
 * scikit-learn: NMF

## Latent Dirichlet Allocation
* **Implementations**
 * scikit-learn: LatentDirichletAllocation

## References
* [A Tutorial on Principal Components Analysis](https://arxiv.org/abs/1404.1100), Jonathon Shlens, 2014
* [A Tutorial on Principal Components Analysis](http://courses.cs.washington.edu/courses/cse528/07sp/pca.pdf), Lindsay I Smith, 2002
* [Principal Components Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis), Wikipedia, Jan 2017
* [A Tutorial on Independent Components Analysis](https://arxiv.org/abs/1404.2986), Jonathon Shlens, 2014
* [A Survey of Dimensionality Reduction Techniques](http://computation.llnl.gov/casc/sapphire/pubs/148494.pdf), Imola K Fodor, LLNL technote
* [Bayesian PCA](https://www.microsoft.com/en-us/research/publication/bayesian-pca/), Christopher Bishop, NIPS 1998
* [Quick-R: PCA & Factor Analysis in R](http://www.statmethods.net/advstats/factor.html)
* [Analysis Factor: A Short Introduction to Factor Analysis](#http://www.theanalysisfactor.com/factor-analysis-1-introduction/_)
* [Analysis Factor: Difference between PCA & FA](http://www.theanalysisfactor.com/the-fundamental-difference-between-principal-component-analysis-and-factor-analysis/)
