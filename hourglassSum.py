#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = None
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            sum_glass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if (max_sum is None) or (sum_glass > max_sum): 
                max_sum = sum_glass
                print(max_sum)
    return max_sum

if __name__ == '__main__':
    arr_s = """
   -1 1 -1 0 0 0
0 -1 0 0 0 0
-1 -1 -1 0 0 0
0 -9 2 -4 -4 0
-7 0 0 -2 0 0
0 0 -1 -2 -4 0"""
    arr = list(map(int, arr_s.rstrip().split()))
    arr = np.array(arr)
    arr = arr.reshape(6,6)
    print(arr)
    arr = arr.tolist()
    print(arr)
    result = hourglassSum(arr)
    print(result)

