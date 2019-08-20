#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c)-1:
        if (i + 2 < len(c)) and (c[i + 2] == 0):
            jumps += 1 
            i += 2
        else:
            jumps += 1
            i += 1

    return jumps


if __name__ == '__main__':
    c = [0,0,0,0,1,0,1,0,0,0,1,0]
    result = jumpingOnClouds(c)
    print(result)