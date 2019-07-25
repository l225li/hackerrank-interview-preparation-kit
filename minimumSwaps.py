#!/bin/python3

import math
import os
import random
import re
import sys

# def minimumSwaps(arr):
#     ref_arr = sorted(arr)
#     index_dict = {v: i for i,v in enumerate(arr)}
#     swaps = 0
    
#     for i,v in enumerate(arr):
#         correct_value = ref_arr[i]
#         if v != correct_value:
#             to_swap_ix = index_dict[correct_value]
#             arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
#             index_dict[v] = to_swap_ix
#             index_dict[correct_value] = i
#             swaps += 1
            
#     return swaps


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = {v: i for i, v in enumerate(arr)}
    swaps = 0

    for i, v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix]
            index_dict[correct_value] = i
            index_dict[v] = to_swap_ix
            swaps += 1
    return swaps

if __name__ == '__main__':
    arr = [1, 3, 5, 2, 4, 6, 8]

    res = minimumSwaps(arr)
    print(res)