#! /usr/bin/env python
import sys

# can be installed with: apt-get install python-qt4
from PyQt4.QtGui import *

app = QApplication(sys.argv)
 
window = QWidget()
window.resize(320, 240)
window.setWindowTitle("stateplotter")
window.show()

sys.exit(app.exec_())

