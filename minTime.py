#!/bin/python3

import math
import os
import random
import re
import sys
import math 


# Complete the minTime function below.
def minTime(machines, goal):
    minDay = math.ceil(goal / len(machines)) * min(machines)
    maxDay = math.ceil(goal / len(machines)) * max(machines)
    while minDay < maxDay:
        midDay = (maxDay + minDay) // 2
        if sum(midDay // m for m in machines) >= goal:
            maxDay = midDay
        else:
            minDay = midDay + 1
    return minDay


if __name__ == '__main__':
    machines = [4, 5, 6]
    goal = 12
    ans = minTime(machines, goal)
    print(ans, 20)