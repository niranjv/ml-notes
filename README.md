# python
My experiments with python, numpy/pandas, scikit-learn, matplotlib/seaborn, ipython/jupyter


## K-Means

### Assumptions
* Data has only K clusters
* Spherical clusters
* Clusters of similar size
* All clusters have similar variance
* All clusters have similar scale
* Sum of Squared Errors is an appropriate clustering metric for the data
* All clusters are equally likely

### Comparison with Gaussian Mixture Models
* In K-Means, a point is either in or not in a cluster 
* GMMs can assign probability of a point belonging to a cluster
* GMMs can be considered as a generalization of K-Means
* Expectation-Maximization is a generalization of both K-Means and GMMs
