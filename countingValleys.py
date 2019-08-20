#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    prev = 0
    num_valleys = 0
    for step in s:
        altitude = prev + 1 if step=='U' else prev - 1
        if altitude == 0 and prev < 0:
            num_valleys += 1
        prev = altitude
    
    return num_valleys


if __name__ == '__main__':
    s = "DDUUUUDD"
    n = len(s)
    result = countingValleys(n, s)
    print(result)
    s = "DDUUUUDDDDUU"
    n = len(s)
    result = countingValleys(n, s)
    print(result)