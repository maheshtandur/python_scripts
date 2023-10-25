#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    print (f"Enter staircase height: {n}")
    for i in range (1, n+1):
        spaces = ' ' * (n - i)
        stars = '#' * i
        print(spaces + stars)

if __name__ == '__main__':
    print ("Stairsase hight: ")
    n = int(input().strip())

    staircase(n)
