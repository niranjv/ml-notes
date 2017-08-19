Variables names
* trailing underscore in attribute name (e..g, `labels_`) => attribute value is available only after fitting model to data, i.e., it is an estimated or fitted attribute

scikit-learn Clustering details:
* `fit()` - fit model to data & determine model parameters
* `labels_` - return learned clusters for training data
* `predict()` - predict clusters for new data. Not available for all algorithms (in which case use `fit_predict()`)


Ref: 
* [Scikit-learn tutorial](http://nbviewer.jupyter.org/github/jakevdp/sklearn_tutorial/blob/master/notebooks/Index.ipynb)