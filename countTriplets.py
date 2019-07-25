#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    r2 = defaultdict(int)
    r3 = defaultdict(int)
    count = 0

    for v in arr:
        count += r3[v]
        r3[v*r] += r2[v]
        r2[v*r] += 1
    
    return count
        


if __name__ == '__main__':
    for r, arr in [(2, [1, 2, 2, 4]), (3, [1, 3, 9, 9, 27, 81]), (5, [1, 5, 5, 25, 125])]:
        ans = countTriplets(arr, r)
        print(r)
        print(arr)
        print(ans)
