#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    current = s[0]
    result = [current]
    for i in range(len(s)):
        if s[i] != current:
            current = s[i]
            result.append(current)
    
    return len(s) - len(result)




if __name__ == '__main__':
    for s in ["AAAA", "BBBBB", "ABABABAB", "BABABA", "AAABBB"]:
        result = alternatingCharacters(s)
        print(result)


