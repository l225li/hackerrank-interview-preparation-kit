#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    min_diff = min(y - x for x, y in zip(arr, arr[1:]))
    return min_diff

if __name__ == '__main__':
    arr = [1, -3, 71, 68, 17]
    result = minimumAbsoluteDifference(arr)
    print(result)
