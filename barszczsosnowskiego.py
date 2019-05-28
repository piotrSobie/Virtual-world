from roslina import *
from cyberowca import *

class BarszczSosnowskiego(Roslina):

    def __init__(self, swiat, xx, yy):
        Roslina.__init__(self, swiat, xx, yy)
        self.setS(10)
        self.setN("BarszczSosnowskiego")

    def sprawdzGatunek(self, o):
        return isinstance(o, BarszczSosnowskiego)

    def gatunek(self, ss, xx, yy):
        w = BarszczSosnowskiego(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'b'

    def akcja(self):
        poprawnyKier = self.getPoprawnyKier(self.x, self.y, True)
        for i in range(len(poprawnyKier)):
            xx = poprawnyKier[i].x + self.x
            yy = poprawnyKier[i].y + self.y
            if (self.s.istniejeOrganizm(xx, yy)) and not(isinstance(self.s.znajdzOrganizm(xx, yy), CyberOwca)):
                if self.s.znajdzOrganizm(xx, yy).getI() > 0:
                    print("Organizm "+self.s.znajdzOrganizm(xx, yy).getN()+"  wszedl w pole razenia Barszczu Sosnowskiego")
                    self.s.lista.remove(self.s.znajdzOrganizm(xx, yy))
        Roslina.akcja(self)

    def Walka(self, attk):
        if not isinstance(attk, CyberOwca):
            self.s.lista.remove(self)
            self.s.lista.remove(attk)
            print("Organizm "+attk.getN()+" zjadl Barszcz Sosnowskiego, przez co umarl")
        else:
            Roslina.Walka(self, attk)
