import pyqtgraph as pg
from PyQt4 import QtGui, QtCore  
import numpy as np
import copy


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
        self.visibleItems = 20

    def clicked(self, item):
        index = item.index
        self.stateHandler.emitCurrentStateChange(index)
        
    def nextClicked(self, b):
        if(self.bottomItem > len(self.events)):
            return
        
        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], True)        

        self.topItem += self.visibleItems
        self.bottomItem += self.visibleItems

        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], False)        

    def previousClicked(self, b):
        if(self.topItem == 0):
            return
        
        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], True)        

        self.topItem -= self.visibleItems
        self.bottomItem -= self.visibleItems

        for i in range(self.topItem, min(self.bottomItem, len(self.events))):
            self.setItemHidden(self.events[i], False)        

    def visibleItemsChanged(self, n):
        self.visibleItems = n

    def loadFile(self, b):
        print(self.textbox.text())
        self.stateHandler.stateFromFile(self.textbox.text())
        # TODO handle io exception
        
    def onStatesChange(self, stateSnapshots):
        i = 0
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
            
        nextButton = QtGui.QPushButton("next")
        previousButton = QtGui.QPushButton("previous")
        nextButton.clicked.connect(eventLog.nextClicked)
        previousButton.clicked.connect(eventLog.previousClicked)

        linesInput = QtGui.QSpinBox()
        linesInput.valueChanged.connect(eventLog.visibleItemsChanged)
        linesInput.setValue(eventLog.visibleItems)
        
        hbox0 = QtGui.QHBoxLayout()
        hbox0.addStretch(1)
        hbox0.addWidget(nextButton)
        hbox0.addWidget(previousButton)
        hbox0.addWidget(linesInput)

        loadButton = QtGui.QPushButton("load file")
        loadButton.clicked.connect(eventLog.loadFile)
        textbox = QtGui.QLineEdit()
        eventLog.textbox = textbox
        textbox.move(20, 20)
        textbox.resize(280,40)
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(loadButton)
        hbox1.addWidget(textbox)
        
        vbox = QtGui.QVBoxLayout()

        vbox.addWidget(eventLog)        
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        
        QtGui.QVBoxLayout.__init__(self)
        self.addLayout(vbox)
