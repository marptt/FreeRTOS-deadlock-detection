from PyQt4 import QtGui, QtCore  
import pyqtgraph as pg
from TaskGraph import TaskGraphWidget
from SemaphoreGraph import SemaphoreWidget
from EventLog import EventLog
from StateHandler import StateHandler

app = QtGui.QApplication([])
pg.setConfigOptions(antialias=True)

w = QtGui.QWidget()

layout = QtGui.QHBoxLayout()
stateHandler = StateHandler()

taskWidget = TaskGraphWidget(stateHandler)
semaphoreWidget = SemaphoreWidget(stateHandler)
listwidget = EventLog(stateHandler)

layout.addWidget(taskWidget)
layout.addWidget(semaphoreWidget) 
layout.addWidget(listwidget)   

layout.setStretch(0,3)
layout.setStretch(1,3)
layout.setStretch(2,1)

w.setLayout(layout)

stateHandler.testStates()


w.show()
app.exec_()
