#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 2)
    for start, end, value in queries:
        arr[start] += value
        arr[end + 1] -= value

    max_val = 0
    for val in arr:
        if val > 0:
            max_val += val
    return max_val

if __name__ == '__main__':
    n = 5
    queries = [[1, 2, 100],
               [2, 5, 100],
               [3, 4, 100]]
    result = arrayManipulation(n, queries)
    print(result)