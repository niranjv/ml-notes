# Contents
* [Overview](#overview)
* [Notebooks](#notebooks)
* Algorithms
 * [K-Means](#k-means)
 * [Gaussian Mixture Models](#gaussian-mixture-models)
 * [Hierarchical Clustering](#hierarhical-clustering)
 * [Affinity Propagation](#affinity-propagation)
 * [Mean Shift](#mean-shift)
 * [Spectral Clustering](#spectral-clustering)
 * [DBSCAN](#dbscan)
 * [Birch](#birch)
 * [Power Iteration Clustering](#power-iteration-clustering)
* [Evaluation Metrics for Clustering](#evaluation-metrics-for-clustering)
* [References](#references)

## Overview
* Purpose: Find sub-groups/clusters in data by partitioning into groups s.t. samples within groups are more similar to each compared to samples in other group
* Unsupervised learning since no labelled data is available; training data consists only of features
* Output is a cluster/class for each sample.

## Notebooks
* [K-Means - ideal case](kmeans-ideal-blobs.ipynb)
* [K-Means vs GMMs - Iris](kmeans-vs-gmm-iris.ipynb)

## K-Means
* Group samples into `K` distinct non-overlapping clusters to minimize within-cluster variation (sum of squares from cluster center)

**Lloyd's Algorithm for KMeans**
* Assign some points to be cluster centers (randomly or using k-means++)
* **E-step:** Assign each of the remaining points to one of the clusters based on whichever cluster has the lowest within-cluster sum of squares (same as Euclidean distance => assign to 'nearest' cluster).
* **M-step:** After all points have been assigned, re-compute centroid of each cluster as its mean
* Repeat until point assignments don't change or max number of iterations has been reached
* Results in a Voronoi diagram with linear decision boundaries

**K-Means Assumptions**
* Data has only K clusters
* Clusgters are spherical with similar variance
* Clusters have similar size
* Sum of Squared Errors (variance) is an appropriate clustering metric for the data
* All clusters are equally likely

**K-Means TODO**

Examine performance when K-Means assumptions are violated:
* No assumption violations - optimal cluster size (plot # clusters vs. dispersion/inertia)
* Similar cluster size/variance violation - Unequal spherical cluster size - 1 small cluster with low variance, 1 large cluster with high variance
* Similar cluster size violation - Unequal spherical cluster size - Mickey mouse clusters (https://en.wikipedia.org/wiki/K-means_clustering#/media/File:ClusterAnalysis_Mouse.svg)
* Isotropic variance violation - Elongated (non-spherical) clusters
* Isotropic variance violation - 2 half-moons
* Well-separated clusters violation - Uniform data
* MiniBatchKMeans vs KMeans on various data sets (when does MiniBatchKMeans perform better/worse?)

**Implementations**
* scikit-learn:
* R: `kmeans`
* Spark: `KMeans`, `KMeansModel`

## Gaussian Mixture Models
* Fit GMM to training data (assumes data is generated from a mixture of finite number of Gaussian distributions with unknown params)
* **Implementations**
 * scikit-learn: Gaussian Mixture Models
 * Spark: `GaussianMixture`, `GaussianMixtureModel`

 **GMMs vs KMeans**
 * In K-Means, a point is either in or not in a cluster
 * GMMs can assign probability of a point belonging to a cluster
 * GMMs can be considered as a generalization of K-Means
 * Expectation-Maximization is a generalization of both K-Means and GMMs
 * **Implementations**
  * scikit-learn: KMeans, Mini-batch K-Means
  * Spark: `KMeans`, `BisectingKMeans`, `StreamingKMeans` (generalization of mini-batch K-Means)


## Hierarchical Clustering
 * Can be agglomerative (bottom-up) or divisive (top-down) like bisecting K-Means
 * Build nested clusters by merging or splitting them successively
 * Generates all possible clusters from 1 to `n` in a `dendrogram`
**Implementations**
* R: `hclust`, `cutree`
* Spark: `BisectingKMeans`

## Affinity Propagation
* Creates clusters by sending messages between pairs of samples until convergence

## Mean Shift
* Discover blobs in smooth density of samples

## Spectral Clustering
* Low-dim embed affinity matrix between samples, followed by K-Means in low-dim space

## DBSCAN
* View clusters as area of high density separated by areas of low density

## Birch
* Builds a `Characteristic Feature Tree (CFT)` for training data

## Power Iteration Clustering
* **Implementations**
 * Spark: `PowerIterationClustering`

## Evaluation Metrics for Clustering
 * Adjusted Rand index
 * Mutual Information-based scores
 * Homogeneity, completeness & V-measure
 * Fowlkes-Mallows scores
 * Silhouette coefficient
 * Calinski-Harabaz Index

## References
* _An Introduction to Statistical Learning with Applications in R_, Daniela Witten, Gareth James, Robert Tibshirani, and Trevor Hastie, 2013, Chap 10
