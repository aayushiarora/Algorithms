#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = [0] * (n + 1)
    for q in queries:
        a[q[0] - 1] += q[2]
        a[q[1]] -= q[2]
    
    return max(accumulate(a))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()