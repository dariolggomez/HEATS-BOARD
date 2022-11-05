import pyqtgraph as pg
from PySide2 import QtCore
from time import time
from collections import deque
class NodesCentreController(QtCore.QObject):
    __mainWindow = None
    def __init__(self, mainWindow) -> None:
        super().__init__()
        self.__mainWindow = mainWindow
        self.net_connected = 0
        self.net_curve_pen = pg.mkPen(width=1, color='r')
        self.rt_curve_pen = pg.mkPen(width=1, color='g')
        self.last_time = 0.0
        self.t_end = 0.0
        self.ptr = 0
        self.connected_net_data = deque(maxlen= 10)
        self.connected_rt_data = deque(maxlen= 10)
        self.createNodesPlot()
        self.startNodesPlot()

    def createNodesPlot(self):
        self.nodes_plot = pg.PlotWidget(title="Nodos conectados")
        self.nodes_plot.showGrid(x=False, y=True)
        self.nodes_plot.enableAutoRange('x', True)
        self.nodes_plot.setMouseEnabled(x=False, y=True)
        self.nodes_plot.setYRange(0, 30)
        self.nodes_plot.setLabel('left', "Nodos")
        self.nodes_plot.setLabel('bottom', "Tiempo", units='s')
        self.nodes_plot.addLegend()
        self.net_nodes_curve = self.nodes_plot.plot(name= 'Nodos NET', pen=self.net_curve_pen, skipFiniteCheck=True)
        self.rt_nodes_curve = self.nodes_plot.plot(name= 'Nodos RT', pen=self.rt_curve_pen, skipFiniteCheck=True)
        self.__mainWindow.ui.nodes_graphic_layout.addWidget(self.nodes_plot)

    def updateNodesPlot(self):
        self.t_end = time()
        self.net_connected = 0
        self.rt_connected = 0
        
        for netNodeDict in self.__mainWindow.getNetNodesInUse():
            self.net_connected += 1
            for rtNodesDict in netNodeDict.get("rtNodesList"):
                if rtNodesDict.get("status") == 1:
                    self.rt_connected += 1
        
        self.connected_net_data.append(self.net_connected)
        self.connected_rt_data.append(self.rt_connected)
        self.ptr += (self.t_end - self.last_time)
        self.last_time = time()
        
        self.net_nodes_curve.setData(self.connected_net_data)
        self.net_nodes_curve.setPos(self.ptr, 0)
        self.rt_nodes_curve.setData(self.connected_rt_data)
        self.rt_nodes_curve.setPos(self.ptr, 0)

    def startNodesPlot(self):
        self.last_time = time()
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.updateNodesPlot)
        self.timer.start(1000)

        