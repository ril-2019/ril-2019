#!/usr/bin/python
# -*- coding: utf-8 -*-

def fusion(arr):
    l = len(arr)
    if l <= 1:
        return arr
    
    m = l // 2
    g = fusion(arr[:m])
    d = fusion(arr[m:])

    return separation(g, d)


def separation(arr1, arr2):

    arr1_index, arr2_index = 0, 0
    res = []
    while arr1_index < len(arr1) and arr2_index < len(arr2):
        if arr1[arr1_index] < arr2[arr2_index]:
            res.append(arr1[arr1_index])
            arr1_index += 1
        else:
            res.append(arr2[arr2_index])
            arr2_index += 1

    res += arr1[arr1_index:]
    res += arr2[arr2_index:]
    return res

test = [ 6, 4, 5, 2, 2, 5, 2, 4 ]

print(fusion(test))