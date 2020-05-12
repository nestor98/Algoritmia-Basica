


class Escenario:
    def __init__(self, dimensiones, pos_ini, n_bombas):
        self.dimensiones = dimensiones
        self.pos_ini = pos_ini
        self.n_bombas = n_bombas
        self.pos_bombas = []

    def add_bomb(self, pos):
        self.pos_bombas.append(pos)# += pos

    def __str__(self):
        string = 'dimensiones: ' + str(self.dimensiones) + '\n'
        string += 'pos_ini: ' + str(self.pos_ini) + '\n'
        string += 'n_bombas: ' + str(self.n_bombas) + '\n'
        string += 'pos_bombas: ' + str(self.pos_bombas)
        return string
