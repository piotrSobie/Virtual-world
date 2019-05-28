from zwierze import *


class Zolw(Zwierze):

    def __init__(self, swiat, xx, yy):
        Zwierze.__init__(self, swiat, xx, yy)
        self.setI(1)
        self.setS(2)
        self.setN("Zolw")

    def sprawdzGatunek(self, o):
        return isinstance(o, Zolw)

    def gatunek(self, ss, xx, yy):
        w = Zolw(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'Z'

    def WykonajRuch(self, punktyDocel):
        seed()
        wylosowana = randint(0, 3)
        if wylosowana < 3:
            print("Zolw nie poruszyl sie")
            return
        Zwierze.WykonajRuch(self, punktyDocel)

    def Walka(self, attk):
        if attk.getS() < 5:
            print("Zolw odparl atak "+attk.getN())
            return
        Zwierze.Walka(self, attk)
