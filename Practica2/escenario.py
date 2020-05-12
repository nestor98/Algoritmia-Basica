


class Escenario:
    def __init__(self, dimensiones, pos_ini, n_bombas):
        self.dimensiones = dimensiones
        self.pos_ini = pos_ini
        self.n_bombas = n_bombas
        self.pos_bombas = []

    def add_bomb(self, pos):
        self.pos_bombas += pos
