from organizm import *
from punkt import *
from random import seed, randint

class Roslina(Organizm):

    def __init__(self, swiat, xx, yy):
        Organizm.__init__(self, swiat, xx, yy)
        self.setI(0)
        self.kier = self.s.getKierunki(self.y)

    def getPoprawnyPunktDocel(self, punkt, zas, startX, startY):
        ret = []
        for i in range(1, zas+1):
            nowyPunkt = Punkt(startX + punkt.x*i, startY + punkt.y*i)
            if self.s.jestWGranicachP(nowyPunkt):
                ret.append(nowyPunkt)
        return ret

    def getPoprawnyKier(self, startX, startY, zajety):
        poprawneMiejsce = []
        for i in range(len(self.kier)):
            punkt2 = Punkt(self.kier[i].x + startX, self.kier[i].y+startY)
            if self.s.jestWGranicachP(punkt2):
                if zajety:
                    poprawneMiejsce.append(self.kier[i])
                elif not(self.s.istniejeOrganizm(punkt2.x, punkt2.y)):
                    poprawneMiejsce.append(self.kier[i])
        return poprawneMiejsce

    def WykonajRuch(self, punktyDocel):
        for i in range(len(punktyDocel)):
            if self.s.istniejeOrganizm(punktyDocel[i].x, punktyDocel[i].y):
                o = self.s.znajdzOrganizm(punktyDocel[i].x, punktyDocel[i].y)
                o.kolizja(self)
                break
            else:
                self.x = punktyDocel[i].x
                self.y = punktyDocel[i].y

    def akcja(self):
        self.kier = self.s.getKierunki(self.y)
        seed()
        rozmnoz = randint(0, 99)
        if rozmnoz < 5:
            poprawnyKier = self.getPoprawnyKier(self.x, self.y, False)
            if len(poprawnyKier) < 1:
                return
            wylosowana = randint(0, len(poprawnyKier) - 1)
            d = self.getPoprawnyPunktDocel(poprawnyKier[wylosowana], 1, self.x, self.y)
            dziecko = d[0]
            self.s.dodajOrganizm(self.gatunek(self.s, dziecko.x, dziecko.y))
            print("Organizm "+self.nazwa+" rozmnaza sie")

    def Walka(self, attk):
        if self.getS() > attk.getS():
            usun = attk
            print("Organizm "+self.nazwa+" pokonal "+attk.getN())
        else:
            usun = self
            print("Organizm "+attk.getN()+" pokonal "+self.nazwa)
        self.s.lista.remove(usun)
        if attk != usun:
            attk.setX(usun.getX())
            attk.setY(usun.getY())



    def kolizja(self, attk):
        if self.sprawdzGatunek(attk):
            poprawnyKier = self.getPoprawnyKier(self.x, self.y, False)
            if len(poprawnyKier) < 1:
                return
            seed()
            wylosowana = randint(0, len(poprawnyKier) - 1)
            d = self.getPoprawnyPunktDocel(poprawnyKier[wylosowana], 1, self.x, self.y)
            dziecko = d[0]
            self.s.dodajOrganizm(self.gatunek(self.s, dziecko.x, dziecko.y))
            print("Organizm "+self.nazwa+" rozmnaza sie")
        else:
            self.Walka(attk)