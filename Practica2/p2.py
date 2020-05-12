import fileinput
import sys
from escenario import Escenario


def list_to_tuple(lista):
    return (int(lista[0]), int(lista[0]))


if __name__ == '__main__':
    nescenarios = 0
    i_escenario = 0 # indice dentro del escenario
    en_escenario = True
    escenarios = []
    dimensiones = 0
    pos_ini = 0
    n_bombas = 0
    for i, line in enumerate(fileinput.input(sys.argv[1])):
        lista=line[:-1].split(' ')
        if i == 1: # primera linea
            nescenarios = int(lista[0])
        elif i_escenario == 0:
            dimensiones = list_to_tuple(lista)#(int(lista[0]), int(lista[1])) # tupla con las dimensiones
            i_escenario += 1
        elif i_escenario == 1:
            pos_ini = list_to_tuple(lista)
            i_escenario += 1
        elif i_escenario == 2:
            n_bombas = int(lista[0])
            escenarios.append(Escenario(dimensiones, pos_ini, n_bombas))
            i_escenario += 1
        else:
            pass
