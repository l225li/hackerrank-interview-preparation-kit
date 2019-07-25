#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    freq = defaultdict(int)
    cnt = defaultdict(int)
    output = []
    for action, val in queries:
        if action == 1:
            cnt[ freq[val] ] -= 1
            freq[val] += 1
            cnt[ freq[val] ] += 1
        elif action == 2:
            if freq[val] > 0:
                cnt[ freq[val] ] -= 1
                freq[val] -= 1
                cnt[ freq[val] ] += 1
        else:
            output.append(int(cnt[val]))
    return output




if __name__ == '__main__':
    queries = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]
    # queries = [(2, 2), (2, 2), (2, 3)]
    result = freqQuery(queries)
    print(result)