#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(b):
    maxi, max1 = 0, 0
    for i in range(1,len(b)):
        curr, prev = b[i], b[i-1]
        newmaxi = max(maxi + abs(curr - prev), max1 + (curr - 1))
        newmax1 = max(maxi + abs(1 - prev), max1)
        maxi, max1 = newmaxi, newmax1    
    u=max(maxi, max1)
    return u

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
