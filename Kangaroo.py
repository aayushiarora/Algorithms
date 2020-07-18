#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1 == x2 and v1 == v2):
        print("YES")
    elif (x1 == x2 and v1 > v2):
        print("NO")
    elif (x1 <= x2 and v1 <= v2):
        print("NO")
    elif((x2-x1)%(v1-v2) == 0):
        print("YES")
    else:
        print("NO")




if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

