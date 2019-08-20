#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    candies = 0
    passes = 0
    
    while candies < n:
        production = m * w
        candies += production % p
        passes += 1
        
    
    return passes

if __name__ == '__main__':
    result = minimumPasses(3, 1, 2, 12)
    print(result)
