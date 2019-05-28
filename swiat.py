from czlowiek import *
from wilk import *
from lis import *
from zolw import *
from antylopa import *
from trawa import *
from mlecz import *
from guarana import *
from wilczejagody import *
from barszczsosnowskiego import *
from cyberowca import *

class Swiat:

    def __init__(self, aa, bb):
        self.a = aa
        self.b = bb
        self.nrTury = 1
        self.lista = []
        self.czlowiek = None
        self.stan = [[0 for y in range(self.a)] for x in range(self.b)]  # wiersze = a, kolumny = b
        for i in range(self.b):
            for j in range(self.a):
                self.stan[i][j] = '#'

    def rysujSwiat(self):
        for i in range(self.b):
            for j in range(self.a):
                print(self.stan[i][j], end='')
            print()

    def wykonajTure(self):
        licznik = 0
        while licznik < len(self.lista):
            self.lista[licznik].akcja()
            licznik += 1
        for i in range(self.b):
            for j in range(self.a):
                self.stan[i][j] = '#'
        licznik = 0
        while licznik < len(self.lista):
            self.stan[self.lista[licznik].getX()][self.lista[licznik].getY()] = self.lista[licznik].rysowanie()
            licznik += 1
        print("Koniec tury "+str(self.nrTury))
        self.nrTury+=1

    def dodajOrganizm(self, o):
        warunek = True
        pozycja = 0
        temp = []
        if len(self.lista) == 0:
            self.lista.append(o)
        else:
            while warunek:
                if o.getI() > self.lista[pozycja].getI():
                    temp.append(o)
                    warunek = False
                else:
                    temp.append(self.lista[pozycja])
                    pozycja += 1
                    if pozycja == len(self.lista):
                        temp.append(o)
                        warunek = False
        for i in range(pozycja, len(self.lista)):
            temp.append(self.lista[i])
        self.lista = temp

    def znajdzOrganizm(self, x, y):
        for i in range(len(self.lista)):
            if self.lista[i].getX() == x and self.lista[i].getY() == y:
                return self.lista[i]
        return None

    def znajdzCzlowieka(self):
        for o in self.lista:
            if isinstance(o, Czlowiek):
                self.czlowiek = o
                break

    def getClowiek(self):
        return self.czlowiek

    def istniejeOrganizm(self, x, y):
        for i in range(len(self.lista)):
            if self.lista[i].getX() == x and self.lista[i].getY() == y:
                return True
        return False

    def znajdz(self, q, x, y):
        if q == 'C':
            return Czlowiek(self, x, y)
        elif q == 'W':
            return Wilk(self, x, y)
        elif q == 'O':
            return Owca(self, x, y)
        elif q == 'L':
            return Lis(self, x, y)
        elif q == 'Z':
            return Zolw(self, x, y)
        elif q == 'A':
            return Antylopa(self, x, y)
        elif q == 't':
            return Trawa(self, x, y)
        elif q == 'm':
            return Mlecz(self, x, y)
        elif q == 'g':
            return Guarana(self, x, y)
        elif q == 'j':
            return WilczeJagody(self, x, y)
        elif q == 'b':
            return BarszczSosnowskiego(self, x, y)
        elif q == 'Y':
            return CyberOwca(self, x, y)
        return None

    def dodajOrganizmPlik(self, o, l):
        if l == 0:
            temp = []
            temp.append(o)
            self.lista = temp
        else:
            self.lista.append(o)

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getNrTury(self):
        return self.nrTury

    def jestWGranicachP(self, p):
        return p.x >= 0 and p.y >=0 and p.x < self.b and p.y < self.a

    def jestWGranicach(self, x , y):
        return x >= 0 and y >= 0 and x < self.b and y < self.a

    def zapisz(self):
        plik = open('zapis.txt', 'w')
        for i in range(len(self.lista)):
            plik.write(self.lista[i].rysowanie())
            plik.write(str(self.lista[i].getX()))
            plik.write(str(self.lista[i].getY()))
        plik.close()

    def wczytaj(self):
        text = open('zapis.txt').read()
        l = 0
        for i in range(0, len(text), 3):
            for j in range(3):
                if j == 0:
                    nazwa = text[i + j]
                elif j == 1:
                    xx = text[i + j]
                else:
                    yy = text[i + j]
            self.dodajOrganizmPlik(self.znajdz(nazwa, int(xx), int(yy)), l)
            l += 1

    def getKierunki(self, y):
        return

    def czyJestBarszcz(self):
        for o in self.lista:
            if isinstance(o, BarszczSosnowskiego):
                return True
        return False

    def znajdzKierDoBarszczu(self, x, y):
        min = -1
        barszcz = None
        for o in self.lista:
            if isinstance(o, BarszczSosnowskiego):
                kwodl = (x-o.getX())**2 + (y-o.getY())**2
                if kwodl > min:
                    min = kwodl
                    barszcz = o

        def znak(x): # jeśli x > 0 to zwraca 1, jeśli x < 0 to zwraca -1, jeśli x == 0 to zwraca 0
            return (1 if x > 0 else -1) if x != 0 else 0

        dx = znak(o.getX()-x)
        if dx != 0: # najpierw idziemy po x
            return Punkt(dx, 0)
        dy = znak(o.getY()-y)
        return Punkt(0, dy)

    def oknoSymulacji(self):
        self.okno.show()

