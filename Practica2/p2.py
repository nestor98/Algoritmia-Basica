import fileinput
import sys
from escenario import Escenario


def list_to_tuple(lista):
    return (int(lista[0]), int(lista[1]))

if __name__ == '__main__':
    nescenarios = 0
    i_escenario = 0 # indice dentro del escenario
    en_escenario = True
    escenarios = []
    dimensiones = 0
    pos_ini = 0
    n_bombas = 0
    for i, line in enumerate(fileinput.input(sys.argv[1])):
        lista=line.split(' ')
        if lista[0] != '':
            if i == 0: # primera linea
                nescenarios = int(lista[0])
            else: # estamos en un escenario
                if i_escenario == 0: # dimensiones
                    dimensiones = list_to_tuple(lista)#(int(lista[0]), int(lista[1])) # tupla con las dimensiones

                elif i_escenario == 1: # pos inicial
                    pos_ini = list_to_tuple(lista)

                elif i_escenario == 2: # num de bombas
                    n_bombas = int(lista[0])
                    escenarios.append(Escenario(dimensiones, pos_ini, n_bombas))

                else: # posicion de cada bomba
                    pos_bomba = list_to_tuple(lista)
                    escenarios[-1].add_bomb(pos_bomba)
                    #print(pos_bomba)
                    if i_escenario == n_bombas + 2:
                        i_escenario = -1 # para que sea 0 con el +1
                i_escenario += 1
                #print(i_escenario, '.....',line)

    for escenario in escenarios:
        print(escenario)
        print('--------------------------------------')
