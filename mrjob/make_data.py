# -*- coding: utf-8 -*-

"""

@author: lizongxing 
@time: 2019/1/30
@file: make_data.py 
@software: PyCharm 
@desc: 

"""

import argparse
import random

parser = argparse.ArgumentParser()

parser.add_argument('--count', type=int, default=100000)

if __name__ == '__main__':
    t = parser.parse_args()
    words = ['hello', 'hi', 'ni', 'word', 'count', 'jha', 'qowo', 'nasd', 'avuvu', 'cry', '654', 'bvu']
    print t.count
    with open('data.txt', mode='w') as f:
        for i in range(t.count):
            f.write(random.choice(words) + ' ')
            if 0.5 > random.random():
                f.write('\n')
