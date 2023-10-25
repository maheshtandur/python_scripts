#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    score1 = 0
    score2 = 0

    for num1, num2 in zip (a, b):
        print (f"num1: {num1} and num2: {num2}")
        if num1 > num2:
            score1 = score1 + 1
        elif num1 < num2:
            score2 = score2 + 1

    print (f"score1: {score1} and score2: {score2}")
    return ([score1, score2])

if __name__ == '__main__':

    print ("Enter element of List 1: ")
    a = list(map(int, input().rstrip().split()))
    print ("Enter element of List 2: ")
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

