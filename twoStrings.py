#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d = dict()
    for c in s1:
        d[c] = True
    
    for c in s2:
        if c in d:
            return "YES"

    return "NO"
        

if __name__ == '__main__':
    s1 = "hello"
    s2 = "world"
    result = twoStrings(s1, s2)
    print(result)
    s1 = "hi"
    s2 = "world"
    result = twoStrings(s1, s2)
    print(result)