import yaml
from yaml.loader import SafeLoader
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtWidgets import QTableWidgetItem
from threading import Thread

class DashboardController(QObject):
    __mainWindow = None
    showConsoleMessageSignal = Signal(str)
    compareDataSignal = Signal(int, float, float, float, float)
    loadMaxAmpTableSignal = Signal()
    def __init__(self, parent):
        super().__init__()
        self.__mainWindow = parent
        self.showConsoleMessageSignal.connect(self.__mainWindow.showConsoleMessage)
        self.compareDataSignal.connect(self.compare_data)
        self.loadMaxAmpTableSignal.connect(self.load_max_amp_table)
        self.init_tables()
        self.load_data()
        self.saverThread = Thread(target=self.saveData)
        self.saverThread.daemon = True
    
    def init_tables(self):
        #Max amplitude table
        self.__mainWindow.ui.maxAmplitudeTable.setColumnCount(2)
        self.__mainWindow.ui.maxAmplitudeTable.setHorizontalHeaderLabels(("Nombre","Magnitud"))
        self.__mainWindow.ui.maxAmplitudeTable.horizontalHeader().setVisible(True)

        #Max frequenct table
        self.__mainWindow.ui.maxFrequencyTable.setColumnCount(2)
        self.__mainWindow.ui.maxFrequencyTable.setHorizontalHeaderLabels(("Nombre","Frecuencia"))
        self.__mainWindow.ui.maxFrequencyTable.horizontalHeader().setVisible(True)

        #Min amplitude table
        self.__mainWindow.ui.minAmplitudeTable.setColumnCount(2)
        self.__mainWindow.ui.minAmplitudeTable.setHorizontalHeaderLabels(("Nombre","Magnitud"))
        self.__mainWindow.ui.minAmplitudeTable.horizontalHeader().setVisible(True)

        #Min frequency table
        self.__mainWindow.ui.minFrequencyTable.setColumnCount(2)
        self.__mainWindow.ui.minFrequencyTable.setHorizontalHeaderLabels(("Nombre","Frecuencia"))
        self.__mainWindow.ui.minFrequencyTable.horizontalHeader().setVisible(True)

    @Slot()
    def load_max_amp_table(self):
        rows = []
        for key in self.dashData:
            rows.append((self.dashData.get(key)[0], self.dashData.get(key)[1]))
        self.__mainWindow.ui.maxAmplitudeTable.setRowCount(len(rows))
        for row, cols in enumerate(rows):
            for col, text in enumerate(cols):
                table_item = QTableWidgetItem(str(text))
                table_item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.__mainWindow.ui.maxAmplitudeTable.setItem(row, col, table_item)
    
    def load_data(self):
        try:
            with open('backup/data.yaml') as f:
                self.dashData = yaml.load(f, Loader=SafeLoader)
            if self.dashData == None:
                self.dashData = {}
            else:
                self.loadMaxAmpTableSignal.emit()
        except Exception as e:
            print(e)
            self.showConsoleMessageSignal.emit("No se pudieron cargar los datos del dashboard. Se creará una nueva salva al recibir datos.")
            self.dashData = {}

    def recognize_data(self, values, net_id):
        maxAmplitude = max(values[1])
        minAmplitude = abs(min(values[1]))
        maxAmpIndex = 0
        minAmpIndex = 0
        for index, item in enumerate(values[1]):
            if item == maxAmplitude:
                maxAmpIndex = index
                break
        for index, item in enumerate(values[1]):
            if abs(item) == minAmplitude:
                minAmpIndex = index
                break
        maxAmpFrequency = values[0][maxAmpIndex]
        minAmpFrequency = values[0][minAmpIndex]
        if maxAmpFrequency != max(values[0]) and minAmpFrequency != min(values[0]):
            self.compareDataSignal.emit(net_id, maxAmplitude, maxAmpFrequency, minAmplitude, minAmpFrequency)
        
    @Slot()    
    def compare_data(self, net_id, maxAmplitude, maxAmpFrequency, minAmplitude, minAmpFrequency):
        needSave = False
        if self.dashData.get(net_id) is not None:
            if self.dashData[net_id][1] < maxAmplitude:
                self.dashData[net_id][1] = maxAmplitude
                self.dashData[net_id][3] = maxAmpFrequency
                needSave = True
            if self.dashData[net_id][2] > minAmplitude:
                self.dashData[net_id][2] = minAmplitude
                self.dashData[net_id][4] = minAmpFrequency
                needSave = True
            if needSave and not self.saverThread.is_alive():
                self.saverThread = Thread(target=self.saveData)
                self.saverThread.daemon = True
                self.saverThread.start()
        else:
            self.dashData[net_id] = [net_id, maxAmplitude, minAmplitude, maxAmpFrequency, minAmpFrequency]
            if not self.saverThread.is_alive():
                self.saverThread = Thread(target=self.saveData)
                self.saverThread.daemon = True
                self.saverThread.start()
        
    def saveData(self):
        with open('backup/data.yaml', 'w') as f:
            yaml.dump(self.dashData, f)
        self.loadMaxAmpTableSignal.emit()
