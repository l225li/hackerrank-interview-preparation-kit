#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    l = []
    cur = None
    count = 0

    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))            
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0

    for _, r in l:
        ans += r * (r+1) // 2
    
    for i in range(1, len(l)-1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])
    
    return ans


if __name__ == '__main__':
    for n, s in [(7, "abcbaba")]:
        result = substrCount(n, s)
        print(result)
