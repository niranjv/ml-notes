# K-Means on Spark (RDD)
# Runs on EMR with Spark 2.1.0 & Hadoop (Amazon 2.7.3)
# Based on example at https://spark.apache.org/docs/latest/mllib-clustering.html#k-means

# WORKS on local - input file is local (.py file is local)
# spark-submit --master local[2] --deploy-mode client pyspark-kmeans-iris.py iris.csv

# WORKS on EMR master - input file on S3 (.py file is local)
# spark-submit --deploy-mode client --master yarn pyspark-kmeans-iris.py s3://com.lifetech.ampliseq.dev.transfer/iris.csv

# WORKS on EMR master - input file on HDFS (.py file is local)
# hadoop fs -put iris.csv
# spark-submit --deploy-mode client --master yarn pyspark-kmeans-iris.py iris.csv

# DOESN'T WORK on EMR master - input file is local (.py file is local)
# spark-submit --deploy-mode client --master yarn pyspark-kmeans-iris.py file:///iris.csv (file:/iris.csv, file:////home/hadoop/iris.csv, file:/home/hadoop/iris.csv)


import sys
from numpy import array
from math import sqrt
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark import SparkContext

try:
    input_file = sys.argv[1] # argv[0] is script name
except IndexError:
    print 'Need to submit input file containing data to cluster'
    exit(1)

# iris.csv is from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# this file is uploaded to the S3 bucket used in sc.textfile() below
# FORMAT:
# 5.1,3.5,1.4,0.2,setosa
# 4.9,3.0,1.4,0.2,setosa
# 4.7,3.2,1.3,0.2,setosa
# 4.6,3.1,1.5,0.2,setosa

sc = SparkContext()
# data = sc.textFile("s3://com.lifetech.ampliseq.dev.transfer/iris.csv") # publically accessible file
data = sc.textFile(input_file) # local file or publicly accessible file in S3
p = data.map(lambda line: array([float(x) for x in line.split(',')[0:4] ]))

# print RDD
for x in p.collect():
    print x

clusters = KMeans.train(p, 3, maxIterations=100, initializationMode="random")

# Get within-cluster sum-of-squares
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = p.map(lambda point: error(point)).reduce(lambda x, y: x + y)

print("Within Set Sum of Squared Error (WSSSE) = " + str(WSSSE))
