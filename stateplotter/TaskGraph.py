import pyqtgraph as pg
import numpy as np

positions = np.array([
    [10,0],
    [0,0],
    [0,-10],
    [0,10],
    ], dtype=float)

adjacencies = np.array([
    [0,1],
    [0,2],
    [0,3],
    [1,0]
    ])

symbols = ['o','o','o','o']
sizes = [3 for i in range(0, 4)]

lines = np.array([
    (255,0,0,255,1),
    (255,0,255,255,2),
    (255,0,255,255,3),
    (255,255,0,255,2)
    ], dtype=[('red',np.ubyte),('green',np.ubyte),('blue',np.ubyte),('alpha',np.ubyte),('width',float)])


class TaskGraph(pg.GraphItem):
    def __init__(self):
        self.tasks = []
        self.dragPoint = None
        self.dragOffset = None
        self.textItems = []
        pg.GraphItem.__init__(self)
        self.setData(pos=positions, adj=adjacencies, symbol=symbols, size=sizes,  pxMode = False)
        self.scatter.sigClicked.connect(self.clicked)
        self.setTexts( ["Running","Suspended","Ready","Blocked"])
        
    def setOffset(self, x, y):
        self.pos = positions + [x,y]
        self.setData(pos=self.pos)

    def setData(self, **kwds):
        self.data = kwds
        if 'pos' in self.data:
            npts = self.data['pos'].shape[0]
            self.data['data'] = np.empty(npts, dtype=[('index', int)])
            self.data['data']['index'] = np.arange(npts)
        self.updateGraph()
        
    def setTexts(self, text):
        for i in self.textItems:
            i.scene().removeItem(i)
        self.textItems = []
        for t in text:
            item = pg.TextItem(t)
            self.textItems.append(item)
            item.setParentItem(self)
        
    def updateGraph(self):
        pg.GraphItem.setData(self, **self.data)
        for i,item in enumerate(self.textItems):
            item.setPos(*self.data['pos'][i])
        
    def clicked(self, pts):
        print("clicked: %s" % pts)
        self.brush = pg.mkColor(100,255, 100)

    def blobItem(self, x, y, color, text):
        poop
        

class TaskGraphWidget():
    def __init__(self, stateHandler):
        self.graph = TaskGraph()
        self.stateHandler = stateHandler
        self.stateHandler.subscribeToCurrentState(self.onStateChange)
        
    def onStateChange(self, state):
        print('TaskGraph: new state '+str(state))
        print(state.event)

            
        
