#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# run as example: arr = [1,1,0,-1,-1]
#

def plusMinus(arr):
    # Write your code here
    print (f"Entered list: {arr}")
    count_positive = 0
    count_negative = 0
    count_zero = 0
    total_num = len(arr)
    decimal_places = 6
    for num in arr:
        if num > 0:
            count_positive = count_positive +1
        elif num < 0:
            count_negative = count_negative +1
        elif num == 0:
            count_zero = count_zero +1

    ratio = count_positive/total_num
    formatted_value = "{:.{}f}".format(ratio, decimal_places)
    print(f"Positive Count: {count_positive} and Ratio: {formatted_value}")
    
    ratio = count_negative/total_num
    formatted_value = "{:.{}f}".format(ratio, decimal_places)
    print(f"Negative Count: {count_negative} and Ratio: {formatted_value}")

    ratio = count_zero/total_num
    formatted_value = "{:.{}f}".format(ratio, decimal_places)   
    print(f"Zero Count:     {count_zero} and Ratio: {formatted_value}")


if __name__ == '__main__':
    print("Enter list length: ")
    n = int(input().strip())
    print("Enter list elements: ")
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
