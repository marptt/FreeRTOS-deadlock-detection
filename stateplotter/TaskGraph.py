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
    (255,0,0,  255,1),
    (255,0,255,255,2),
    (255,0,255,255,3),
    (255,255,0,255,2)
    ], dtype=[('red',np.ubyte),('green',np.ubyte),('blue',np.ubyte),('alpha',np.ubyte),('width',float)])

BLUE = (0, 0, 100, 255)
RED = (100,0,0, 255)

brush=pg.mkBrush(color=(200, 10, 0,1))

brush = (30, 100, 2, 255)

class TaskGraph(pg.GraphItem):    
    def __init__(self, x_offset, y_offset):
        self.x_offset = x_offset
        self.y_offset = y_offset
        
        self.setCurrentState('Ready')
        self.dragPoint = None
        self.dragOffset = None
        self.textItems = []
        pg.GraphItem.__init__(self)
        # self.setData(pos=positions, adj=adjacencies, symbol=symbols, size=sizes,  pxMode = False,symbolBrush = brush)
        # self.setData(adj=adjacencies, symbol=symbols, size=sizes,  pxMode = False,symbolBrush = brush)

        self.scatter.addPoints([
            {
                'pos': (self.nodes[key]['x'] + x_offset, self.nodes[key]['y'] + y_offset),
                'size': 100,
                'brush': BLUE
            } for key in self.nodes 
        ])

        self.setTexts( ["Running","Suspended","Ready","Blocked"])
        
    def setCurrentState(self, state):
        self.nodes = {}
        self.nodes['Running'] =   {'x': 10,'y': 0,  'color': BLUE} 
        self.nodes['Suspended'] = {'x': 0, 'y': 0,  'color': BLUE} 
        self.nodes['Ready'] =     {'x': 0, 'y': -10,'color': BLUE}
        self.nodes['Blocked'] =   {'x': 0, 'y': 10, 'color': BLUE}
        
        self.nodes[state]['color'] = RED
       
        for key in self.nodes:
            node = self.nodes[key]            

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
         
class TaskGraphWidget(pg.GraphicsView):
    def __init__(self, stateHandler):
        
        #tasks_vb.addItem(pg.ArrowItem(angle=-120, tipAngle=30, baseAngle=20, headLen=40, tailLen=40, tailWidth=8, pen=None, brush='y'))

        graph = TaskGraph(0,0)
        #taskGraph = taskWidget.graph
        tasks_vb = pg.ViewBox()
        tasks_vb.addItem(graph)
        tasks_vb.setAspectLocked(1.0)
        tasks_vb.setMouseEnabled(False, False)
        
        pg.GraphicsView.__init__(self)
        self.addItem(tasks_vb)
        self.setCentralWidget(tasks_vb)

        self.stateHandler = stateHandler
        self.stateHandler.subscribeToCurrentState(self.onStateChange)
        
    def onStateChange(self, state):
        print('TaskGraph: new state '+str(state))
        print(state.event)

            
        



