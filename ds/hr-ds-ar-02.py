#!/bin/python3

import sys

def splitArr(arr, a):
    end = len(arr[0])
    print("array length: " + str(len(arr[0])))
    if len(arr) == 2:
        return 0
    else:
        temp = []
        print("End: " + str(end))
        print(len(arr))
        for i in range(0, len(arr) - 2):
            temp.extend(arr[i][0+i:3+i])
            temp.append(arr[i+1][1+i])
            temp.extend(arr[i+2][0+i:3+i])
            a.append(temp)
            temp = []
        print(len(a))
        return a.append(splitArr(arr[1:],a))

def splitArr1(arr):
    a = []
    for i in range(0, len(arr) - 2):
        temp = []
        for j in range(0, len(arr[0]) - 2):
            temp.extend(arr[i][0+j:3+j])
            temp.append(arr[i+1][1+j])
            temp.extend(arr[i+2][0+j:3+j])
            a.append(sum(temp))
            temp = []
    return a

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

print(arr[1:])
new_arr = []
ar = splitArr1(arr)

print(max(ar))
