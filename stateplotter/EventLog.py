import pyqtgraph as pg
from PyQt4 import QtGui, QtCore  
import numpy as np
import copy

class EventItem(QtGui.QListWidgetItem):
    def __init__(self, index, stateSnapshot):
        QtGui.QListWidgetItem.__init__(self, str(index) + ":" +stateSnapshot.event)
        self.index = index
        if stateSnapshot.isDeadlocked:
            self.setForeground(QtGui.QBrush( QtGui.QColor(255,0,0)))
        self.stateSnapshot = stateSnapshot
        
class EventLog(QtGui.QListWidget):
    def __init__(self, stateHandler):
        self.stateHandler = stateHandler
        pg.QtGui.QListWidget.__init__(self)
        
        self.currentItemChanged.connect(self.clicked)
        self.stateHandler.subscribeToStates(self.onStatesChange)
        self.events = []
        self.visibleItems = 100

    def clicked(self, item):
        index = item.index
        self.stateHandler.emitCurrentStateChange(index)
        
    def nextClicked(self, b):
        if not self.events:
            return
        if self.bottomItem > len(self.events):
            return
        
        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], True)        

        self.topItem += self.visibleItems
        self.bottomItem = self.topItem + self.visibleItems

        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], False)        

    def previousClicked(self, b):
        if not self.events:
            return
        if(self.topItem == 0):
            return
        
        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], True)        

        self.topItem -= self.visibleItems
        self.bottomItem = self.topItem + self.visibleItems

        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], False)        

    def visibleItemsChanged(self, n):
        if not self.events:
            return
        
        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], True)        

        self.visibleItems = n
        self.topItem = 0
        self.bottomItem = self.topItem + self.visibleItems

        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], False)    

    def loadFileByButton(self, b):
        self.stateHandler.stateFromFile(self.textbox.text())

    def loadFileByReturn(self):
        self.stateHandler.stateFromFile(self.textbox.text())
        
        
    def onStatesChange(self, stateSnapshots):
        i = 0
        self.clear()
        self.events = []
        for stateSnapshot in stateSnapshots:
            event = EventItem(i, stateSnapshot)
            self.addItem(event)
            self.events.append(event)
            self.setItemHidden(event, True)
            i = i + 1
        
        self.topItem = 0
        self.bottomItem = self.visibleItems
        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], False)
                    
class EventLogWidget(QtGui.QVBoxLayout):
    def __init__(self, stateHandler):
        eventLog = EventLog(stateHandler)
            
        previousButton = QtGui.QPushButton("previous")
        nextButton = QtGui.QPushButton("next")
        nextButton.clicked.connect(eventLog.nextClicked)
        previousButton.clicked.connect(eventLog.previousClicked)

        linesInput = QtGui.QSpinBox()
        linesInput.valueChanged.connect(eventLog.visibleItemsChanged)
        linesInput.setValue(eventLog.visibleItems)
        linesInput.setMaximum(10000)
        hbox0 = QtGui.QHBoxLayout()
        hbox0.addWidget(previousButton)
        hbox0.addWidget(nextButton)
        hbox0.addWidget(linesInput)
        
        loadButton = QtGui.QPushButton("load file")
        loadButton.clicked.connect(eventLog.loadFileByButton)
        textbox = QtGui.QLineEdit()
        textbox.returnPressed.connect(eventLog.loadFileByReturn)
        eventLog.textbox = textbox
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(loadButton)
        hbox1.addWidget(textbox)
        
        vbox = QtGui.QVBoxLayout()

        vbox.addWidget(eventLog)        
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        
        QtGui.QVBoxLayout.__init__(self)
        self.addLayout(vbox)
