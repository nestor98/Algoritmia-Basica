import fileinput
import sys
from escenario import Escenario


def list_to_tuple(lista):
    return (int(lista[0]), int(lista[0]))


if __name__ == '__main__':
    nescenarios = 0
    i_escenario = 0 # indice dentro del escenario
    for i,line in enumerate(fileinput.input(sys.argv[1])):
        lista=line[:-1].split(' ')
        if i == 1: # primera linea
            nescenarios = int(lista[0])
        else:
            dimensiones = (int(lista[0]), int(lista[1])) # tupla con las dimensiones
            pos_ini = fileinput.input(sys.argv[1])[:-1].split(' ')

            escenarios[0] = Escenario(dimensiones)



        if len(lista)>1:
            if i > 1: # sig lineas
                if i%2==0: # primera
                    if len(lista) > 3:
                        exit(1)
                        print('DEMASIADOS NUMEROSSSSSSSSS')
                                # id, num_b, dias_libro,  tiempo_sign
                    #print(lista)
                    biblio = Biblioteca(int(i/2)-1, lista[0], lista[2], lista[1])
                    biblios.append(biblio)
                else:
                    biblios[-1].set_books(lista, [libros[int(i)] for i in lista])


            elif i>0: # segunda, libros
                libros = lista
            else: # primera, numeros
                n_libros = lista[0]
                n_biblio = lista[1]
                n_dias = lista[2]
