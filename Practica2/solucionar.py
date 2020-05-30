import numpy as np
import math
from escenario import Escenario
from copy import deepcopy
from arbol import Nodo


def distancia(pos0, posf):
    # distancia L1
    return abs(posf[0]-pos0[0] + posf[1] - pos0[1])


def crearMatriz(e: Escenario):
    n = e.getNumMinas()

    listaMinas = e.getMinas()

    m = np.zeros((n+1, n+1), dtype=float)

    for i in range(n+1):
        # iterar solo en la mitad superior (es una matriz simetrica por las propiedades del problema)
        for j in range(i, n + 1):

            if i == j:
                m[i, j] = math.inf
            else:
                if i == 0:
                    d = distancia(e.getPosIni(), listaMinas[j-1])
                else:
                    d = distancia(listaMinas[i-1], listaMinas[j-1])
                m[i, j] = d
                m[j, i] = d

    return m


def reducirMatrizFilas(orig):
    m = orig
    restado = 0

    for i, fila in enumerate(m):
        min = math.inf
        for elemento in fila:
            if elemento < min:
                min = elemento
                if elemento == 0:
                    break
        if min != math.inf:
            restado += min
            for j, elemento in enumerate(fila):
                m[i, j] -= min

    return restado


def reducirMatrizColumnas(orig):
    m = np.transpose(orig)
    restado = 0

    for j, columna in enumerate(m):
        min = math.inf
        for elemento in columna:
            if elemento < min:
                min = elemento
                if elemento == 0:
                    break

        if min != math.inf:
            restado += min
            for i, elemento in enumerate(columna):
                m[j, i] -= min

    return restado


def reducir(m):
    aux = reducirMatrizFilas(m)
    aux += reducirMatrizColumnas(m)
    return aux


def elegirReducir(n: Nodo, je):
    m = deepcopy(n.matriz)

    ie = n.i

    for i in range(len(m)):
        m[ie, i] = math.inf
        m[i, je] = math.inf

    # marcar la celda en sentido opuesto como infinito
    m[je, ie] = math.inf

    # marcar como infinito todos los que se dirigen a nodos ya visitados
    padre = n.n_padre
    while padre != None:
        i_padre = padre.i
        m[je, i_padre] = math.inf
        padre = padre.n_padre

    return (m, reducir(m))


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


def addOrdenado(lista, nuevo):
    if len(lista) == 0:
        lista.append(nuevo)
    else:
        notFound = True
        i = 0
        while i < len(lista) and notFound:
            if lista[i].coste < nuevo.coste:
                i += 1
            else:
                notFound = False
        lista.insert(i, nuevo)

    # for elemento in lista:
    #    print(str(elemento.i) + "   " + str(elemento.coste))


def expandirNodo(n: Nodo, e: Escenario, colaActivos, upperBound):
    #print("Expandiendo nodo " + str(n.i_nodo) + "\n")
    resultado = -1
    m0 = n.matriz
    c0 = n.coste
    i = n.i
    colaActivos.pop(0)  # eliminamos n puesto que ya se ha expandido
    # para todas las minas
    for j in range(0, e.getNumMinas()+1):
        # no volver a minas ya visitadas (coste infinito)
        if n.matriz[n.i, j] != math.inf:
            # calculamos coste
            m, r = elegirReducir(n, j)
            c = funcionCoste(m0, i, j, c0, r)

            # creamos el hijo
            hijo = Nodo(c, j, n)

            # añadimos el nuevo hijo que aún no se ha expandido
            if c <= upperBound:
                hijo.addMatriz(m)
                addOrdenado(colaActivos, hijo)
            n.addHijo(hijo)

    # si al acabar el bucle n solo tiene un hijo, quiere decir que dicho hijo es un nodo hoja
    if n.n_hijos < 2:
        # no es necesario expandir el hijo, pues ya es un nodo hoja
        if c <= upperBound:
            hoja = colaActivos.pop(0)
        resultado = hoja.coste

    return resultado


def solucionar(e: Escenario):

    colaActivos = []
    soluciones = []

    # calcular raiz
    m0 = crearMatriz(e)
    c0 = reducir(m0)

    arbol = Nodo(c0, 0, None)
    arbol.addMatriz(m0)

    upperBound = math.inf
    addOrdenado(colaActivos, arbol)

    # calcular hijos
    while (len(colaActivos) > 0):
        nodo = colaActivos[0]
        bound = expandirNodo(nodo, e, colaActivos, upperBound)
        if bound != -1 and bound < upperBound:
            upperBound = bound
            soluciones.append(nodo)
            #print("Nodo hoja encontrado. UpperBound = " + str(upperBound) + "\n")
            i = len(colaActivos) - 1
            n = colaActivos[i]
            while i > 0 and n.coste >= upperBound:
                # n.desactivar
                colaActivos.pop(i)
                i -= 1
                n = colaActivos[i]

            for j, s in enumerate(soluciones):
                if s.coste > upperBound:
                    soluciones.pop(j)

    return (int(upperBound), soluciones, arbol)
