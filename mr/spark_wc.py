# -*- coding: utf-8 -*-

"""

@author: lizongxing 
@time: 2019/1/30
@file: spark_wc.py 
@software: PyCharm 
@desc: 

"""

from mrjob.job import MRJob
from operator import add


class SparkWC(MRJob):
    def spark(self, input_path, output_path):
        from pyspark import SparkContext
        sc = SparkContext(appName='spark_wordcount')
        lines = sc.textFile(input_path)

        count = lines.flatMap(lambda line: line.split()).map(lambda word: (word.lower(), 1)).reduceByKey(add)
        count.saveAsTextFile(output_path)
        sc.stop()

if __name__ == '__main__':
    SparkWC.run()
    # print