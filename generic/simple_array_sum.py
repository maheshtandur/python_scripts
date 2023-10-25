#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    total = 0
    for num in ar:
        print(num)
        total = total + num
    return total

if __name__ == '__main__':

    print ("Eneter array limit: ")
    ar_count = int(input().strip())
    print ("Enter list elements: ")
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print (f"List Sum: {ar} = {result}")

  
