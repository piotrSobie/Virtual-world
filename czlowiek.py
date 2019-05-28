from zwierze import *


class Czlowiek(Zwierze):

    def __init__(self, swiat, xx, yy):
        Zwierze.__init__(self, swiat, xx, yy)
        self.setI(4)
        self.setS(5)
        self.setN("Czlowiek")
        self.specjalna = False
        self.licznik = 0
        self.wlacz = True

    def sprawdzGatunek(self, o):
        return isinstance(o, Czlowiek)

    def gatunek(self, ss, xx, yy):
        w = Czlowiek(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'C'

    def setSp(self, x):
        self.specjalna = x

    def getSp(self):
        return self.specjalna

    def setL(self, x):
        self.licznik = x

    def getL(self):
        return self.licznik

    def setW(self, x):
        self.wlacz = x

    def getW(self):
        return self.wlacz

    def akcja(self):
        if self.getK() is None:
            return
        punktyDocel = self.getPoprawnyPunktDocel(self.getK(), self.zasieg, self.x, self.y)
        self.WykonajRuch(punktyDocel)
        self.setK(None)
        if self.licznik < 1:
            self.specjalna = False
        if self.licznik <= -5:
            self.wlacz = True
        if self.specjalna:
            print("Pozostalo "+str(self.licznik)+" tur umiejetnosci specjalnej")
        self.licznik -= 1

    def Walka(self, attk):
        if self.specjalna:
            if attk.getI() > 0:
                print("Czlowiek odstraszyl zwierze "+attk.getN())
                kierunki = attk.getPoprawnyKier(attk.getX(), attk.getY(), False)
                seed()
                wylosowana = randint(0, len(kierunki) - 1)
                zmiana = kierunki[wylosowana]
                attk.setX(attk.getX()+zmiana.x)
                attk.setY(attk.getY()+zmiana.y)
                return
        Zwierze.Walka(self, attk)