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
taskGraph = taskWidget.graph
taskGraph.setOffset(0,0)
tasks_vb = pg.ViewBox()
tasks_vb.addItem(taskGraph)
tasks_vb.setAspectLocked(1.0)
tasks_vb.setMouseEnabled(False, False)


tasks_v = pg.GraphicsView()
tasks_v.addItem(tasks_vb)
tasks_v.setCentralWidget(tasks_vb)


tasks_vb2 = pg.ViewBox()
tasks_v2 = pg.GraphicsView()
tasks_v2.setCentralWidget(tasks_vb2)


listwidget = EventLog(stateHandler)


layout.addWidget(tasks_v)
layout.addWidget(tasks_v2) 
layout.addWidget(listwidget)   

layout.setStretch(0,3)
layout.setStretch(1,3)
layout.setStretch(2,1)

w.setLayout(layout)

# connect up subscribers
# TODO MOVE
# stateHandler.subscribeToCurrentState(taskGraph.onStateChange)
# stateHandler.subscribeToCurrentState(placeholderGraph.onStateChange)
# stateHandler.subscribeToState(eventLog.onStateChange) maybe not needed
stateHandler.testStates()


w.show()
app.exec_()

