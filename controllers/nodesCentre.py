import pyqtgraph as pg
from PySide2 import QtCore
class NodesCentreController(QtCore.QObject):
    __mainWindow = None
    def __init__(self, mainWindow) -> None:
        super().__init__()
        self.__mainWindow = mainWindow
        self.net_curve_pen = pg.mkPen(width=1, color='r')
        self.rt_curve_pen = pg.mkPen(width=1, color='g')
        self.createNodesPlot()

    def createNodesPlot(self):
        self.nodes_plot = pg.PlotWidget(title="Nodos conectados")
        self.nodes_plot.showGrid(x=False, y=True)
        self.nodes_plot.enableAutoRange('x', True)
        self.nodes_plot.setMouseEnabled(x=False, y=True)
        self.nodes_plot.setYRange(0, 30)
        self.nodes_plot.setLabel('left', "Nodos")
        self.nodes_plot.setLabel('bottom', "Tiempo", units='s')
        self.net_nodes_curve = self.nodes_plot.plot(pen=self.net_curve_pen, skipFiniteCheck=True)
        self.rt_nodes_curve = self.nodes_plot.plot(pen=self.rt_curve_pen, skipFiniteCheck=True)
        self.__mainWindow.ui.nodes_graphic_layout.addWidget(self.nodes_plot)