#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore
import RGBW_Leds

class MainWindow(QtGui.QWidget):
    
    def __init__(self):
        
        self.controller = None

        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont("ComicSans", 10))

        button = QtGui.QPushButton("Connect", self)
        button.clicked.connect(self.handleConnect)
        button.setToolTip("Starts the LE scan and connects to the controller")
        button.resize(button.sizeHint())
        button.move(50,50)


        qbtn = QtGui.QPushButton("Quit", self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)
        
        offbtn = QtGui.QPushButton("Off", self)
        offbtn.clicked.connect(self.handleOff)
        offbtn.resize(offbtn.sizeHint())
        offbtn.move(200, 50)
        
        onbtn = QtGui.QPushButton("On", self)
        onbtn.clicked.connect(self.handleOn)
        onbtn.resize(onbtn.sizeHint())
        onbtn.move(200, 100)
        
        clrbtn = QtGui.QPushButton("Colour", self)
        clrbtn.clicked.connect(self.colourPicker)
        clrbtn.resize(clrbtn.sizeHint())
        clrbtn.move(200, 150)

        self.resize(500, 300)
        self.center()
        self.setWindowTitle("LED GUI WIP")

        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handleConnect(self):
        self.controller = RGBW_Leds.ScanConnect(3)

    def handleOff(self):
        self.controller.setColour(0)

    def handleOn(self):
        self.controller.setColour(0xFFFFFFFF)

    def colourPicker(self):
        colour = QtGui.QColorDialog.getColor()
        newColour = colour.red()
        newColour |= (colour.green() << 8)
        newColour |= (colour.blue() << 16)
        self.controller.setColour(newColour & 0x00FFFFFF)


def main():

    app = QtGui.QApplication(sys.argv)
    asd = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
