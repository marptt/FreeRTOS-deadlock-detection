import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import copy

visibleItems = 100

class EventItem(QtGui.QListWidgetItem):
    def __init__(self, index, stateSnapshot):
        QtGui.QListWidgetItem.__init__(self, str(index) + ":" +stateSnapshot.event)
        self.index = index
        self.stateSnapshot = stateSnapshot
        
class EventLog(QtGui.QListWidget):
    def __init__(self, stateHandler):
        self.stateHandler = stateHandler
        pg.QtGui.QListWidget.__init__(self)
        
        self.currentItemChanged.connect(self.clicked)
        self.stateHandler.subscribeToStates(self.onStatesChange)
        self.events = []
        
    def clicked(self, item):
        index = item.index
        self.stateHandler.emitCurrentStateChange(index)

        for i in range(self.topItem, self.bottomItem):
            self.setItemHidden(self.events[i], True)
        
        if index > visibleItems:
            self.topItem = index - (visibleItems/2)
        else:
            self.topItem = 0
        self.bottomItem = index + (visibleItems/2)

        for i in range(self.topItem, self.bottomItem):
            self.setItemHidden(self.events[i], False)        
        
    def onStatesChange(self, stateSnapshots):
        i = 0
        for stateSnapshot in stateSnapshots:
            event = EventItem(i, stateSnapshot)
            self.addItem(event)
            self.events.append(event)
            self.setItemHidden(event, True)
            i = i + 1
        
        self.topItem = 0
        self.bottomItem = visibleItems
        for i in range(self.topItem, self.bottomItem):
            self.setItemHidden(self.events[i], False)

            
