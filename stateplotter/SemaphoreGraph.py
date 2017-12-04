from PyQt4 import QtGui, QtCore  
import pyqtgraph as pg


NODE_RADIUS = 3

class GraphNodes(pg.GraphItem):
    def __init__(self):
        pg.GraphItem.__init__(self)
        self.scatter.setData(pxMode=False)

    def addPoints(self, points):
        self.scatter.clear()
        self.scatter.addPoints(points)

class GraphArrows():
    def __init__(self, x0, x1, y0, y1):
        self.arrowItemList = []
        self.arrowItemList.append(self.makeArrow(x0, x1, y0, y1))
        
    def makeArrow(self, x0, x1, y0, y1):
        if x0 == x1:
            angle = - 90*np.sign(y1-y0)
        else:
            angle = np.degrees(np.arctan((y1-y0)/(x1-x0))) 
        if np.sign(x1-x0) == 1:
            angle = angle + 180
            
        length = np.sqrt(np.power(y1-y0, 2) + np.power(x1-x0, 2)) - NODE_RADIUS * 2
        arrowTarget = (x1+np.cos(angle)*NODE_RADIUS,y1+np.sin(angle)*NODE_RADIUS)
             
        arrow = pg.ArrowItem(
            angle=angle,
            tipAngle=30,
            baseAngle=0,
            headLen=1,
            tailLen=length-1,
            tailWidth=0.3,
            pen=None,
            brush='w',
            pos=arrowTarget,
            pxMode = False
        )
        return [arrow]
        
class SemaphoreWidget(pg.GraphicsView):
    def __init__(self, stateHandler):
        self.viewBox = pg.ViewBox()
        
        self.viewBox.setAspectLocked(1.0)
        self.viewBox.setMouseEnabled(False, False)
        
        pg.GraphicsView.__init__(self)
        self.addItem(self.viewBox)
        self.setCentralWidget(self.viewBox)
       
        self.stateHandler = stateHandler
        self.stateHandler.subscribeToCurrentState(self.onStateChange)

    def makeLabel(self, text, x, y, angle):
        t = pg.TextItem(
            text,
            anchor=(1,0.5),
            angle=angle
            )
        t.setPos(x, y)
        return t
        
    def onStateChange(self, state):
        self.viewBox.clear()
        nodes = GraphNodes()
        self.viewBox.addItem(nodes)   
        points = []
        
        i = 0
        for semph in state.semaphores:
            i = i + 10
            points.append({
                'pos': (0, i),
                'size': NODE_RADIUS * 2,
                'brush': (255,0,0),
                'symbol': 'd',
            })

        i = 0
        for semph in state.semaphores:
            i = i + 10
            self.viewBox.addItem(self.makeLabel(semph, -NODE_RADIUS, i, 0))
        
        i = 0        
        for task in state.tasks:
            i = i + 10
            points.append({
                'pos': (30, i),
                'size': NODE_RADIUS * 2,
                'brush': (255,0,0),
                'symbol': 's',
            })

        nodes.addPoints(points)


        # arrows = GraphArrows()
        
