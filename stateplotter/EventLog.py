import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

class EventItem(QtGui.QListWidgetItem):
    def __init__(self, index, item):
        QtGui.QListWidgetItem.__init__(self, item.name + ' in state ' + str(item.taskState))
        self.index = index
        self.item = item
        
class EventLog(QtGui.QListWidget):
    def __init__(self, stateHandler):
        self.stateHandler = stateHandler
        pg.QtGui.QListWidget.__init__(self)
        
        self.currentItemChanged.connect(self.clicked)
        self.stateHandler.subscribeToStates(self.onStatesChange)
        
    def clicked(self, item):
        self.stateHandler.emitCurrentStateChange(item.index)
        
    def onStatesChange(self, states):
        for state in states:
            self.addItem(EventItem(0, state))
         

