#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# example 07:05:45PM, output: 19:05:45

def timeConversion(s):
    # Write your code here
    print(f"Entered time to convert 24 hr format: {s}")
    time_str = s.split(":")
    time_hr = int(time_str[0])
    converted_time = 0
    if re.search("PM", s):
        print ("IN PM ")
        if time_str[0] != "12":
            print("In 12 houre check....")
            time_hr = time_hr + 12
            conv_hr = str(time_hr)
            print(f"conv_hr: {conv_hr}")
            print(f"time_str[0]: {time_str[0]}")
            converted_time = s.replace("PM", "")
            converted_time = converted_time.replace(time_str[0], conv_hr)
        else:
            converted_time = s.replace("PM", "")
    else:
        print ("IN AM ")
        converted_time = s.replace("AM", "")
        if time_str[0] == "12":
            converted_time = converted_time.replace("12", "00")
    
    print(f"Comverted time: {converted_time}")
    return converted_time

if __name__ == '__main__':

    print("Enter time to convert to 24 format: ")
    s = input()
    result = timeConversion(s)
