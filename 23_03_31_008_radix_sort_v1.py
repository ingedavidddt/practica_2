# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:08:52 2023

@author: david
"""
import numpy as np
lista = np.random.randint(100, size = (10))

def radixSort(nums):
    # determinar el número máximo de dígitos
    max_num = max(nums)
    num_digits = len(str(max_num))

    # clasificar los valores en función de cada dígito
    for digit in range(num_digits):
        # crear un arreglo para cada posible valor de dígito
        buckets = [[] for _ in range(10)]

        # colocar cada valor en el cubo correspondiente
        for num in nums:
            bucket_index = (num // 10**digit) % 10
            buckets[bucket_index].append(num)

        # unir los cubos en un solo arreglo
        nums = [num for bucket in buckets for num in bucket]

    return nums

lo = radixSort(np.copy(lista))

print("ordenamiento con el metodo radix sort sort\n\n")
print("lista sin ordenar =\t", lista, "\nlista ordenada =\t", lo)