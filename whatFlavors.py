#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left


# Complete the whatFlavors function below.
def findIndices(arr, e1, e2):
    pos1 = arr.index(e1)
    if e1 == e2:
        pos2 = [i for i, c in enumerate(arr) if c == e2 and i != pos1][0]
    else:
        pos2 = arr.index(e2)

    return "{} {}".format(*sorted([pos1 + 1, pos2 + 1]))


def whatFlavors(cost, money):
    sorted_cost = sorted(cost)
    for i, c in enumerate(sorted_cost):
        match = money - c
        pos = bisect_left(sorted_cost, match, lo=i + 1)
        if pos != len(cost) and sorted_cost[pos] == match:
            print(findIndices(cost, c, match))


if __name__ == '__main__':
    cost = [4, 3, 2, 5, 7]
    money = 8
    result = whatFlavors(cost, money)