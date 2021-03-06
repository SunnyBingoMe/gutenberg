import sys, re
from random import random
from operator import add
from pyspark import SparkContext, SparkConf
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
from pyspark.mllib.linalg import SparseVector
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.mllib.linalg import SparseVector

if __name__ == "__main__":
    sc = SparkContext(appName="gutenberg")
    cluster_k_nr = 480
    docsDir = '/mnt/nfsMountPoint/datasets/gutenberg_data/Gutenberg_2G_3k/txt/'
    outputPathPrefix = '/mnt/nfsMountPoint/datasets/gutenberg_data/tfidf_3k_output'
    if len(sys.argv) > 1:
        cluster_k_nr = int(sys.argv[1])
    if len(sys.argv) > 2:
        docsDir = sys.argv[2]
    if len(sys.argv) > 3:
        outputPathPrefix = sys.argv[3]
    outputPath = outputPathPrefix + '_k' + str(cluster_k_nr) + '.txt'
    #print(docsDir, outputPath)
    files = sc.wholeTextFiles(docsDir)
    names = files.keys()
    documents = files.values().map(lambda doc: re.split('\W+', doc))
    hashingTF = HashingTF(1500)
    tf = hashingTF.transform(documents)
    idf = IDF(minDocFreq=2).fit(tf)
    tfidf = idf.transform(tf)
    clusters = KMeans.train(tfidf, cluster_k_nr, maxIterations=450)

    #membership2 = []
    #sparse_data = tfidf.collect()
    #words_map = {}
    #for i in range(len(sparse_data)):
    #    clusterid = clusters.predict(sparse_data[i])
    #    membership2.append(clusterid)
        #print('cluster id: %d') % clusterid
    #names = names.collect()
    #dictionary = dict(zip(names, membership2))
    clusterid = clusters.predict(tfidf).collect()
    names = names.collect()
    dictionary = dict(zip(names, clusterid))
    #print(dictionary)
   
    d = sc.parallelize(dictionary.items())
    d.saveAsTextFile(outputPath)
    sc.stop()

