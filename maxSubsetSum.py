#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n = len(arr)
    if n <= 0:
        return 0
    if n == 1:
        return arr[0]

    max_sum = [0] * n
    max_sum[0] = arr[0]
    max_sum[1] = max(arr[0], arr[1])

    for i in range(2, n):
        max_sum[i] = max(arr[i], max_sum[i-1], arr[i] + max_sum[i-2])
    return max_sum[i]
                

if __name__ == '__main__':
    arr = [2,-1,-3,4,-5]
    res = maxSubsetSum(arr)
    print(res)
