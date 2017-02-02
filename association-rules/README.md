Association rule learning - discover 'interesting' relations between variables

## Problems
* Association Rules (with confidence score)
 * Order of items is not considered
* Sequential pattern mining
 * Order of items matters

## Metrics
* Support
* Confidence
* Lift
* Conviction

## Algorithms
* FP-growth - find frequent itemsets without traversing all possible itemsets
* Apriori
* Eclat - Equivalence Class Transformation
* PrefixSpan - for sequential pattern mining


## Tools
* Spark
* R
* Python

## References
* FP-Growth algorithm: [Mining frequent patterns without candidate generation](https://dx.doi.org/10.1145%2F342009.335372), Han, et al., 2000, SIGMOD
* Parallel FP-Growth: [PFP - Parallel FP-Growth for Query Recommendation](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/34668.pdf)
* Apriori algorithm: [Fast Algorithms for Mining Association Rules](http://rakesh.agrawal-family.com/papers/vldb94apriori.pdf)
* PrefixSpan algorithm: [Mining sequential patterns by pattern-growth: the PrefixSpan approach](https://www.cs.sfu.ca/~jpei/publications/span.pdf)
* Spark docs, Feb 2017: [Frequent Pattern Mining - RDD-based API](http://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
* Databricks blog, Apr 2015: [New MLlib Algorithms in Apache Spark 1.3: FP-Growth and Power Iteration Clustering](https://databricks.com/blog/2015/04/17/new-mllib-algorithms-in-spark-1-3-fp-growth-and-power-iteration-clustering.html)
