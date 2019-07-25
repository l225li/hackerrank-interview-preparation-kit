#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    for i, p in enumerate(q):
        if p - i > 3:
            print("Too chaotic")
            return
        for j in range(max(0, p-2), i):
            if q[j] > p:
                moves += 1
    print(moves)

if __name__ == '__main__':
    q = [2, 1, 5, 3, 4]
    minimumBribes(q)
    q = [2, 5, 1, 3, 4]
    minimumBribes(q)
    q = [1,2,5,3,7,8,6,4]
    minimumBribes(q)

