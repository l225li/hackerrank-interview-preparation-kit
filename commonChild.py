#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the commonChild function below.
def commonChild(s1, s2):
    n = len(s1) + 1
    m = len(s2) + 1

    arr = [[0] * m for _ in range(m)]

    for i in range(1, n):
        for j in range(1, m):
            if s1[i-1] == s2[j-1]:
                arr[i][j] = 1 + arr[i-1][j-1]
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    
    return arr[-1][-1]

if __name__ == '__main__':
    s1 = "ABCDEF"
    s2 = "FBDAMN"
    result = commonChild(s1, s2)
    print(result)
