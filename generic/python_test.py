#!/usr/bin/env python3

import os

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









