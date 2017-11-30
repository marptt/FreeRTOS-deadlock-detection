import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

log = """
0, semaphore give
0, switched out Tmr Svc
0, switched in PeriodicTask
0, switched out PeriodicTask
0, switched in ContinuousTask1
0, semaphore take
0, switched out ContinuousTask1
0, switched in ContinuousTask2
0, switched out ContinuousTask2
0, switched in IDLE
1, switched out IDLE
250, switched in PeriodicTask
250, switched out PeriodicTask
250, switched in IDLE
251, switched out IDLE
"""
    
class EventItem(QtGui.QListWidgetItem):
    def __init__(self, index):
        QtGui.QListWidgetItem.__init__(self, 'event '+str(index))
        self.index = index
        
class EventLog(QtGui.QListWidget):
    def __init__(self):
        pg.QtGui.QListWidget.__init__(self)
        for i in range(0, 100):
            self.addItem(EventItem(i))
        
        self.currentItemChanged.connect(self.clicked)
        
    def clicked(self, item):
        print(item.index)
        

