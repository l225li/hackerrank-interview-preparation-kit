#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr = sorted(arr)
    if len(arr) < 2:
        return 0
    i = 0
    j = 1
    count = 0
    while i < j and j < len(arr):
        diff = arr[j] - arr[i]
        if diff == k:
            count += 1
            i += 1
            j += 1
        elif diff < k:
            j += 1
        else:
            i += 1
    return count

if __name__ == '__main__':
    arr = [1, 5, 3, 4, 2]
    k = 2  
    result = pairs(k, arr)
    print(result)