import sys
from random import uniform
from escenario import Escenario
from solucionar import solucionar
from timeit import default_timer as timer
from arbol import Nodo

def line_to_tuple(linea):
    lista = linea.replace("\n", "").split(' ')
    return (int(lista[0]), int(lista[1]))

def tuple_to_line(tuple):
    return str(tuple[0]) + ' ' + str(tuple[1])


def escribir_escenario(dim, pos_ini, n_minas):
    # la primera línea son las dimensiones
    # dim = line_to_tuple(f.readline())
    print(tuple_to_line(dim))
    # la segunda línea es la posición inicial
    # pos_ini = line_to_tuple(f.readline())
    print(tuple_to_line(pos_ini))

    # la tercera es el número de minas
    # n_minas = int(f.readline().replace("\n", ""))
    print(n_minas)

    for _ in range(n_minas):
        pos = (int(uniform(1, dim[0])), int(uniform(1, dim[1])))
        print(tuple_to_line(pos))


def recorrer(n: Nodo):
    asdf = 1
    for e in n.listaHijos:
        asdf += recorrer(e)
    return asdf


if __name__ == '__main__':
    n_escenarios = 50
    dim = (10,10)
    pos_ini = (1,1)
    n_minas = 4
    print(n_escenarios)
    for i_esc in range(n_escenarios):
        escribir_escenario(dim, pos_ini, n_minas)
