#!/usr/bin/env python3

import os
import random

this_file =  os.path.realpath(__file__)


print ("Well Come Mahesh Tandur")

# split string
text = "this is a python program"
print (text)
print (text.split(' '))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alphabet)
for count, item in enumerate(alpha_list):
	print(count, " ", item)
	
A = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
B = [6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14]
A = set(B)
print(A)

print(this_file)
f = open(this_file, "r")
print(type(f))
print(f.read())


mydict = {'first' : "First Item", 'second' : "Second Item"}
print(mydict.keys())
print(mydict.values())
print(mydict)


# Map function example:
def calculateSq(n):
    return n*n
numbers = (2, 3, 4, 5)
result = map( calculateSq, numbers)
print(result)


# Range example
for i in range(1,10):
      print (i)

# Print a file content in reverse.
for line in reversed(list(open(this_file))):
    print(line.rstrip())

# set to remove duplicat arguments
demo_list=[5,4,4,6,8,12,12,1,5]
unique_list=t = list(set(demo_list))
print(demo_list)
print(unique_list)


# Random example: read line dandomely
import random
def read_random(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(read_random (this_file))

# Prints string random froma list
List = ['He', 'Loves', 'To', 'Code', 'In', 'Python']
random.shuffle(List)
print(List)


# lambada example: lambda function in Python:
l = lambda x,y : x*y
print((5, 6))

