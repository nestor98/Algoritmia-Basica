import sys
from escenario import Escenario
from solucionar import solucionar
from timeit import default_timer as timer
from arbol import Nodo

def line_to_tuple(linea):
    lista = linea.replace("\n", "").split(' ')
    return (int(lista[0]), int(lista[1]))


def leer_escenario(f):
    # la primera línea son las dimensiones
    dim = line_to_tuple(f.readline())

    # la segunda línea es la posición inicial
    pos_ini = line_to_tuple(f.readline())

    # la tercera es el número de minas
    n_minas = int(f.readline().replace("\n", ""))

    # crear objeto de tipo escenario
    e = Escenario(dim, pos_ini, n_minas)

    for _ in range(n_minas):
        e.addMina(line_to_tuple(f.readline()))  # añadir mina al escenario

    return e


def recorrer(n: Nodo):
    asdf = 1
    for e in n.listaHijos:
        asdf += recorrer(e)
    return asdf


if __name__ == '__main__':

    i_escenario = 0  # indice dentro del escenario
    f = open(sys.argv[1], "r")  # leer archivo
    f_out = open(sys.argv[2], "w")

    n = int(f.readline().replace("\n", ""))  # leer el numero de escenarios
    escenarios = []

    for i in range(n):
        # print(i)
        escenarios.append(leer_escenario(f))

    for e in escenarios:
        start = timer()
        upperBound, arbol = solucionar(e)
        end = timer()
        f_out.write(str(upperBound) + " " + str(end - start) + "\n")
        f_out.flush()

        # asdf = 0
        # for e in arbol.listaHijos:
        #     asdf = recorrer(arbol)
        # print(asdf)

    f.close()
    f_out.close()
