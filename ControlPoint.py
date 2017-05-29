from PyQt5.Qt import *
from StyleSheets import *


class ControlPoint(QPushButton):
    def __init__(self, isPrimary, x, y, role, *args):
        super(ControlPoint, self).__init__(*args)
        self.isPrimary = isPrimary
        self.point = QPoint(x, y)
        self.role = role
        if self.isPrimary:
            self.setStyleSheet(STYLE_PRIMARY_CP)
        else:
            self.setStyleSheet(STYLE_SECONDARY_CP)
        self.size = 10
        self.setGeometry(x-self.size/2, y-self.size/2, self.size, self.size)
        self.carryChildren = True
        self.lbl = QLabel(self.parentWidget(), text="null", pos=self.point)
        self.lbl.show()
        self.lbl.lower()

    def update(self):
        self.lbl.setText(str(self.parentWidget().pointlist.index(self)))
        self.lbl.setGeometry(QRect(self.point, self.lbl.size()))

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == 1:
            self.isPressed = True
            if self.isPrimary:
                self.myindex = self.parentWidget().pointlist.index(self)
                self.child1 = self.parentWidget().pointlist[self.myindex-1]
                self.child1diff = self.point - self.child1.point
                self.child2 = self.parentWidget().pointlist[self.myindex+1]
                self.child2diff = self.point - self.child2.point
            self.parent().update()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == 1:
            self.parentWidget().update()
            self.parent().update()
            self.isPressed = False

    def mouseMoveEvent(self, QMouseEvent):
        if self.isPressed:
            x = QMouseEvent.windowPos().x()
            y = QMouseEvent.windowPos().y()
            self.point = QPoint(x, y)
            self.setGeometry(x-self.size/2, y-self.size/2, self.size, self.size)
            if self.carryChildren & self.isPrimary:
                child1 = self.parentWidget().pointlist[self.myindex-1]
                child1.point = self.point - self.child1diff
                child1.setGeometry(child1.point.x()-child1.size/2,
                                   child1.point.y()-child1.size/2,
                                   child1.size, child1.size)
                self.child1.update()
                child2 = self.parentWidget().pointlist[self.myindex+1]
                child2.point = self.point - self.child2diff
                child2.setGeometry(child2.point.x()-child2.size/2,
                                   child2.point.y()-child2.size/2,
                                   child2.size, child2.size)
                self.child2.update()
        self.parent().update()
        self.update()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Shift:
            self.carryChildren = False

    def keyReleaseEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Shift:
            self.carryChildren = True
