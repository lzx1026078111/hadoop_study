# -*- coding: utf-8 -*-

"""

@author: lizongxing 
@time: 2019/1/30
@file: wordcount.py 
@software: PyCharm 
@desc: 

"""

from mrjob.job import MRJob


class WordCountJob(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            yield word.lower(), 1

    def reducer(self, key, values):
        yield (key, sum(values))


if __name__ == '__main__':
    WordCountJob.run()
