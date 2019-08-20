#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import insort

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests = sorted(contests, reverse=True)
    total = 0
    for luck, impt in contests:
        if not impt:
            total += luck
        elif k > 0:
            total += luck
            k -= 1
        else:
            total -= luck
    return total


if __name__ == '__main__':
    contests = [[5, 1], [2, 1],
                [1, 1], [8, 1],
                [10, 0], [5, 0]]
    k = 3
    result = luckBalance(k, contests)
    print(result)
