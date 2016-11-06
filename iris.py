# Explorations of the Iris data set

from sklearn import datasets
from sklearn.decomposition import PCA

import matplotlib.pyplot as p

iris = datasets.load_iris()

dir(iris)
# ['DESCR', 'data', 'feature_names', 'target', 'target_names']

iris.data.shape
# (150, 4)

iris.data[0:5]
# array([[ 5.1,  3.5,  1.4,  0.2],
#       [ 4.9,  3. ,  1.4,  0.2],
#       [ 4.7,  3.2,  1.3,  0.2],
#       [ 4.6,  3.1,  1.5,  0.2],
#       [ 5. ,  3.6,  1.4,  0.2]])

iris.feature_names
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

iris.target_names
# array(['setosa', 'versicolor', 'virginica'], 
#      dtype='|S10')

iris.target[0:5]
# array([0, 0, 0, 0, 0])


x = iris.data
y = iris.target


# ----------
# PCA
# ----------

pca = PCA(n_components=2)
comp = pca.fit(x).transform(x)

p.figure()
colors = ['red', 'green', 'blue']

for col, i, target_name in zip(colors, [0,1,2], iris.target_names):
	p.scatter(comp[y==i,0], comp[y==i,1], color=col, label=target_name)

p.title('PCA of Iris dataset')
p.legend(loc='best', shadow=False, scatterpoints=1)
p.show()

