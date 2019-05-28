from roslina import *


class Guarana(Roslina):

    def __init__(self, swiat, xx, yy):
        Roslina.__init__(self, swiat, xx, yy)
        self.setS(0)
        self.setN("Guarana")

    def sprawdzGatunek(self, o):
        return isinstance(o, Guarana)

    def gatunek(self, ss, xx, yy):
        w = Guarana(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'g'

    def Walka(self, attk):
        attk.setS(attk.getS() + 3)
        print("Organizm "+attk.getN()+" zwieksza swoja sile do "+str(attk.getS()))
        Roslina.Walka(self, attk)
