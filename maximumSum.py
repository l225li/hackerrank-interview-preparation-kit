#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right, insort

# Complete the maximumSum function below.
def maximumSum(a, m):
    prefix = [0] * len(a)
    curr = 0

    for i, val in enumerate(a):
        curr = (curr + val) % m
        prefix[i] = curr
    
    pq = [prefix[0]]
    max_sum = max(prefix)
    for i, val in enumerate(prefix):
        left = bisect_right(pq, val)
        if left != len(pq):
            mod_sum = (val - pq[left] + m) % m
            max_sum = max(mod_sum, max_sum)
        insort(pq, val)
    return max_sum
    

if __name__ == '__main__':
    a = [3,3,9,9,5]
    m = 7
    result = maximumSum(a, m)
    print(result)