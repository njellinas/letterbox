from ControlPoint import *


class CurveEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.pointlist = list()
        self.pointlist = [ControlPoint(0, 24, 380, 'none', self),
                          ControlPoint(1, 24, 340, 'origin', self),
                          ControlPoint(0, 35, 80, 'none', self),
                          ControlPoint(0, 447, 10, 'none', self),
                          ControlPoint(1, 395, 36, 'none', self),
                          ControlPoint(0, 169, 148, 'none', self),
                          ControlPoint(0, 459, 332, 'none', self),
                          ControlPoint(1, 459, 332, 'none', self),
                          ControlPoint(0, 470, 340, 'none', self)]
        for each in self.pointlist:
            each.update()
        self.isClosed = False
        self.updatePath()
        for bt in self.pointlist:
            bt.show()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Curve editor')
        self.btclosetexts = ['Close curve', 'Open curve']
        hbox = QHBoxLayout()
        self.btClosecurve = QPushButton()
        self.btClosecurve.setText(self.btclosetexts[0])
        hbox.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addWidget(self.btClosecurve)
        self.lvPoints = QListWidget()
        vbox.addWidget(self.lvPoints)
        hbox.addLayout(vbox)
        self.setLayout(hbox)
        self.show()
        self.btClosecurve.clicked.connect(self.closeOpenCurve)
        for each in self.pointlist:
            self.lvPoints.addItem('point ' + str(self.pointlist.index(each)) + ': ' + each.role)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == 1:
            self.addPoint(ControlPoint(0, QMouseEvent.pos().x()+10, QMouseEvent.pos().y()+10, 'none', self))
            self.addPoint(ControlPoint(1, QMouseEvent.pos().x(), QMouseEvent.pos().y(), 'none', self))
            self.addPoint(ControlPoint(0, QMouseEvent.pos().x()-10, QMouseEvent.pos().y()-10, 'none', self))
            self.path.cubicTo(self.pointlist[-4].point, self.pointlist[-3].point, self.pointlist[-2].point)
            for bt in self.pointlist[-3:]:
                bt.show()
            self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp, self.path)
        qp.end()

    def updatePath(self):
        primindexes = list(self.pointlist.index(p) for p in self.pointlist if p.isPrimary)
        i = primindexes[0]
        self.path = QPainterPath(self.pointlist[i].point)
        for i in primindexes[:-1]:
            self.path.cubicTo(self.pointlist[i+1].point, self.pointlist[i+2].point, self.pointlist[i+3].point)
        if self.isClosed:
            self.path.cubicTo(self.pointlist[-1].point, self.pointlist[0].point, self.pointlist[1].point)

    def drawLines(self, qp, path):
        qp.setPen(Qt.gray)
        prev = self.pointlist[0]
        for curpoint in self.pointlist[1:]:
            if prev.isPrimary ^ curpoint.isPrimary:
                qp.drawLine(prev.point, curpoint.point)
            prev = curpoint
        self.updatePath()
        qp.setPen(Qt.red)
        qp.drawPath(path)

    def addPoint(self, p):
        self.pointlist.append(p)
        self.pointlist[-1].update()
        self.lvPoints.addItem('point ' + str(len(self.pointlist) - 1) + ': ' + p.role)

    def closeOpenCurve(self):
        self.isClosed ^= True
        self.btClosecurve.setText(self.btclosetexts[int(self.isClosed)])
        self.updatePath()
        self.update()
