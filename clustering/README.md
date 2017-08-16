# Contents
* [Overview](#overview)
* [Investigations](#investigations)
* [References](#references)

# Overview
Explore clustering in scikit-learn, R, Spark MLLib

# Investigations
* Jupyter/sklearn: [K-Means - ideal case](kmeans-ideal-blobs.ipynb)
* Jupyter/sklearn: [K-Means vs GMMs - Iris](kmeans-vs-gmm-iris.ipynb)
* Examine performance when K-Means assumptions are violated:
  * No assumption violations - optimal cluster size (plot # clusters vs. dispersion/inertia)
  * Similar cluster size/variance violation - Unequal spherical cluster size - 1 small cluster with low variance, 1 large cluster with high variance
  * Similar cluster size violation - Unequal spherical cluster size - Mickey mouse clusters (https://en.wikipedia.org/wiki/K-means_clustering#/media/File:ClusterAnalysis_Mouse.svg)
  * Isotropic variance violation - Elongated (non-spherical) clusters
  * Isotropic variance violation - 2 half-moons
  * Well-separated clusters violation - Uniform data
  * MiniBatchKMeans vs KMeans on various data sets (when does MiniBatchKMeans perform better/worse?)

# References
* [Wiki](https://github.com/niranjv/ml-notes/wiki/Clustering)
