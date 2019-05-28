from zwierze import *


class Owca(Zwierze):

    def __init__(self, swiat, xx, yy):
        Zwierze.__init__(self, swiat, xx, yy)
        self.setI(4)
        self.setS(4)
        self.setN("Owca")

    def sprawdzGatunek(self, o):
        return isinstance(o, Owca)

    def gatunek(self, ss, xx, yy):
        w = Owca(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'O'
