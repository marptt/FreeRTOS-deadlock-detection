# from pyqtgraph.Qt import QtGui, QtCore
# import pyqtgraph as pg
# import numpy as np
# from TaskGraph import TaskGraph

# class Grid():
#     def __init__(self):
#         self.view = pg.GraphicsLayoutWidget(border=(255,255,100))
#         self.view.show()
#         self.view.setWindowTitle('State plotter')
#         self.view.resize(1920,1080)
        
#         tasks_width = 3
#         semphs_width = 3
#         events_width = 1
#         self.tasks_widget = self.view.addLayout(col=0, colspan=tasks_width)
#         self.semphs_widget = self.view.addLayout(col=tasks_width, colspan=semphs_width)
#         self.events_widget = self.view.addLayout(col=tasks_width + semphs_width, colspan=events_width)

#         self.qGraphicsGridLayout = self.view.ci.layout

#         # all columns set to width 1/cols
#         cols = tasks_width  + semphs_width + events_width

#         for i in range(0, cols):
#             self.qGraphicsGridLayout.setColumnStretchFactor(i, 1)     
            
