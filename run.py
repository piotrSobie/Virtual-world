from swiatkw import *
from swiathex import *
from czlowiek import *
from wilk import *
from owca import *
from lis import *
from zolw import *
from antylopa import *
from trawa import *
from mlecz import *
from guarana import *
from wilczejagody import *
from barszczsosnowskiego import *
from cyberowca import *
from punkt import *
import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

class OknoWyboru(QtGui.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ustawienia gry')
        self.spinW = QtGui.QSpinBox(self)
        self.spinW.setMinimum(2)
        self.spinW.setValue(8)
        self.spinH = QtGui.QSpinBox(self)
        self.spinH.setMinimum(2)
        self.spinH.setValue(8)
        self.btn = QtGui.QPushButton('OK')
        self.sw = QtGui.QComboBox(self)
        self.sw.addItem('Świat kwadratowy')
        self.sw.addItem('Świat hex')
        self.setMinimumWidth(250)

        vb = QtGui.QVBoxLayout()
        vb.addWidget(self.sw)
        vb.addWidget(QtGui.QLabel('Szerokość:'))
        vb.addWidget(self.spinW)
        vb.addWidget(QtGui.QLabel('Wysokość:'))
        vb.addWidget(self.spinH)
        vb.addWidget(self.btn)

        self.btn.clicked.connect(self.akceptuj)

        self.setLayout(vb)

        self.w = None
        self.h = None
        self.type = None

    def akceptuj(self):
        self.w = int(self.spinW.value())
        self.h = int(self.spinH.value())
        self.type = self.sw.currentIndex()
        self.accept()

tryb = OknoWyboru()
tryb.exec_()

if tryb.type == 0:
    s = SwiatKw(tryb.w, tryb.h)
else:
    s = SwiatHex(tryb.w, tryb.h)

s.dodajOrganizm(Czlowiek(s, 0, 0))
s.znajdzCzlowieka()
s.dodajOrganizm(Owca(s, 6, 6))
s.dodajOrganizm(Owca(s, 7, 7))
s.dodajOrganizm(Wilk(s, 0, 4))
s.dodajOrganizm(Wilk(s, 0, 5))
s.dodajOrganizm(Lis(s, 2, 5))
s.dodajOrganizm(Lis(s, 3, 5))
s.dodajOrganizm(Zolw(s, 3, 8))
s.dodajOrganizm(Zolw(s, 5, 5))
s.dodajOrganizm(Antylopa(s, 6, 0))
s.dodajOrganizm(Antylopa(s, 4, 0))
s.dodajOrganizm(CyberOwca(s, 8, 8))
s.dodajOrganizm(CyberOwca(s, 8, 0))
s.dodajOrganizm(Trawa(s, 3, 3))
s.dodajOrganizm(Mlecz(s, 5, 8))
s.dodajOrganizm(Guarana(s, 2, 8))
s.dodajOrganizm(WilczeJagody(s, 3, 7))
s.dodajOrganizm(BarszczSosnowskiego(s, 7, 3))

s.oknoSymulacji()

sys.exit(app.exec_())
