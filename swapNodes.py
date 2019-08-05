#!/bin/python3

import os
import sys


def inOrder(indexes):
    stack = [1]
    result = []
    while stack:
        i = stack.pop()
        if i > 0:
            if indexes[i][1] > 0:
                stack.append(indexes[i][1])
            stack.append(-i)
            if indexes[i][0] > 0:
                stack.append(indexes[i][0])
        else:
            result.append(-i)
    return result

def swapNodes(indexes, queries):
    result = []
    indexes = [None] + indexes
    for k in queries:
        depth = 1
        toVisit = [1]
        while toVisit:
            if depth % k == 0:
                for i in toVisit:
                    indexes[i] = [indexes[i][1], indexes[i][0]]
            toVisit_ = []
            for i in toVisit:
                if indexes[i][0] > 0:
                    toVisit_.append(indexes[i][0])
                if indexes[i][1] > 0:
                    toVisit_.append(indexes[i][1])
            toVisit = toVisit_
            depth += 1
        result.append(inOrder(indexes))
    return result


if __name__ == '__main__':
    indexes = [[2, 3], [4, -1], [5, -1],
               [6, -1], [7, 8], [-1, 9],
               [-1, -1], [10, 11], [-1, -1],
               [-1, -1], [-1, -1]]
    queries = [2, 4]
    result = swapNodes(indexes, queries)
    print(result)
    # print(result)
    # for k in queries:
    #     swap(T, k)
    #     print(" ".join(str(_) for _ in inorder(T)))
