from zwierze import *


class Lis(Zwierze):

    def __init__(self, swiat, xx, yy):
        Zwierze.__init__(self, swiat, xx, yy)
        self.setI(7)
        self.setS(3)
        self.setN("Lis")

    def sprawdzGatunek(self, o):
        return isinstance(o, Lis)

    def gatunek(self, ss, xx, yy):
        w = Lis(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'L'

    def WykonajRuch(self, punktyDocel):
        for i in range(len(punktyDocel)):
            o = self.s.znajdzOrganizm(punktyDocel[i].x, punktyDocel[i].y)
            if (o is not None) and (o.getS() > self.getS()):
                print("Lis napotkal organizm silniejszy "+o.getN())
                return
        Zwierze.WykonajRuch(self, punktyDocel)