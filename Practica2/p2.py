"""
Autores: Andres Otero y Nestor Monzon
Asignatura: Algoritmia Básica
Ejecucion: python3 p2.py <entrada.txt> <salida.txt>
Escribe en <salida.txt> las soluciones (y los tiempos) a los escenarios descritos en
<entrada.txt>, ambos con la sintaxis descrita en el enunciado de la práctica
"""
import sys
from escenario import Escenario
from escenario import leer_escenario
from solucionar import solucionar
from timeit import default_timer as timer
from arbol import Nodo

if __name__ == '__main__':

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

    f.close()
    f_out.close()
