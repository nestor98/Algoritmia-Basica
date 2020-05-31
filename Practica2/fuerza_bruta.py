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
    # print("Expandiendo nodo " + str(nivel) + " " + str(lista) + " " + str(pos0) + "\n")
    if nivel == n_minas:
        # no expandir más
        return distancia(posPadre, pos0)
    else:
        for j, _ in enumerate(lista):
            lista_restantes = deepcopy(lista)
            lista_restantes.pop(j)
            coste = expandir(
                nivel + 1, pos0, lista[j], lista_restantes, n_minas, resultado
            ) + distancia(posPadre, lista[j])
            if coste < resultado:
                resultado = coste
        return resultado


if __name__ == "__main__":

    f = open(sys.argv[1], "r")  # leer archivo
    f_out = open(sys.argv[2], "w")

    n = int(f.readline().replace("\n", ""))  # leer el numero de escenarios
    escenarios = []

    for i in range(n):
        # print(i)
        escenarios.append(leer_escenario(f))

    for e in escenarios:
        start = timer()
        upperBound = expandir(
            0, e.pos_ini, e.pos_ini, e.lista_minas, e.n_minas, math.inf
        )
        end = timer()
        f_out.write(str(upperBound) + " " + str(end - start) + "\n")
        f_out.flush()

    f.close()
    f_out.close()
