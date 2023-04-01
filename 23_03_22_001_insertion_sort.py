# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:42:01 2023

@author: david
"""

"""
El algoritmo recibe un arreglo o lista de objetos comparables y retorna el mismo ordenado, 
para esto realiza un ciclo comenzando desde la segunda posición y terminando en N (última posición), 
entonces toma cada elemento del arreglo[i] y lo inserta en su lugar correspondiente de la secuencia
previamente ordenada arreglo[1...i-1]. Y de esta manera elemento a elemento vamos ordenando el arreglo

"""

import numpy as np
lista = np.random.randint(100, size = (10))

def insertion_sort(ordenar):
    
    for i in range(1, len(ordenar)):
        #se crea una variable temporal en la quye se almacernara el primer elementop a comparar
        value = ordenar[i] 
        j = i - 1
        # se compara si el valor de la derecha es menor al de la izquierda y de serlos invierte sus posiciones
        while(j >= 0 and value < ordenar[j]):
            ordenar[j+1], ordenar[j] = ordenar[j], value
            j -= 1
            
    return ordenar


lo = insertion_sort(np.copy(lista))
print("ordenamiento con el metodo insertion sort\n\n")
print("lista sin ordenar =\t", lista, "\nlista ordenada =\t", lo)