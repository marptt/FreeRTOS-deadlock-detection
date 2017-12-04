import pyqtgraph as pg
import numpy as np

BLUE = (0, 0, 100, 255)
RED = (100,0,0, 255)

brush=pg.mkBrush(color=(200, 10, 0,1))

brush = (30, 100, 2, 255)

class GraphNodes(pg.GraphItem):
    def __init__(self, x_offset, y_offset):
        self.x_offset = x_offset
        self.y_offset = y_offset
        
        self.setCurrentState('Ready')
        self.dragPoint = None
        self.dragOffset = None
        self.textItems = []
        pg.GraphItem.__init__(self)

        self.scatter.setData(pxMode=False)
        self.scatter.addPoints([
            {
                'pos': (self.nodes[key]['x'] + x_offset, self.nodes[key]['y'] + y_offset),
                'size': 3,
                'brush': BLUE,
                'symbol': 'o'
            } for key in self.nodes 
        ])

      #  self.setTexts( ["Running","Suspended","Ready","Blocked"])
        
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

class GraphArrows():
    def __init__(self, x, y):
        self.arrowItemList = []
        self.arrowItemList.append(self.makeArrow(0,0, 0, 10))
        
    def makeArrow(self, x0, x1, y0, y1):
        if x0 == x1:
            angle = - 90*np.sign(y1-y0)
        else:
            angle = np.degrees(np.arctan((y1-y0)/(x1-x0))) 
        if np.sign(x1-x0) == 1:
            angle = angle + 180
            
        length = np.sqrt(np.power(y1-y0, 2) + np.power(x1-x0, 2)) 

        arrow = pg.ArrowItem(
            angle=angle,
            tipAngle=30,
            baseAngle=0,
            headLen=1,
            tailLen=length-1,
            tailWidth=0.3,
            pen=None,
            brush='w',
            pos=(x1,y1),
            pxMode = False
        )
        text = pg.TextItem(
            text = "some sort of event",
            border='w',
            fill=(0, 0, 255, 100),
            angle=angle+180,
            anchor=(-0.1,1.2)
        )

        return [text,arrow]
            
class TaskGraphWidget(pg.GraphicsView):
    def __init__(self, stateHandler):
        self.viewbox = pg.ViewBox()

        
        self.viewbox.setAspectLocked(1.0)
        self.viewbox.setMouseEnabled(False, False)
        
        pg.GraphicsView.__init__(self)
        self.addItem(self.viewbox)
        self.setCentralWidget(self.viewbox)
       
        self.stateHandler = stateHandler
        self.stateHandler.subscribeToCurrentState(self.onStateChange)

    def onStateChange(self, state):
        print('TaskGraph: new state '+str(state))
        print(state.event)
        self.viewbox.clear()

        gridwidth = np.around(np.sqrt(len(state.tasks)))
        i = 0
        
        for task in state.tasks:
              y = (i % gridwidth ) * -35
              x = (i // gridwidth) * 30
              i = i + 1 
              nodes = GraphNodes(x,y)
              title = pg.TextItem(
                    text = task.name,
                    border='w',
                    fill=(0, 0, 255, 100),
                    anchor=(0,1)
                    )

              
              title.setPos(x+3, y+10)
              self.viewbox.addItem(title)
              self.viewbox.addItem(nodes)            
              
        arrows = GraphArrows(0,0)
        for bunch in arrows.arrowItemList:
            for item in bunch:
                self.viewbox.addItem(item)




