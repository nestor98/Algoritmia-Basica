
# TODO: revisar implementacion
def costeL1(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

class Nodo:
    # puede que le pasemos la pos de nikita y la del nodo para calcular su coste
    def __init__(self, pos_nikita, mi_pos):#pos, coste):
        self.pos = mi_pos
        self.coste = costeL1(pos_nikita, mi_pos) # supongo

    def coste(self):
        return self.coste


    def __str__(self):
        return 'pos: ' + str(self.pos) + '\n' + 'coste: ' + str(self.coste)


if __name__ == '__main__': # test
    nodo = Nodo((1,5), (3,7))
    print(nodo)
