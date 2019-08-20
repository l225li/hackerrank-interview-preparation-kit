#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    num_pairs = 0
    sorted_ar = sorted(ar)
    print(sorted_ar)
    prev = sorted_ar[0]
    count_color = 1
    for color in sorted_ar[1:]:
        if color==prev:
            count_color+=1
        else:
            num_pairs += count_color//2
            count_color=1
        prev = color
    
    num_pairs += count_color//2
    return num_pairs
            
if __name__ == '__main__':
    ar = [10, 30, 10, 30, 20, 15, 15, 18, 18, 18, 19]
    n = len(ar)
    num_pairs = sockMerchant(n, ar)
    print(num_pairs)