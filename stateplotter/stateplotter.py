# -*- coding: utf-8 -*-

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

from TaskGraph import TaskGraph, makeTaskGraph
from Grid import Grid
app = QtGui.QApplication([])

grid=Grid()
pg.setConfigOptions(antialias=True)

tasks_vb = pg.ViewBox()
grid.tasks_widget.addItem(tasks_vb)
tasks_vb.setAspectLocked(1.0)
tasks_vb.setMouseEnabled(False, False)

semphs_vb = pg.ViewBox()
grid.semphs_widget.addItem(semphs_vb)

graph = makeTaskGraph()
graph.setOffset(0,0)

graph2 = makeTaskGraph()
graph2.setOffset(0,40)

graph3 = makeTaskGraph()
graph3.setOffset(30,40)

tasks_vb.addItem(graph3)
tasks_vb.addItem(graph2)
tasks_vb.addItem(graph)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
