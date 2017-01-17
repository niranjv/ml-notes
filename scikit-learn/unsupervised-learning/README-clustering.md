## Overview
* Clustering is unsupervised learning since no labelled data is available; training data consists only of features; output is a cluster/class for each sample.
* See [Clustering guide](http://scikit-learn.org/stable/modules/clustering.html) for types of clustering algorithms available in scikit-learn and when to use them. Algorithms include:
 * **K-Means** - Group samples into clusters to minimize within-cluster sum of squares from cluster center. **Mini-batch K-Means** uses small batches to reduce computation time.
 * **Affinity propagation** - Creates clusters by sending messages between pairs of samples until convergence
 * **Mean Shift** - Discover blobs in smooth density of samples
 * **Spectral clustering** - Low-dim embed affinity matrix between samples, followed by K-Means in low-dim space
 * **Hierarchical clustering / Agglomerative clustering** - Build nested clusters by merging or splitting them successively
 * **Gaussian mixtures** - Fit GMM to training data (assumes data is generated from a mixture of finite number of Gaussian distributions with unknown params)
 * **DBSCAN** - View clusters as area of high density separated by areas of low density
 * **Birch** - Builds a `Characteristic Feature Tree (CFT)` for training data
* `fit()` - learn clusters from training data
* `labels_` - return learned clusters for training data (trailing underscore in attribute name `=>` attribute value is available only after fitting model to training data, i.e., it is an estimated or fitted attribute)
* `predict()` - predict clusters for new data. Not available for all algorithms (in which case use `fit_predict()`)

## Clustering Evaluation metrics
* Adjusted Rand index
* Mutual Information-based scores
* Homogeneity, completeness & V-measure
* Fowlkes-Mallows scores
* Silhouette coefficient
* Calinski-Harabaz Index
