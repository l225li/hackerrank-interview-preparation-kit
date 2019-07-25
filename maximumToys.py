#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sorted(prices) # nlog(n) sorting
    count = 0
    for price in prices:
        if k > price:
            count += 1
            k -= price
        else:
            break
    return count




if __name__ == '__main__':
    k = 50
    prices = [1, 12, 5, 111, 200, 1000, 10]
    result = maximumToys(prices, k)
    print(result)
    assert result == 4
