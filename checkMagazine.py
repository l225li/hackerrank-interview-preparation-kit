#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dict_magazine = Counter(magazine.split())
    print(dict_magazine)
    for word in note.split():
        if not dict_magazine[word]:
            print("NO")
            return
        else:
            dict_magazine[word] -= 1
    print("YES")


if __name__ == '__main__':
    magazine = "give me one grand today night"
    note = "give one grand today today"
    m = len(magazine.split())
    n = len(note.split())
    checkMagazine(magazine, note)
