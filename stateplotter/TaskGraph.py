import pyqtgraph as pg
import numpy as np


BLUE = (0, 0, 100, 255)
RED = (100,0,0, 255)

TASK_BLOCKED   = 'Running'    
TASK_SUSPENDED = 'Suspended' 
TASK_RUNNING   = 'Ready'
TASK_READY     = 'Blocked'   

NODE_RADIUS = 3

class GraphNodes(pg.GraphItem):
    def __init__(self, x_offset, y_offset):
        self.x_offset = x_offset
        self.y_offset = y_offset
        pg.GraphItem.__init__(self)
        self.scatter.setData(pxMode=False)
                
    def setCurrentState(self, state):
        self.nodes = {}
        self.nodes['Running'] =   {'x': 10,'y': 0,  'color': BLUE} 
        self.nodes['Suspended'] = {'x': 0, 'y': 0,  'color': BLUE} 
        self.nodes['Ready'] =     {'x': 0, 'y': -10,'color': BLUE}
        self.nodes['Blocked'] =   {'x': 0, 'y': 10, 'color': BLUE}

        self.nodes[state]['color'] = RED
        for key in self.nodes:
            node = self.nodes[key]

        self.scatter.clear()
        self.scatter.addPoints([
            {
                'pos': (self.nodes[key]['x'] + self.x_offset, self.nodes[key]['y'] + self.y_offset),
                'size': NODE_RADIUS * 2,
                'brush': self.nodes[key]['color'],
                'symbol': 'o',
            } for key in self.nodes 
        ])

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
            
        length = np.sqrt(np.power(y1-y0, 2) + np.power(x1-x0, 2))
             
        arrow = pg.ArrowItem(
            angle=angle,
            tipAngle=40,
            baseAngle=0,
            headLen=2,
            tailLen=length-1,
            tailWidth=0.3,
            pen=None,
            brush='w',
            pos=(x1,y1),
            pxMode = False
        )
        return [arrow]
            
class TaskGraphWidget(pg.GraphicsView):
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

        # text boxes scale much better like this
        gridheight = 10000#np.around(np.sqrt(len(state.tasks)))
        i = 0
        
        for task in state.tasks:            
              y = (i % gridheight ) * -35
              x = (i // gridheight) *  30
              i = i + 1 
              nodes = GraphNodes(x,y)
              nodes.setCurrentState(task.currentState)
              title = pg.TextItem(
                  text = "Task:"+task.taskName +"\n" +
                         "Event:" + task.eventName +"\n" +
                         "Priority:" + "TODO",
                  border='w',
                  fill=(0, 0, 0, 100),
                  anchor=(0,0.5),
                  angle = 0
                  )
              title.setPos(x+NODE_RADIUS*2+10, y)

              self.viewBox.addItem(nodes)            
              
              labels = [
                   self.makeLabel("Running",   x+10 , y+NODE_RADIUS,-90), 
                   self.makeLabel("Suspended", x - NODE_RADIUS,    y,0), 
                   self.makeLabel("Ready",     x - NODE_RADIUS,    y-10,0), 
                   self.makeLabel("Blocked",   x - NODE_RADIUS,    y+10, 0) 
              ]

              for label in labels:
                  self.viewBox.addItem(label)
              self.viewBox.addItem(title)

            
              
              source = nodes.nodes[task.previousState]
              target = nodes.nodes[task.currentState]

              debugArrows = True
              if task.enableArrow or debugArrows:
                  arrows = GraphArrows(
                      source['x'] + x,
                      target['x'] + x,
                      source['y'] + y,
                      target['y'] + y
                      )
                  for bunch in arrows.arrowItemList:
                      for item in bunch:
                          self.viewBox.addItem(item)
