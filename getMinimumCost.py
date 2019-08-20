#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c = sorted(c, reverse=True)
    total = 0
    for i, price in enumerate(c):
        total += price * (i // k + 1)
    return total 

if __name__ == '__main__':
    k = 3
    c = [1, 3, 5, 7, 9]
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)