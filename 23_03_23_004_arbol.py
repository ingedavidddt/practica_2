# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:50:59 2023

@author: david
https://parzibyte.me/blog/2021/01/14/arbol-binario-python/
"""

import numpy as np
lista = np.random.randint(100, size = (10))

class Nodo:
    def __init__(self, dato):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)
            return(nodo.dato)
        
    def __almacenar_en_array(self, nodo, array):
        if nodo is not None:
            self.__almacenar_en_array(nodo.izquierda, array)
            array.append(nodo.dato)
           
            self.__almacenar_en_array(nodo.derecha, array)
        
  
        
    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
        
    

    # Funciones públicas

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        orden = self.__inorden_recursivo(self.raiz)
        print("")
        return(orden)
    
    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    
    def array(self, array):
        return self.__almacenar_en_array(self.raiz, array)


orArbol = Arbol(lista[0])
ordenado = []

for i in range(1, len(lista)):
    orArbol.agregar(lista[i])
   
orArbol.array(ordenado)

ordenado = np.asarray(ordenado)
print("\n\nordenamiento con el metodo de arboles binarios inorder\n\n")

print("lista sin ordenar =\t", lista, "\nlista ordenada =\t", ordenado)