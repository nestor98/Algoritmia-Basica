# Autores: Monzón González, Néstor
#          Otero García, Andrés

from copy import deepcopy
import math


class Nodo:
    i = 0  # variable estatica, numero de nodos total

    def __init__(self, coste, i_mina, n_padre):
        self.i = i_mina  # identificador de la mina
        if i_mina == 0:
            Nodo.i = 0
        else:
            Nodo.i += 1
        self.i_nodo = Nodo.i  # identificador del nodo

        self.coste = coste
        self.listaHijos = []  # lista ordenada de hijos por coste
        self.n_hijos = 0  # numero de hijos
        self.n_padre = n_padre  # nodo padre
        self.activo = True  # activo (si no, no se seguirá expandiendo)

    def addMatriz(self, matriz):
        if self.activo:
            self.matriz = matriz

    def addHijo(self, n):
        self.listaHijos.append(n)
        self.n_hijos += 1

    def desactivar(self):
        if self.activo:
            self.activo = False

    def __gt__(self, nodo2):
        return self.coste > nodo2.coste

    def __lt__(self, nodo2):
        return self.coste < nodo2.coste

    def __ge__(self, nodo2):
        return self.coste >= nodo2.coste

    def __le__(self, nodo2):
        return self.coste <= nodo2.coste
