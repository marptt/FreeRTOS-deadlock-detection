import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

class EventItem(QtGui.QListWidgetItem):
    def __init__(self, index, stateSnapshot):
        QtGui.QListWidgetItem.__init__(self, stateSnapshot.event)
        self.index = index
        self.stateSnapshot = stateSnapshot
        
class EventLog(QtGui.QListWidget):
    def __init__(self, stateHandler):
        self.stateHandler = stateHandler
        pg.QtGui.QListWidget.__init__(self)
        
        self.currentItemChanged.connect(self.clicked)
        self.stateHandler.subscribeToStates(self.onStatesChange)
        
    def clicked(self, item):
        self.stateHandler.emitCurrentStateChange(item.index)
        
    def onStatesChange(self, stateSnapshots):
        i = 0
        for stateSnapshot in stateSnapshots:
            self.addItem(EventItem(i, stateSnapshot))
            i = i + 1
