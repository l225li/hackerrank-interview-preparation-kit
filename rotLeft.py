#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]

if __name__ == '__main__':
    a = [1,2,3,4,5]
    n = len(a)
    d = 3
    result = rotLeft(a, d)
    print(result)