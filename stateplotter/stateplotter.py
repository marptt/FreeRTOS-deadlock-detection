# -*- coding: utf-8 -*-

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

from TaskGraph import TaskGraph
from Grid import Grid
app = QtGui.QApplication([])

grid=Grid()
# layout = grid.layout
# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

# window = pg.GraphicsWindow()
# window.setWindowTitle('stateplotter')
# view = window.addViewBox()
# view.setAspectLocked()

#graph = TaskGraph()
# view.addItem(graph)

## Define positions of nodes
pos = np.array([
    [10,0],
    [0,0],
    [0,-10],
    [0,10],
    ], dtype=float)
    
## Define the set of connections in the graph
adj = np.array([
    [0,1],
    [0,2],
    [0,3],
    [1,0]
    ])

## Define the symbol to use for each node (this is optional)
symbols = ['o','o','o','o']

## Define the line style for each connection (this is optional)
lines = np.array([
    (255,0,0,255,1),
    (255,0,255,255,2),
    (255,0,255,255,3),
    (255,255,0,255,2)
    ], dtype=[('red',np.ubyte),('green',np.ubyte),('blue',np.ubyte),('alpha',np.ubyte),('width',float)])


texts = ["Running","Suspended","Ready","Blocked"]
## Update the graph
#graph.setData(pos=pos, adj=adj, pen=lines, size=1, symbol=symbols, pxMode=False, text=texts)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
