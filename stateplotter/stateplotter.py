#! /usr/bin/env python
import sys

from PyQt4.QtGui import *

import pyqtgraph as pg

app = QApplication(sys.argv)
 
window = QWidget()
window.resize(320, 240)
window.setWindowTitle("stateplotter")
window.show()

sys.exit(app.exec_())


