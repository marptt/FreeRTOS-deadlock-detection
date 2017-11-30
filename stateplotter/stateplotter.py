from PyQt4 import QtGui, QtCore  
import pyqtgraph as pg
from TaskGraph import TaskGraph, makeTaskGraph
from EventLog import EventLog

app = QtGui.QApplication([])
pg.setConfigOptions(antialias=True)

w = QtGui.QWidget()

layout = QtGui.QHBoxLayout()
    
graph = makeTaskGraph()
graph.setOffset(0,0)
tasks_vb = pg.ViewBox()
tasks_vb.addItem(graph)
tasks_vb.setAspectLocked(1.0)
tasks_vb.setMouseEnabled(False, False)

tasks_v = pg.GraphicsView()
tasks_v.addItem(tasks_vb)
tasks_v.setCentralWidget(tasks_vb)



graph2 = makeTaskGraph()
graph2.setOffset(0,0)
tasks_vb2 = pg.ViewBox()
tasks_vb2.addItem(graph2)
tasks_vb2.setAspectLocked(1.0)
tasks_vb2.setMouseEnabled(False, False)

tasks_v2 = pg.GraphicsView()
tasks_v2.addItem(tasks_vb2)
tasks_v2.setCentralWidget(tasks_vb2)

listwidget = EventLog()

layout.addWidget(tasks_v)
layout.addWidget(tasks_v2) 
layout.addWidget(listwidget)   

layout.setStretch(0,3)
layout.setStretch(1,3)
layout.setStretch(2,1)

w.setLayout(layout)


w.show()
app.exec_()

