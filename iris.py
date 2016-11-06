# Explorations of the Iris data set

from sklearn import datasets

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

