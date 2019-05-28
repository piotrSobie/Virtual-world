from roslina import *


class WilczeJagody(Roslina):

    def __init__(self, swiat, xx, yy):
        Roslina.__init__(self, swiat, xx, yy)
        self.setS(99)
        self.setN("WilczeJagody")

    def sprawdzGatunek(self, o):
        return isinstance(o, WilczeJagody)

    def gatunek(self, ss, xx, yy):
        w = WilczeJagody(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'j'

    def Walka(self, attk):
        self.s.lista.remove(self)
        self.s.lista.remove(attk)
        print("Organizm "+attk.getN()+" zjadl Wilcza Jagode, przez co umral")