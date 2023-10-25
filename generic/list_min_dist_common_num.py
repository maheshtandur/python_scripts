#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    print (f"Enter List numbers: {a}")
    list_len = len(a)
    dist = []
    for i in range(0, list_len):
        for j in range (i+1, list_len):
            if a[i] == a[j]:
                print(f"The value of: {a[i]} in at positio: {i} and {j}")
                dist.append(j - i)

    min_dist = -1
    if len(dist) >= 2:
        print(f"Minmum list: {dist}")
        min_dist = dist[0]
        for num in dist:
            if num < min_dist:
                min_dist = num
    elif len(dist) == 1:
        min_dist = dist[0]

    if min_dist == -1:
        print (f"Common value dosent exist...")
        return (-1)
    else:
        print(f"Minum Distance: {min_dist}")
        return (min_dist)

if __name__ == '__main__':

    print("Enter list limit: ")
    n = int(input().strip())
    print ("Enter list elemens: ")
    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)
