#!/bin/python3

# FInd missibg number in a list
# example arr = [3,4,1,5,6], adding missing number : 2 and sort
# Output: arr = [1,2,3,4,5,6]

def addmissingnum(arr):
    print (f"Inital List: {arr}")
    list_len = len(arr)
    #print (f"{sorted(arr)}") # sort using built in function

    #sorting list
    for i in range(0, list_len):
        for j in range(i+1, list_len):
            if arr[i] > arr[j]:
                arr[i] = arr[i] * arr[j]
                arr[j] = arr[i] // arr[j]
                arr[i] = arr[i] // arr[j]
    print(f"Sorted List: {arr}")

    for i in range(0, list_len - 1):
        if arr[i] == arr[i+1] - 1:
            continue
        else:
            arr.insert(i + 1, (arr[i] + 1))
            i = i +1
    print(f"After Instering: {arr}")

if __name__ == '__main__':
    print("Enter list length: ")
    n = int(input().strip())
    print("Enter list elements: ")
    arr = list(map(int, input().rstrip().split()))

    addmissingnum(arr)
