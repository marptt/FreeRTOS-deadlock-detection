from PyQt4 import QtGui, QtCore  
import pyqtgraph as pg
from TaskGraph import TaskGraphWidget
from EventLog import EventLog
from StateHandler import StateHandler
app = QtGui.QApplication([])
pg.setConfigOptions(antialias=True)

w = QtGui.QWidget()

layout = QtGui.QHBoxLayout()

stateHandler = StateHandler()

taskWidget = TaskGraphWidget(stateHandler)

tasks_vb2 = pg.ViewBox()
tasks_v2 = pg.GraphicsView()
tasks_v2.setCentralWidget(tasks_vb2)

listwidget = EventLog(stateHandler)

layout.addWidget(taskWidget)
layout.addWidget(tasks_v2) 
layout.addWidget(listwidget)   

layout.setStretch(0,3)
layout.setStretch(1,3)
layout.setStretch(2,1)

w.setLayout(layout)

stateHandler.testStates()


w.show()
app.exec_()

