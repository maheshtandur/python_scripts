#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
# example run: arr = [4 4 1 3], Output: 2

def birthdayCakeCandles(candles):
    # Write your code here
    print(f"Entered list: {candles}")
    max_num = candles[0]
    count = 0
    for num in candles:
        if num >= max_num:
            max_num = num
    
    for num in candles:
        if max_num == num:
            count = count + 1
    print (f"Maximun Height: {max_num} and there are {count} of them")
    return count



if __name__ == '__main__':

    print ("Enter max list: ")
    candles_count = int(input().strip())
    print ("Enter list elements: ")
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print (f"There are {result} of them")
