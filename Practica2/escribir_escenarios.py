# Autores: Monzón González, Néstor
#          Otero García, Andrés

import sys
from random import uniform
from escenario import Escenario
from solucionar import solucionar
from timeit import default_timer as timer
from arbol import Nodo
from math import floor

# pasa una linea con el formato definido en la práctica a una tupla (x,y), las cuales son las posiciones en los ejes del plano
def line_to_tuple(linea):
    lista = linea.replace("\n", "").split(" ")
    return (int(lista[0]), int(lista[1]))


# pasa una tupla (x,y), las cuales son las posiciones en los ejes del plano a una linea con el formato definido en la práctica
def tuple_to_line(tuple):
    return str(tuple[0]) + " " + str(tuple[1]) + "\n"


# devuelve una posición aleatoria (tuplas (x,y))
def random_pos():
    return (int(uniform(1, dim[0])), int(uniform(1, dim[1])))


# imprime en el fichero f el escenario de dimensión "dim", posición inicial de Nikita "pos_ini" y "n_minas" aleatorias
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
    f = open(sys.argv[1], "w")  # abrir el archivo
    n_escenarios = int(sys.argv[2])  # leer el numero de escenarios
    dim = (int(sys.argv[3]), int(sys.argv[4]))  # leer las dimensiones
    f.write(str(n_escenarios) + "\n")  # escribir en f el numero de fichero
    for i_esc in range(n_escenarios):
        pos_ini = random_pos()  # elegir una posicion aleatoria para Nikita
        n_minas = floor(
            i_esc / 2 + 1
        )  # se escriben 2 escenarios para cada numero de minas
        escribir_escenario(f, dim, pos_ini, n_minas)

    f.close()
