#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    total = 0
    for num in ar:
        total = total + num
    return total


if __name__ == '__main__':

    print("Enter list limit: ")
    ar_count = int(input().strip())
    print("Enter very Big numbers: ex: 1000000001")
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print (f"sum of num: {ar} = {result}")
