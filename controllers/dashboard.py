from controllers.mainwindow import *
import yaml
from yaml.loader import SafeLoader
from PySide2 import QtCore
from threading import Thread

class DashboardController(QObject):
    __mainWindow = None
    showConsoleMessageSignal = QtCore.Signal(str)
    compareDataSignal = QtCore.Signal(int, float, float, float, float)
    def __init__(self, parent):
        super().__init__()
        self.__mainWindow = parent
        self.showConsoleMessageSignal.connect(self.__mainWindow.showConsoleMessage)
        self.compareDataSignal.connect(self.compare_data)
        self.load_data()
        self.saverThread = Thread(target=self.saveData)
        self.saverThread.daemon = True
    
    def load_data(self):
        try:
            with open('backup/data.yaml') as f:
                self.dashData = yaml.load(f, Loader=SafeLoader)
            if self.dashData == None:
                self.dashData = {}
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
        
    QtCore.Slot()    
    def compare_data(self, net_id, maxAmplitude, maxAmpFrequency, minAmplitude, minAmpFrequency):
        needSave = False
        if self.dashData.get(net_id) is not None:
            if self.dashData[net_id][0] < maxAmplitude:
                self.dashData[net_id][0] = maxAmplitude
                self.dashData[net_id][2] = maxAmpFrequency
                needSave = True
            if self.dashData[net_id][1] > minAmplitude:
                self.dashData[net_id][1] = minAmplitude
                self.dashData[net_id][3] = minAmpFrequency
                needSave = True
            if needSave and not self.saverThread.is_alive():
                self.saverThread = Thread(target=self.saveData)
                self.saverThread.daemon = True
                self.saverThread.start()
        else:
            self.dashData[net_id] = [maxAmplitude, minAmplitude, maxAmpFrequency, minAmpFrequency]
            if not self.saverThread.is_alive():
                self.saverThread = Thread(target=self.saveData)
                self.saverThread.daemon = True
                self.saverThread.start()
        
    def saveData(self):
        with open('backup/data.yaml', 'w') as f:
            yaml.dump(self.dashData, f)
