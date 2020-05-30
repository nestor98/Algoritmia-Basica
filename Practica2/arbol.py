from copy import deepcopy
import math


class Nodo:
    i = 0

    def __init__(self, coste, i_mina, n_padre):
        self.i_nodo = Nodo.i
        Nodo.i += 1
        self.coste = coste
        self.i = i_mina
        self.listaHijos = []  # lista ordenada de hijos por coste
        self.n_hijos = 0
        self.n_padre = n_padre
        # if self.n_padre == None:
        #    padre_string = None
        #    print("Creado nodo" + str(self.i_nodo) + ", con mina " +
        #          str(self.i) + ", coste " + str(self.coste) + " y sin padre\n")
        # else:
        #    padre_string = str(self.n_padre.i_nodo)
        #    print("Creado nodo" + str(self.i_nodo) + ", con mina " +
        #          str(self.i) + ", coste " + str(self.coste) + " y padre " + padre_string + "\n")

    def addMatriz(self, matriz):
        # if self.activo:
        self.matriz = deepcopy(matriz)
        #print("Matriz en nodo " + str(self.i_nodo) + "\n")
        # print(matriz)

    def addHijo(self, n):
        self.listaHijos.append(n)
        self.n_hijos += 1

    # def desactivar(self):
        # if self.activo:
        #self.activo = False
        #del self.matriz
        #del self.listaHijos
        #print("Nodo " + str(self.i_nodo) + " desactivado\n")
