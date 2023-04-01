# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:42:59 2023

@author: david
"""

"""
The selection sort algorithm maintains two sub-arrays by breaking the given array into sorted and unsorted parts.

In every iteration of the selection sort algorithm, the minimum element from the unsorted sub-array is picked and is moved to the sorted sub-array
"""

import numpy as np
lista = np.random.randint(100, size = (10))

def selection_sort(ordenar):
      
    # loop to Traverse through all the elements in the given array
    for i in range(len(ordenar)):
          
        # setting min_indx equal to the first unsorted element
        
        min_indx = i
        # Loop to iterate over un-sorted sub-array
        for j in range(i+1, len(ordenar)):
        
        #Finding the minimum element in the unsorted sub-array
            if ordenar[min_indx] > ordenar[j]:
                min_indx = j
                  
        # swapping the minimum element with the element at min_index to place it at its correct position    
        ordenar[i], ordenar[min_indx] = ordenar[min_indx], ordenar[i]
      
    
    
    return ordenar


print("\n\nordenamiento con el metodo selection sort\n\n")
lo = selection_sort(np.copy(lista))
print("lista sin ordenar =\t", lista, "\nlista ordenada =\t", lo)