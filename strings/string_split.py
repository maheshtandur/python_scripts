# This program defines a function print_substrings that takes a string s as input and prints all possible substrings. 
# It iterates over each character in the string and prints all substrings starting from that character to the end of the string.

# You can achieve this by iterating over the string and printing all possible substrings starting from each character. 

# Here's a Python program to accomplish this:

def print_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            print(s[i:j+1], end=", \n")
    print()  # to move to the next line after printing all substrings

# Test the function
str = "abcdefghijklmnopqrstuvwxyz"
print_substrings(str)
