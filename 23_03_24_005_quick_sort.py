# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:24:44 2023

@author: david
"""
import numpy as np
lista = np.random.randint(100, size = (10))

"""
el arreglo a ordenar se divide en dos partes, una izquierda y otra derecha,
 en función de un elemento pivot que se selecciona al azar (en este caso, el primer elemento).
 Luego, se recorre el arreglo para comparar cada elemento con el pivot y agregarlo a la parte
 izquierda o derecha según corresponda.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        

        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)
"""
Después de eso, se aplican recursivamente los pasos anteriores a las partes izquierda y derecha, 
hasta que el tamaño de las partes a ordenar es de 1 o menos (lo que indica que ya están ordenadas)
"""    

lo = quicksort(np.copy(lista))
print("ordenamiento con el metodo insertion sort\n\n")
print("lista sin ordenar =\t", lista, "\nlista ordenada =\t", lo)