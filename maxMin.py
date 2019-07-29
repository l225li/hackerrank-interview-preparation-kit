#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr = sorted(arr)
    min_unfair = arr[k-1] - arr[0]
    for i in range(1, len(arr)-k+1):
        unfair = arr[i+k-1] - arr[i]
        if unfair < min_unfair:
            min_unfair = unfair
    return min_unfair


if __name__ == '__main__':
    arr = [100, 200, 300, 350, 400, 401, 402]
    k = 3
    result = maxMin(k, arr)
    print(result)
