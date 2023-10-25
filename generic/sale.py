#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    games_purchased = 0
    current_price = p
    while s >= current_price:
        games_purchased += 1
        s -= current_price
        current_price = max(current_price - d, m)

    return games_purchased

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    p = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    s = int(first_multiple_input[3])
    answer = howManyGames(p, d, m, s)

