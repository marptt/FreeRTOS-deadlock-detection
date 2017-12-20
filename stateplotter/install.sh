#!/bin/bash         
sudo apt-get install python-qt4

git clone https://github.com/pyqtgraph/pyqtgraph.git
cd pyqtgraph
sudo python setup.py install

pip install numpy 

sudo easy_install networkx
sudo apt-get install python-matplotlib
