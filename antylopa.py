from zwierze import *


class Antylopa(Zwierze):

    def __init__(self, swiat, xx, yy):
        Zwierze.__init__(self, swiat, xx, yy)
        self.setI(4)
        self.setS(4)
        self.setN("Antylopa")
        self.zasieg = 2

    def sprawdzGatunek(self, o):
        return isinstance(o, Antylopa)

    def gatunek(self, ss, xx, yy):
        w = Antylopa(ss, xx, yy)
        return w

    def rysowanie(self):
        return 'A'

    def Walka(self, attk):
        seed()
        wylosowana = randint(0, 1)
        kierunki = self.getPoprawnyKier(self.x, self.y, False)
        if (wylosowana == 0) and (len(kierunki) > 0):
            print("Antylopa ucieka")
            zmiana = kierunki[randint(0, len(kierunki) - 1)]
            self.x += zmiana.x
            self.y += zmiana.y
        else:
            Zwierze.Walka(self, attk)
