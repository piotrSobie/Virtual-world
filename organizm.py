class Organizm:

    def __init__(self, swiat, xx, yy):
        self.s = swiat
        self.x = xx
        self.y = yy
        self.sila = None
        self.inicjatywa = None
        self.nazwa = None
        self.kierunek = None

    def getS(self):
        return self.sila

    def setS(self, x):
        self.sila = x

    def getI(self):
        return self.inicjatywa

    def setI(self, x):
        self.inicjatywa = x

    def getX(self):
        return self.x

    def setX(self, a):
        self.x = a

    def getY(self):
        return self.y

    def setY(self, a):
        self.y = a

    def getN(self):
        return self.nazwa

    def setN(self, a):
        self.nazwa = a

    def getK(self):
        return self.kierunek

    def setK(self, p):
        self.kierunek = p
