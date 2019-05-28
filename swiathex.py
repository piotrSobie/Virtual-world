from swiat import *
from PySide import QtGui, QtCore


class GlOkno(QtGui.QWidget):
    rozmiar = 50

    def __init__(self, s):
        super().__init__()
        self.s = s

        self.setGeometry(100, 100, (s.getB() + 0.5)*self.rozmiar, s.getA()*self.rozmiar)
        self.setFixedSize(self.size())
        self.setWindowTitle('Gra')
        self.installEventFilter(self)
        self.show()
        self.menu = QtGui.QMenu(self)
        self.menu.addAction('W  Wilk')
        self.menu.addAction('O  Owca')
        self.menu.addAction('L  Lis')
        self.menu.addAction('Z Zolw')
        self.menu.addAction('A Antylopa')
        self.menu.addAction('Y CyberOwca')
        self.menu.addAction('t Trawa')
        self.menu.addAction('m Mlecz')
        self.menu.addAction('g Guarana')
        self.menu.addAction('j WilczeJagody')
        self.menu.addAction('b BarszczSosnowskiego')

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor(0, 0, 0))
        qp.setFont(QtGui.QFont('Arial', 12))
        for o in self.s.lista:
            x = o.getX()*self.rozmiar
            if o.getY() % 2 == 0:
                x += self.rozmiar/2
            y = o.getY()*self.rozmiar
            qp.drawText(x, y, self.rozmiar, self.rozmiar, QtCore.Qt.AlignCenter, o.rysowanie())
        for x in range(self.s.getB()):
            for y in range(self.s.getA()):
                if not self.s.istniejeOrganizm(x, y):
                    wndX = (x+0.5)*self.rozmiar
                    if y % 2 == 0:
                        wndX += self.rozmiar/2
                    qp.drawPoint(wndX, (y+0.5)*self.rozmiar)
        qp.end()

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key == QtCore.Qt.Key_Up:
                self.s.getClowiek().setK(Punkt(0, -1))
                self.s.wykonajTure()
            elif key == QtCore.Qt.Key_Down:
                self.s.getClowiek().setK(Punkt(0, 1))
                self.s.wykonajTure()
            elif key == QtCore.Qt.Key_Right:
                self.s.getClowiek().setK(Punkt(1, 0))
                self.s.wykonajTure()
            elif key == QtCore.Qt.Key_Left:
                self.s.getClowiek().setK(Punkt(-1, 0))
                self.s.wykonajTure()
            elif key == QtCore.Qt.Key_W:
                self.s.wczytaj()
                self.s.znajdzCzlowieka()
                print("Wczytano stan z pliku")
            elif key == QtCore.Qt.Key_Z:
                self.s.zapisz()
                print("Zapisano stan")
            elif key == QtCore.Qt.Key_U:
                if self.s.getClowiek().getW():
                    print("Wlaczono umiejetnosc specjalna")
                    self.s.getClowiek().setL(5)
                    self.s.getClowiek().setSp(True)
                    self.s.getClowiek().setW(False)
                else:
                    print("Nie mozna jeszcze wlaczyc umiejetnosci specjalnej")
            self.repaint()
            return True
        return QtGui.QWidget.eventFilter(self, widget, event)

    def contextMenuEvent(self, event):
        x, y = self.zmienOkPosDoSwPos(event.pos())
        if not self.s.istniejeOrganizm(x, y):
            ret = self.menu.exec_(event.globalPos())
            if ret is not None:
                nameZnak = ret.text()[0]
                organizm = self.s.znajdz(nameZnak, x, y)
                self.s.dodajOrganizm(organizm)
                self.repaint()
        # print(event.pos(), x, y)

    def zmienOkPosDoSwPos(self, pos):
        return pos.x()//self.rozmiar, pos.y()//self.rozmiar

class SwiatHex(Swiat):

    def __init__(self, aa, bb):
        Swiat.__init__(self, aa, bb)
        self.okno = GlOkno(self)

    def getKierunki(self, y):
        if y % 2 == 1:
            return [
                Punkt(-1, 0),
                Punkt(1, 0),
                Punkt(0, 1),
                Punkt(0, -1),
                Punkt(-1, -1),
                Punkt(-1, 1)
            ]
        return [
                Punkt(-1, 0),
                Punkt(1, 0),
                Punkt(0, 1),
                Punkt(0, -1),
                Punkt(1, 1),
                Punkt(1, -1)
            ]
