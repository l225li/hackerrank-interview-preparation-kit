#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    for length in range(1, len(s)):
        # range(len(s) - length + 1) because range is end exclusive, it stops at (len(s) - length) which is desired
        patterns = ["".join(sorted(s[start: start+length])) for start in range(len(s)-length + 1)]
        dict_patterns = Counter(patterns)
        for pattern in dict_patterns:
            count += (dict_patterns[pattern] - 1) * (dict_patterns[pattern]) / 2
    return int(count)



if __name__ == '__main__':
    for s in ["kkkk", "cdcd"]:
        s = s
        result = sherlockAndAnagrams(s)
        print(result)