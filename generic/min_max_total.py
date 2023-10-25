#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# Example: arr = [1 3 5 7 9], output: 16 and 24

def miniMaxSum(arr):
    # Write your code here
    print (f"Enterd list value: {arr}")
    min = arr[0]
    max = arr[0]
    total = 0
    for num in arr:
        print(num)
        if min < num:
            min = num
        elif max > num:
            max = num
        total = total + num
    print(f"Max: {max} and MIN: {min}")

    print(f"The minimum sum is: {total - min}")
    print(f"The maximum sum is: {total - max}")

if __name__ == '__main__':

    print ("Enter list value to calculate MIN and MAX total: ")
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
