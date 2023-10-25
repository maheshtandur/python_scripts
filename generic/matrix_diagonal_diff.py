#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    # Write your code here
    print (arr)
    list_len = len(arr)
    print (f"List length: {list_len}")
    sum1 = 0
    sum2 = 0
    j = -1
    for i in range(0, list_len):
        print (f"--> {arr[i][i]}")
        sum1 = sum1 + arr[i][i]
        print (f"==> {arr[i][j]}")
        sum2 = sum2 + arr[i][j]
        j = j - 1
    diff = sum1 - sum2
    abs_num = abs(diff)
    print (f"Diagnol difference: {sum1} - {sum2} = {abs_num}")

    return abs_num

if __name__ == '__main__':

    print ("Enter matix size: ")
    n = int(input().strip())
    arr = []
    print ("Enter matrix elements: ")
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr, n)
    print (f"Diagnol difference: {result}")
