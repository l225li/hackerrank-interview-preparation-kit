#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import insort, bisect_left

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    def get_median(t_days):
        if d % 2 == 0:
            return (t_days[d//2] + t_days[d//2 - 1]) / 2
        else:
            return t_days[d//2]

    count = 0
    t_days = sorted(expenditure[:d])
    for i, current in enumerate(expenditure[d:]):
        median = get_median(t_days)
        if current >= 2 * median:
            count += 1
        del t_days[bisect_left(t_days, expenditure[i])]
        insort(t_days, current)

    return count


if __name__ == '__main__':

    for d, expenditure in [(5, [2, 3, 4, 2, 3, 6, 8, 4, 5]), (4, [1, 2, 3, 4, 4]), (4, [10, 20, 30, 40, 50])]:
        d = d
        expenditure = expenditure
        result = activityNotifications(expenditure, d)
        print(result)