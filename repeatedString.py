#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the repeatedString function below.
def repeatedString(s, n):
    length_s = len(s)
    count_a = 0
    remainder = n % length_s
    quotient = n // length_s
    if remainder:
        count_a += Counter(s[:remainder])['a']
    if quotient:
        count_a += Counter(s)['a'] * quotient
    return count_a


if __name__ == '__main__':
    s = "a"
    n = 1000000000000000
    result = repeatedString(s, n)
    print(result)
