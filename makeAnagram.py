#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict_a = defaultdict(int) # O(n)
    dict_b = defaultdict(int)
    for c in a: dict_a[c] += 1
    for c in b: dict_b[c] += 1
    count_same = 0
    for key, val in dict_a.items():
        count_same += min(dict_b[key], val)
    count = len(a) + len(b) - count_same * 2 
    return count

if __name__ == '__main__':
    a = "cde"
    b = "abc"
    res = makeAnagram(a, b)
    print(res)