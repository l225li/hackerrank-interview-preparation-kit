#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    ai, bi, ci, count = 0, 0, 0, 0 
    na, nb, nc = len(a), len(b), len(c)
    while bi < nb:
        while ai < na and a[ai] <= b[bi]:
            ai += 1
        while ci < nc and c[ci] <= b[bi]:
            ci += 1
        count += ai * ci
        bi += 1
    return count


if __name__ == '__main__':

    arra = [1, 3, 5, 7]
    arrb = [5, 7, 9]
    arrc = [7, 9, 11, 13]

    ans = triplets(arra, arrb, arrc)
    print(ans)