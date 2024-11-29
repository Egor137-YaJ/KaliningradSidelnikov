import sys
from PyQt6.QtCore import Qt, QPointF, QRectF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QWidget, QApplication
from random import randint as ri
from math import *


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.STATUS = 0
        self.coords = (None, None)
        self.flag = False
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Суперматизм')

    def mouseMoveEvent(self, event):
        self.coords = event.pos().x(), event.pos().y()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.STATUS = 3
            self.draw()
            print('had drawn circle!')

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.STATUS = 4
            self.draw()
        elif event.button() == Qt.MouseButton.RightButton:
            self.STATUS = 2
            self.draw()

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.painter = QPainter()
            self.painter.begin(self)
            self.draw_ev(self.painter)
            self.painter.end()
        self.flag = False

    def draw_ev(self, p):
        D = ri(20, 100)
        r, g, b = ri(0, 255), ri(0, 255), ri(0, 255)
        p.setBrush(QColor(r, g, b))
        x, y = self.coords
        if self.STATUS == 4:
            x, y = x - D / 4, y - D / 4
            p.drawEllipse(QPointF(x, y), D, D)

        if self.STATUS == 2:
            x, y = x - D / 2, y - D / 2
            p.drawRect(QRectF(x, y, D, D))

        if self.STATUS == 3:
            coords = QPolygonF([QPointF(x, y - D),
                                QPointF(x + cos(7 * pi / 6) * D,
                                        y - sin(7 * pi / 6) * D),
                                QPointF(x + cos(11 * pi / 6) * D,
                                        y - sin(11 * pi / 6) * D)])
            p.drawPolygon(coords)
        self.STATUS = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
