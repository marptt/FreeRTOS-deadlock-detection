from PyQt4 import QtGui, QtCore  
import pyqtgraph as pg
import numpy as np


NODE_RADIUS = 3

class GraphNodes(pg.GraphItem):
    def __init__(self):
        pg.GraphItem.__init__(self)
        self.scatter.setData(pxMode=False)

    def addPoints(self, points):
        self.scatter.clear()
        self.scatter.addPoints(points)


def makeArrow(x0, x1, y0, y1):
    if x0 == x1:
        angle = - 90*np.sign(y1-y0)
    else:
        angle = np.degrees(np.arctan((y1-y0)/(x1-x0))) 
    if np.sign(x1-x0) == 1:
        angle = angle + 180
        
    length = np.sqrt(np.power(y1-y0, 2) + np.power(x1-x0, 2))
         
    arrow = pg.ArrowItem(
        angle=angle,
        tipAngle=40,
        baseAngle=0,
        headLen=2,
        tailLen=length-2,
        tailWidth=0.3,
        pen=None,
        brush='w',
        pos=(x1,y1),
        pxMode = False
    )
    return arrow

        
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

    def makeLabel(self, text, x, y, xjustify, angle):
        t = pg.TextItem(
            text,
            anchor=(xjustify,0.5),
            angle=angle
            )
        t.setPos(x, y)
        return t
        
    def onStateChange(self, state):
        self.viewBox.clear()
        nodes = GraphNodes()
        self.viewBox.addItem(nodes)   
        points = []

        semaphore_count = len(state.semaphores)
        task_count = len(state.tasks)
        default_distance = 10
        if semaphore_count < task_count:
            task_spacing = 10
            if (semaphore_count -1) == 0:
                semph_spacing = 0
            else:
                semph_spacing = 10 * (task_count - 1) / (semaphore_count -1)
        else: 
            semph_spacing = 10
            if  (task_count -1) == 0:
                task_spacing = 0
            else:
                task_spacing = 10 * (semaphore_count - 1) / (task_count -1)
       
        i = 0
        for semph in state.semaphores:
            points.append({
                'pos': (0, i),
                'size': NODE_RADIUS * 2,
                'brush': (255,0,0),
                'symbol': 'd',
            })
            self.viewBox.addItem(self.makeLabel(semph, -NODE_RADIUS, i, 1,0))
            i = i + semph_spacing

        i = 0        
        for task in state.tasks:
            
            points.append({
                'pos': (30, i),
                'size': NODE_RADIUS * 2,
                'brush': (255,0,0),
                'symbol': 's',
            })
            self.viewBox.addItem(self.makeLabel(task.taskName, 30+NODE_RADIUS, i, 0, 0))
            
            for held_semph in task.heldSemaphores:
                
                semph_index = state.semaphores.index( str(held_semph))
                self.viewBox.addItem(makeArrow(
                    30.0,
                    0.0,
                    i,
                    semph_index * semph_spacing                    
                ))

            for request_semph in task.requestedSemaphores:
                semph_index = state.semaphores.index(str(request_semph))
                self.viewBox.addItem(makeArrow(
                    0.0,
                    30.0,
                    semph_index * semph_spacing,
                    i                    
                ))
            
            i = i + task_spacing
        nodes.addPoints(points)
        
      
        
                 
