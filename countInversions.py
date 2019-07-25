#!/bin/python3

import math
import os
import random
import re
import sys


def merge(left, right):
    ll, lr = len(left), len(right)
    il, ir = 0, 0
    arr = []
    count = 0
    aa = arr.append
    while il < ll and ir < lr:
        if left[il] <= right[ir]:
            aa(left[il])
            il += 1
        else:
            aa(right[ir])
            ir += 1
            count += ll - il
    
    arr += left[il:]
    arr += right[ir:]
    return count, arr


# Complete the countInversions function below.
def merge_sort(arr):
    # base cases
    if len(arr) <= 1:
        return 0, arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    cnts_left, arr_left = merge_sort(left)
    cnts_right, arr_right = merge_sort(right)
    cnts_merge, arr_merge = merge(arr_left, arr_right)
    return cnts_merge + cnts_left + cnts_right, arr_merge

def countInversions(arr):
    return merge_sort(arr)[0]




if __name__ == '__main__':
    for arr in [[1, 1, 1, 2, 2], [2, 1, 3, 1, 2]]:
        result = countInversions(arr)
        print(result)


# def merge(a1, a2):
#     swaps, i, j, result, m, n = 0, 0, 0, [], len(a1), len(a2)
#     ra = result.append
#     while i < m and j < n:
#         if a1[i] <= a2[j]:
#             ra(a1[i])
#             i += 1
#         else:
#             ra(a2[j])
#             j += 1
#             swaps += m - i
#     result += a1[i:]
#     result += a2[j:]    
#     return swaps, result
    
# def msort(arr):
#     n = len(arr)
#     mid = n // 2
#     if n > 1:
#         left_swaps, left_result = msort(arr[:mid])
#         right_swaps, right_result = msort(arr[mid:])
#         m_swaps, result = merge(left_result, right_result)
#         return m_swaps + left_swaps + right_swaps, result
#     return 0, arr

# def countInversions(arr):
#     return msort(arr)[0]
