
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



class Escenario:

    def __init__(self, d, p, n):
        self.dim = d
        self.pos_ini = p
        self.n_minas = n
        self.lista_minas = []

    def addMina(self, mina):
        if mina not in self.lista_minas:
            self.lista_minas.append(mina)
        else:
            self.n_minas -= 1

    def toString(self):
        string = "Escenario de dimensiones " + \
            str(self.dim[0]) + "x" + str(self.dim[1])
        string += ", con posicion inicial (" + str(self.pos_ini[0]) + ", " + str(
            self.pos_ini[1]) + ") y minas en las siguientes posiciones:\n"
        for mina in self.lista_minas:
            string += "(" + str(mina[0]) + ", " + str(mina[1]) + ")\n"
        return string
