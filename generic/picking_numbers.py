#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# Example: a = [1,1,2,2,4,4,5,5,5] 
#          a = [4 6 5 3 3 1], output: 3
#          a = [1 2 2 3 1 2], Output: 5


def pickingNumbers(a):
    # Write your code here
    print (f"Input Array: {a}")

    maxlen = 1
    for i in range (0, len(a)):
        maxofSub = a[i]
        for j in range (i+1, len(a)):
            if (a[j] < maxofSub):
                maxofSub = a[j]
            if (maxofSub <= 1):
                currlen = i - j
                if (maxlen > currlen):
                    maxlen = currlen

    print (f"Max length of sub array: {maxlen}")
    return maxlen

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
