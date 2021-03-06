#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equal function below.
def equal(arr):
    minNum = min(arr)
    minOp = float("inf")
    for i in range(minNum-4,minNum+1):
        op = 0
        for j in arr:
            diff = j - i
            op += diff//5 + diff%5//2 + diff%5%2
        if minOp > op:
            minOp = op
    return minOp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
