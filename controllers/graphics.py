from collections import deque
from threading import Timer
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
from pyqtgraph.exporters import ImageExporter
from time import perf_counter
from PySide2.QtCore import Slot, Qt, QObject, Signal
from controllers import reporter as rp

class GraphicsController(QObject):
    __mainWindow = None
    set_spectrogram_image_signal = Signal(object)
    def __init__(self, parent) -> None:
        super().__init__()
        self.__mainWindow = parent
        self.default_pen = pg.mkPen(width=1, color='y')
        self.default_pen.setStyle(Qt.PenStyle.SolidLine)
        self.createDefinitions()
        self.createWaveformPlot()
        self.createFftPlot()
        self.create_spectrogram_graphic()
        parent.ui.start_btn.clicked.connect(self.start_all)
        parent.ui.stop_btn.clicked.connect(self.stop_all)
        parent.ui.save_btn.clicked.connect(self.save)
        self.set_spectrogram_image_signal.connect(self.set_spectrogram_image)

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
        self.TIMEOUT = 51
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
        if self.running:
            self.waveform_curve.setData(x=valuesList[0], y=valuesList[1], clear=True)
            self.waveform_curve.setPos(valuesList[2], 0)

    def update_fft(self, values):
        if self.running:
            self.fft_curve.setData(x=values[0], y=values[1])
            self.fft_plot.enableAutoRange('y', True)

    def update_spectrogram_data(self, spectrogram_data):
        self.waterfall_data.append(spectrogram_data)

    def update_spectrogram(self):
        arr = np.c_[self.waterfall_data]
        if arr.size > 0:
            if arr.ndim == 1:
                arr = arr[:, np.newaxis]
            max = arr.max()
            min = max / 10
            # self.waterfall_image.setImage(arr, levels=(min, max), autoLevels=False)
            spectro_values = [arr, min, max]
            self.set_spectrogram_image_signal.emit(spectro_values)
        self.spectrogram_update_timer = Timer((self.TIMEOUT+1000)/1000, function=self.update_spectrogram)
        self.spectrogram_update_timer.daemon = True
        self.spectrogram_update_timer.start()

    def set_spectrogram_image(self, values):
        self.waterfall_image.setImage(values[0], levels=(values[1], values[2]), autoLevels=False)

    def start_spectrogram_updates(self):
        self.spectrogram_update_timer = Timer((self.TIMEOUT+1000)/1000, function=self.update_spectrogram)
        self.spectrogram_update_timer.daemon = True
        self.spectrogram_update_timer.start()

    def stop_spectrogram_updates(self):
        self.spectrogram_update_timer.cancel()

    def start_all(self):
        self.running = True
        self.start_spectrogram_updates()
        self.__mainWindow.ui.start_btn.setEnabled(False)

    def stop_all(self):
        self.running = False
        self.stop_spectrogram_updates()
        self.__mainWindow.ui.start_btn.setEnabled(True)

    def save(self):
        self.stop_all()

        fftExporter = ImageExporter(self.fft_plot.plotItem)
        fftExporter.parameters()['width'] = 2000
        fftExporter.export('images/fft.png')

        spectrogramExporter = ImageExporter(self.waterfall_plot.plotItem)
        spectrogramExporter.parameters()['width'] = 2000
        spectrogramExporter.export('images/spectrogram.png')

        nodename, city = self.__mainWindow.getReceptorNetNodenameAndCity()
        reportPath = rp.createDiploma(nodename, city)