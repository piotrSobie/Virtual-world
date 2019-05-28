from zwierze import *
from owca import *

class CyberOwca(Owca):

    def __init__(self, swiat, xx, yy):
        Owca.__init__(self, swiat, xx, yy)
        self.setI(4)
        if self.s.czyJestBarszcz():
            self.setS(11)
            self.setN("CyberOwca")
        else:
            self.setS(4)
            self.setN("Owca")

    def sprawdzGatunek(self, o):
        if self.s.czyJestBarszcz():
            return type(o) == CyberOwca# type(...) zwraca dokładny typ
        return isinstance(o, Owca)# tym samym albo podklasa

    def gatunek(self, ss, xx, yy):
        if self.s.czyJestBarszcz():
            return CyberOwca(ss, xx, yy)
        return Owca(ss, xx, yy)

    def rysowanie(self):
        if self.s.czyJestBarszcz():
            return 'Y'
        return 'O'

    def akcja(self):
        if self.s.czyJestBarszcz():
            self.setS(11)
            self.setN("CyberOwca")
            kier = self.s.znajdzKierDoBarszczu(self.x, self.y)
            punktyDocel = self.getPoprawnyPunktDocel(kier, self.zasieg, self.x, self.y)
            self.WykonajRuch(punktyDocel)
        else:
            self.setS(4)
            self.setN("Owca")
            Zwierze.akcja(self)

