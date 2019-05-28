from roslina import *


class Trawa(Roslina):

    def __init__(self, swiat, xx, yy):
        Roslina.__init__(self, swiat, xx, yy)
        self.setS(0)
        self.setN("Trawa")

    def sprawdzGatunek(self, o):
        return isinstance(o, Trawa)

    def gatunek(self, ss, xx, yy):
        w = Trawa(ss, xx, yy)
        return w

    def rysowanie(self):
        return 't'
