# K-Means on Spark (RDD)
# Runs on EMR with Spark 2.1.0 & Hadoop (Amazon 2.7.3)
# Based on example at https://spark.apache.org/docs/latest/mllib-clustering.html#k-means

from numpy import array
from math import sqrt
from pyspark.mllib.clustering import KMeans, KMeansModel

# iris.csv is from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# this file is uploaded to the S3 bucket used in sc.textfile() below
# FORMAT:
# 5.1,3.5,1.4,0.2,setosa
# 4.9,3.0,1.4,0.2,setosa
# 4.7,3.2,1.3,0.2,setosa
# 4.6,3.1,1.5,0.2,setosa

data = sc.textFile("s3n://<<MY_BUCKET>>/iris.csv")
p = data.map(lambda line: array([float(x) for x in line.split(',')[0:4] ]))

# print RDD
for x in p.collect():
    print x

clusters = KMeans.train(p, 3, maxIterations=10, initializationMode="random")

# Get within-cluster sum-of-squares
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = p.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))
