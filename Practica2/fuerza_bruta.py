import sys
import math
from escenario import Escenario
from escenario import leer_escenario
from timeit import default_timer as timer
from copy import deepcopy


def distancia(pos0, posf):
    # distancia L1
    return abs(posf[0] - pos0[0]) + abs(posf[1] - pos0[1])


def expandir(nivel, pos0, posPadre, lista, n_minas, resultado):
    """
    Para un escenario con n_minas y cuya posición inicial de Nikita sea pos0:
    calcula el coste de todos los hijos de un nodo con posición "posPadre" en el plano del escenario,
    (los cuales forman parte del nivel "nivel" de un árbol completo, cuya raíz posee
    "pos0" como posición) y para el cual "lista" es la lista de minas sin visitar en el
    recorrido desde el nodo raíz hasta el nodo actual de dicho árbol.
    "resultado" es el coste de recorrido mínimo encontrado desde que se comenzó a expandir el primer nodo
    """
    if nivel == n_minas:
        # no expandir más, pues ya se han recorrido todas las minas y devolver la distancia de vuelta
        return distancia(posPadre, pos0)
    else:
        # para cada mina restante
        for j, _ in enumerate(lista):
            # creamos una lista sin la mina que vamos a visitar para pasárselo a la siguiente iteración recursiva
            lista_restantes = deepcopy(lista)
            lista_restantes.pop(j)
            # expandir hijos del nodo generado (en el siguiente nivel, con la lista de minas restantes)
            # y sumar la distancia del nodo generado
            coste = expandir(
                nivel + 1, pos0, lista[j], lista_restantes, n_minas, resultado
            ) + distancia(posPadre, lista[j])
            # devolver solo el coste del recorrido menor que se haya encontrado
            if coste < resultado:
                resultado = coste
        return resultado


if __name__ == "__main__":

    f = open(sys.argv[1], "r")  # leer archivo
    f_out = open(sys.argv[2], "w")  # archivo de salida

    n = int(f.readline().replace("\n", ""))  # leer el numero de escenarios
    escenarios = []

    # lee todos los escenarios
    for i in range(n):
        # print(i)
        escenarios.append(leer_escenario(f))

    for e in escenarios:
        # expandir el árbol desde el nivel 0, con la posición inicial, con toda la lista de minas y con coste inicial infinito
        start = timer()
        upperBound = expandir(
            0, e.pos_ini, e.pos_ini, e.lista_minas, e.n_minas, math.inf
        )
        end = timer()
        # mostrar resultado
        f_out.write(str(upperBound) + " " + str(end - start) + "\n")
        f_out.flush()

    f.close()
    f_out.close()
