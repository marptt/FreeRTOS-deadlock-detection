from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np

class Grid():
    def __init__(self):
        self.view = pg.GraphicsLayoutWidget(border=(255,255,100))
        self.view.show()
        self.view.setWindowTitle('State plotter')
        self.view.resize(1920,1080)

        self.l2 = self.view.addLayout(row=0, col=0, colspan=4)
        self.l3 = self.view.addLayout(row=0, col=2, colspan=6)
        self.qGraphicsGridLayout = self.view.ci.layout

        # all columns set to width 1/cols
        cols = 8
        for i in range(0, cols):
            self.qGraphicsGridLayout.setColumnStretchFactor(i, 1)     
