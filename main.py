# !/usr/bin/python3
# -*- coding: utf-8 -*-
import shits

from PyQt5.Qt import *


from CurveEditor import *



def main():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 600)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()











    ce = CurveEditor(w)

    # bt1 = QPushButton(ce)
    # bt1.setStyleSheet('''QPushButton{border-style: inset;
    #                             border-width: 1px;
    #                             border-color: black;
    #                             border-radius: 5px;
    #                             background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.4 rgba(0, 0, 0, 255), stop:0.41 rgba(255, 255, 255, 0));}
    #                             QPushButton:pressed{background-color: rgb(85, 85, 255);}''')
    # bt1.setGeometry(10, 10, 20, 20)
    # bt1.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
