import sys
from random import uniform
from escenario import Escenario
from solucionar import solucionar
from timeit import default_timer as timer
from arbol import Nodo
from math import floor


def line_to_tuple(linea):
    lista = linea.replace("\n", "").split(" ")
    return (int(lista[0]), int(lista[1]))


def tuple_to_line(tuple):
    return str(tuple[0]) + " " + str(tuple[1]) + "\n"


def random_pos():
    return (int(uniform(1, dim[0])), int(uniform(1, dim[1])))


def escribir_escenario(f, dim, pos_ini, n_minas):
    # la primera línea son las dimensiones
    # dim = line_to_tuple(f.readline())
    f.write(tuple_to_line(dim))
    # la segunda línea es la posición inicial
    # pos_ini = line_to_tuple(f.readline())
    f.write(tuple_to_line(pos_ini))

    # la tercera es el número de minas
    # n_minas = int(f.readline().replace("\n", ""))
    f.write(str(n_minas) + "\n")

    for _ in range(n_minas):
        pos = random_pos()
        f.write(tuple_to_line(pos))


if __name__ == "__main__":
    f = open(sys.argv[1], "w")
    n_escenarios = int(sys.argv[2])
    dim = (int(sys.argv[3]), int(sys.argv[4]))
    f.write(str(n_escenarios) + "\n")
    for i_esc in range(n_escenarios):
        pos_ini = random_pos()
        n_minas = floor(i_esc / 2 + 1)
        escribir_escenario(f, dim, pos_ini, n_minas)

    f.close()
