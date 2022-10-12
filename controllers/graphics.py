from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
from time import perf_counter
from PySide2.QtCore import Slot, Qt

class GraphicsController():
    __mainWindow = None
    def __init__(self, parent) -> None:
        self.__mainWindow = parent
        self.default_pen = pg.mkPen(width=1, color='y')
        self.default_pen.setStyle(Qt.PenStyle.SolidLine)
        self.createDefinitions()
        self.createWaveformPlot()
        self.createFftPlot()
        self.create_spectrogram_graphic()

    def generatePgColormap(self, cm_name):
        """Converts a matplotlib colormap to a pyqtgraph colormap."""
        colormap = plt.get_cmap(cm_name)
        colormap._init()
        lut = (colormap._lut * 255).view(np.ndarray)  # Convert matplotlib colormap from 0-1 to 0 -255 for Qt
        return lut

    def createDefinitions(self):
        sfmt = QtGui.QSurfaceFormat()
        sfmt.setSwapInterval(0)
        QtGui.QSurfaceFormat.setDefaultFormat(sfmt)
        self.CHUNKSIZE = 1024
        self.SAMPLE_RATE = 44100
        self.TIME_VECTOR = np.arange(self.CHUNKSIZE) / self.SAMPLE_RATE
        self.N_FFT = 1024
        self.FREQ_VECTOR = np.fft.rfftfreq(self.N_FFT, d=self.TIME_VECTOR[1] - self.TIME_VECTOR[0])
        self.WATERFALL_FRAMES = int(250 * 2048 // self.N_FFT)
        self.TIMEOUT = 111
        self.fps = None
        self.EPS = 1e-8
        self.ptr = 0
        self.last_time = perf_counter()
        self.running = False
        self.first_run = True

    def createWaveformPlot(self):
        self.waveform_plot = pg.PlotWidget(title="Forma de Onda")
        self.waveform_plot.showGrid(x=False, y=True)
        self.waveform_plot.enableAutoRange('x', True)
        self.waveform_plot.setMouseEnabled(x=False, y=True)
        # waveform_plot.setXRange(TIME_VECTOR.min(), TIME_VECTOR.max())
        self.waveform_plot.setYRange(-2 ** 15, 2 ** 15 - 1)
        self.waveform_plot.setLabel('left', "Señal", units='A.U.')
        self.waveform_plot.setLabel('bottom', "Tiempo", units='s')
        self.waveform_curve = self.waveform_plot.plot(pen=self.default_pen, skipFiniteCheck=True)
        self.__mainWindow.ui.waveform_layout.addWidget(self.waveform_plot)

    def createFftPlot(self):
        self.fft_plot = pg.PlotWidget(title='Transformada de Fourier')
        self.fft_curve = pg.PlotCurveItem(pen=self.default_pen, skipFiniteCheck=True)
        self.fft_plot.addItem(self.fft_curve)
        self.fft_plot.autoRange()
        self.fft_plot.setMouseEnabled(x=False, y=True)
        self.fft_plot.showGrid(x=True, y=True)
        self.fft_plot.setXRange(self.FREQ_VECTOR.min(), self.FREQ_VECTOR.max())
        # self.fft_plot.setYRange(20 * np.log10(2 ** 11 * self.CHUNKSIZE) - 100, 20 * np.log10(2 ** 11 * self.CHUNKSIZE))
        self.fft_plot.setLabel('left', "Amplitud", units='A.U.')
        self.fft_plot.setLabel('bottom', "Frecuencia", units='Hz')
        self.__mainWindow.ui.fft_transform_layout.addWidget(self.fft_plot)
        self.waterfall_data = deque(maxlen=self.WATERFALL_FRAMES)

    def create_spectrogram_graphic(self):
        # image_data = np.random.rand(20, 20)
        self.waterfall_plot = pg.PlotWidget(title='Espectrograma', colspan=2)
        self.waterfall_plot.setLabel('left', "Frecuencia", units='Hz')
        self.waterfall_plot.showAxis('bottom', False)
        # waterfall_plot.setLabel('bottom', "Time", units='s')
        self.waterfall_plot.setXRange(0, self.WATERFALL_FRAMES * self.TIME_VECTOR.max())
        # waterfall_plot.enableAutoRange('x', True)
        self.waterfall_image = pg.ImageItem()
        self.waterfall_plot.addItem(self.waterfall_image)
        # waterfall_image.setImage(image_data)
        lut = self.generatePgColormap('jet')
        self.waterfall_image.setLookupTable(lut)
        tr = QtGui.QTransform()
        tr.scale((self.CHUNKSIZE / self.SAMPLE_RATE), self.FREQ_VECTOR.max() * 2. / self.N_FFT)
        # set scale: x in seconds, y in Hz
        self.waterfall_image.setTransform(tr)
        self.__mainWindow.ui.spectrogram_layout.addWidget(self.waterfall_plot)

    def update_waveform(self, valuesList):
        self.waveform_curve.setData(x=valuesList[0], y=valuesList[1])
        self.waveform_curve.setPos(valuesList[2], 0)