from PyQt4 import QtGui, QtCore  
import pyqtgraph as pg
from TaskGraph import TaskGraphWidget
from SemaphoreGraph import SemaphoreWidget
from EventLog import EventLogWidget
from StateHandler import StateHandler

app = QtGui.QApplication([])
pg.setConfigOptions(antialias=True)

w = QtGui.QWidget()

layout = QtGui.QHBoxLayout()
stateHandler = StateHandler()

taskWidget = TaskGraphWidget(stateHandler)
semaphoreWidget = SemaphoreWidget(stateHandler)
listwidget = EventLogWidget(stateHandler)

layout.addWidget(taskWidget)
layout.addWidget(semaphoreWidget)
layout.addLayout(listwidget)   

layout.setStretch(0,4)
layout.setStretch(1,3)
layout.setStretch(2,2)

w.setLayout(layout)


w.show()
app.exec_()
