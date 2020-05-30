
class Escenario:

    def __init__(self, d, p, n):
        self.dim = d
        self.pos_ini = p
        self.n_minas = n
        self.lista_minas = []

    def addMina(self, mina):
        self.lista_minas.append(mina)

    def getNumMinas(self):
        return self.n_minas

    def getMinas(self):
        return self.lista_minas

    def getPosIni(self):
        return self.pos_ini

    def toString(self):
        string = "Escenario de dimensiones " + \
            str(self.dim[0]) + "x" + str(self.dim[1])
        string += ", con posicion inicial (" + str(self.pos_ini[0]) + ", " + str(
            self.pos_ini[1]) + ") y minas en las siguientes posiciones:\n"
        for mina in self.lista_minas:
            string += "(" + str(mina[0]) + ", " + str(mina[1]) + ")\n"
        return string
