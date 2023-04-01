# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:34:48 2023

@author: david
"""
import numpy as np
lista = np.random.randint(100, size = (10))

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result = np.append(result, left[i])
            i += 1
        else:
            result = np.append(result, right[j])
            j += 1
    result = np.concatenate((result, left[i:], right[j:]))
    return result

lo = mergesort(np.copy(lista))

print("ordenamiento con el metodo merge sort sort\n\n")
print("lista sin ordenar =\t", lista, "\nlista ordenada =\t", lo)