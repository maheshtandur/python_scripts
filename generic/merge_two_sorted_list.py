#!/bin/python3

# Merging two sorted list
# example: arr1 = [1 3 6]
#          arr2 = [2 5 4]
# Out put: [1 2 3 4 5 6]

def mergelist(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    print (f"Sorted list 1: {arr1}")
    print (f"Sorted list 2: {arr2}")

    mergelist = arr1
    mergelist.extend(arr2)
    print (f"Merged list: {mergelist}")
    print (f"Merged Sorted list: {sorted(mergelist)}")

if __name__ == '__main__':
    arr1 = [8, 4, 19, 15]

    arr2 = [16, 10, 9, 7]
    mergelist(arr1, arr2)
