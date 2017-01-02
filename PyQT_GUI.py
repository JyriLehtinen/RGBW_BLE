#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QWidget):
    
    def __init__(self):
        
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont("ComicSans", 10))

        button = QtGui.QPushButton("Connect", self)
        button.setToolTip("Starts the LE scan and connects to the controller")
        button.resize(button.sizeHint())
        button.move(50,50)


        qbtn = QtGui.QPushButton("Quit", self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)

        self.setGeometry(150, 50, 500, 300)
        self.setWindowTitle("LED GUI WIP")

        self.show()
        

def main():

    app = QtGui.QApplication(sys.argv)
    asd = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
