# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:29:34 2023

@author: david
"""
import numpy as np
lista = np.random.randint(100, size = (10))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = np.array([])

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result = np.append(result, left[0])
                left = left[1:]
            else:
                result = np.append(result, right[0])
                right = right[1:]
        elif len(left) > 0:
            result = np.append(result, left[0])
            left = left[1:]
        elif len(right) > 0:
            result = np.append(result, right[0])
            right = right[1:]

    return result

lo = merge_sort(np.copy(lista))

print("ordenamiento con el metodo merge sort sort\n\n")
print("lista sin ordenar =\t", lista, "\nlista ordenada =\t", lo)
