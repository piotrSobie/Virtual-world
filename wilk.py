from zwierze import *


class Wilk(Zwierze):

    def __init__(self, swiat, xx, yy):
        Zwierze.__init__(self, swiat, xx, yy)
        self.setI(5)
        self.setS(9)
        self.setN("Wilk")

    def sprawdzGatunek(self, o):
        return isinstance(o, Wilk)

    def gatunek(self, ss, xx, yy):
        w = Wilk(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'W'
