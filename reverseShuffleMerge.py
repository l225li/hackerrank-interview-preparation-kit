#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    s = s[::-1]
    s = [ord(c) - ord('a') for c in s]
    T = [0] * 26
    for c in s:
        T[c] += 1
    
    R = [t // 2 for t in T]

    result = []
    
    for c in s:
        T[c] -= 1
        if not R[c]:
            continue

        print(result)
        while result and result[-1] > c and T[result[-1]] > R[result[-1]]:
            R[result[-1]] += 1
            result.pop()

        if R[c]:
            R[c] -= 1
            result.append(c)
    
    return "".join([chr(c + ord('a')) for c in result])

if __name__ == '__main__':
    s = "abcdefgabcdefg"
    result = reverseShuffleMerge(s)
    assert result == "agfedcb"