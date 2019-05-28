from roslina import *


class Mlecz(Roslina):

    def __init__(self, swiat, xx, yy):
        Roslina.__init__(self, swiat, xx, yy)
        self.setS(0)
        self.setN("Mlecz")

    def sprawdzGatunek(self, o):
        return isinstance(o, Mlecz)

    def gatunek(self, ss, xx, yy):
        w = Mlecz(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'm'

    def akcja(self):
        Roslina.akcja(self)
        Roslina.akcja(self)
        Roslina.akcja(self)
