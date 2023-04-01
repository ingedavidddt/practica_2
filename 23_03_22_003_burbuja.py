# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:16:14 2023

@author: david
"""
import numpy as np
lista = np.random.randint(100, size = (10))


"""
El ordenamiento de burbuja es un algoritmo que te permite ordenar valores de un arreglo. 
Funciona revisando cada elemento con su adyacente. Si ambos elementos no están ordenados, 
se procede a intercambiarlos, si por el contrario los elementos ya estaban ordenados se dejan 
tal como estaban. Este proceso sigue para cada elemento del arreglo hasta que quede completamente ordenado.
"""

def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):
        #al terminar cada ciclo principal este disminuye ya que el ultimo valor ya ha sido ordenado
        for j in range(n-1-i): 
#se compara si el valor de la izquierda es menor que el de la derecha y de serlo lso intercabia
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

    return arreglo



print("\n\nordenamiento con el metodo de intercambio (burbuja)\n\n")
lo = ord_burbuja(np.copy(lista))
print("lista sin ordenar =\t", lista, "\nlista ordenada =\t", lo)