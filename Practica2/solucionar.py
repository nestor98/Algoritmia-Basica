# Autores: Monzón González, Néstor
#          Otero García, Andrés

import numpy as np
import heapq
import math
from escenario import Escenario
from copy import deepcopy
from arbol import Nodo
from timeit import default_timer as timer


def distancia(pos0, posf):
    # distancia L1
    return abs(posf[0] - pos0[0]) + abs(posf[1] - pos0[1])


def crearMatriz(e: Escenario):
    n = e.n_minas

    listaMinas = e.lista_minas

    m = np.zeros((n + 1, n + 1), dtype=float)

    for i in range(n + 1):
        # iterar solo en la mitad superior (es una matriz simetrica por las propiedades del problema)
        for j in range(i, n + 1):

            if i == j:  # Diagonal a infinito
                m[i, j] = math.inf
            else:
                if i == 0:  # distancia al punto inicial
                    d = distancia(e.pos_ini, listaMinas[j - 1])
                else:  # distancia entre minas
                    d = distancia(listaMinas[i - 1], listaMinas[j - 1])
                m[i, j] = d
                m[j, i] = d
    return m


def reducirMatrizFilas(orig):
    """
    Input: matriz original de costes
    Output: Primero: matriz en la que a cada elto se le ha restado el minimo de su fila
            Segundo: coste de la reduccion (suma de los minimos)
    """
    m = orig
    min = m.min(axis=1)  # minimo en cada fila
    min[min == math.inf] = 0  # si eran todo infinitos, 0

    restado = np.sum(min)  # suma de los minimos
    m = m - min[:, None]  # se reduce cada fila restandole a cada elto el min

    return (m, restado)


def reducirMatrizColumnas(orig):
    """
    Input: matriz original de costes
    Output: Primero: matriz en la que a cada elto se le ha restado el minimo de su columna
            Segundo: coste de la reduccion (suma de los minimos)
    """
    m = orig
    min = m.min(axis=0)
    min[min == math.inf] = 0

    restado = np.sum(min)
    m = m - min

    return (m, restado)


def reducir(m):
    """
    Input: matriz m donde cada celda (i, j) es el coste para ir desde la mina i a la j
    Output: Primer argumento: nueva matriz de costes (tras reducirla)
            Segundo: coste de reducción
    """
    m, aux = reducirMatrizFilas(m)  # reducir filas
    m, aux2 = reducirMatrizColumnas(m)  # y columnas
    aux += aux2  # coste de reduccion total

    return (m, aux)


def elegirReducir(n: Nodo, je):
    m = deepcopy(n.matriz)

    ie = n.i

    m[ie, :] = math.inf
    m[:, je] = math.inf

    # marcar la celda en sentido opuesto como infinito
    m[je, ie] = math.inf

    # marcar como infinito todos los que se dirigen a nodos ya visitados
    padre = n.n_padre
    while padre != None:
        i_padre = padre.i
        m[je, i_padre] = math.inf
        padre = padre.n_padre

    return reducir(m)


def funcionCoste(m0, i, j, c0, r):
    """
    Calcula el coste de ir de un nodo x a un nodo y
    c(y) = c(x) + c(i->j) + r

    r -> mínimo coste que tendrá producir un circuito hamiltoniano con los nodos restantes
    (valor "restado" al reducir la matriz)\n
    c(x) -> coste acumulado hasta x\n
    c(i->j) -> coste de ir de la mina i a la mina j

    Parametros
    ----------
    m0: matriz inicial\n
    i: indice de la mina del nodo x\n
    j: indice de la mina del nodo y\n
    c0: coste desde el origen hasta x\n
    r: coste de reducción de la matriz

    Devuelve
    -------
    c: coste del nodo y
    """
    return c0 + m0[i, j] + r


def expandirNodo(n: Nodo, e: Escenario, colaActivos, upperBound, n_activos):

    resultado = -1
    m0 = n.matriz
    c0 = n.coste
    n_pos = e.n_minas + 1
    i = n.i
    c = math.inf
    # no iterar si se ha superado ya el upperBound en el nodo a expandir (safe-check)
    if c0 < upperBound:
        # para todas las minas
        for j in range(n_pos):
            # no volver a minas ya visitadas (coste infinito)
            if m0[i, j] != math.inf:
                # calculamos coste
                m, r = elegirReducir(n, j)
                c = funcionCoste(m0, i, j, c0, r)

                # creamos el hijo
                hijo = Nodo(c, j, n)

                # añadimos el nuevo hijo que aún no se ha expandido
                if c <= upperBound:
                    hijo.addMatriz(m)
                    heapq.heappush(colaActivos, hijo)
                    n_activos += 1
                n.addHijo(hijo)

        # si al acabar el bucle n solo tiene un hijo, quiere decir que dicho hijo es un nodo hoja

        if n.n_hijos < 2 and c <= upperBound:
            # no es necesario expandir el hijo, pues ya es un nodo hoja
            hoja = heapq.heappop(colaActivos)
            n_activos -= 1
            resultado = hoja.coste

    return (resultado, n_activos)


def solucionar(e: Escenario):

    n_activos = 1

    # calcular raiz
    m0 = crearMatriz(e)  # matriz de costes a partir del escenario
    m0, c0 = reducir(m0)  # reduccion de filas y columnas (c0 el coste)

    arbol = Nodo(c0, 0, None)  # inicializamos el nodo

    if (
        e.n_minas == 0
    ):  # comprobar que el numero de minas es mayor que 0, sino, devolver coste 0 y solo el nodo raiz
        return (0, arbol)

    arbol.addMatriz(m0)  # y le añadimos la matriz

    upperBound = math.inf  # al principio el limite es infinito

    colaActivos = [arbol]
    heapq.heapify(
        colaActivos
    )  # pasamos la lista a monticulo para mejorar la eficiencia

    # calcular hijos
    while n_activos > 0:
        nodo = heapq.heappop(colaActivos)
        n_activos -= 1
        # puesto que solo deseamos conocer el mínimo de pasos, pero no las soluciones, no es necesario expandir nodos no-hoja con coste = upperBound

        if nodo.coste < upperBound:
            bound, n_activos = expandirNodo(nodo, e, colaActivos, upperBound, n_activos)
        else:
            nodo.desactivar
        if bound != -1 and bound < upperBound:
            upperBound = bound

    return (int(upperBound), arbol)
