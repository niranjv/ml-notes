## Lloyd's Algorithm for KMeans
* Assign some points to be cluster centers (randomly or using k-means++)
* **E-step:** Assign each of the remaining points to one of the clusters based on whichever cluster has the lowest within-cluster sum of squares (same as Euclidean distance => assign to 'nearest' cluster).
* **M-step:** After all points have been assigned, re-compute centroid of each cluster as its mean
* Repeat until point assignments don't change or max number of iterations has been reached
* Results in a Voronoi diagram with linear decision boundaries

## K-Means Assumptions
* Data has only K clusters
* Clusgters are spherical with similar variance
* Clusters have similar size
* Sum of Squared Errors (variance) is an appropriate clustering metric for the data
* All clusters are equally likely

## K-Means TODO
Examine performance when K-Means assumptions are violated:
* No assumption violations - optimal cluster size (plot # clusters vs. dispersion/inertia)
* Similar cluster size/variance violation - Unequal spherical cluster size - 1 small cluster with low variance, 1 large cluster with high variance
* Similar cluster size violation - Unequal spherical cluster size - Mickey mouse clusters (https://en.wikipedia.org/wiki/K-means_clustering#/media/File:ClusterAnalysis_Mouse.svg)
* Isotropic variance violation - Elongated (non-spherical) clusters
* Isotropic variance violation - 2 half-moons
* Well-separated clusters violation - Uniform data
* MiniBatchKMeans vs KMeans on various data sets (when does MiniBatchKMeans perform better/worse?)

## Comparison with Gaussian Mixture Models
* In K-Means, a point is either in or not in a cluster
* GMMs can assign probability of a point belonging to a cluster
* GMMs can be considered as a generalization of K-Means
* Expectation-Maximization is a generalization of both K-Means and GMMs
