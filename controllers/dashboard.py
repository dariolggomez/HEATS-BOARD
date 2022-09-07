from controllers.mainwindow import *
class DashboardController():
    __mainWindow = None
    def __init__(self, parent):
        self.__mainWindow = parent
    def loadGraphics(self):
        localFileReaded = False
        try:
            data = pd.read_csv("network/log.txt", nrows=20, sep="/", header=None)
            localFileReaded = True
        except:
            self.__mainWindow.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> No se encontró el archivo proveniente de HEATS-NET. Debe conectarse al servidor.\r")
            self.__mainWindow.ui.console.setFocus()
        if(not localFileReaded):
            try:
                data = pd.read_csv("backup/log.txt", nrows=20, sep="/", header=None)
                self.__mainWindow.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> Se cargará la última información guardada.\r")
            except:
                self.__mainWindow.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> No se encontró el archivo salva, no se podrá mostrar información.\r")
                self.__mainWindow.ui.console.setFocus()
                return
        if(data is not None and self.__mainWindow.graphicsLoaded == False):
            dataToDisplay = []
            for x in range(300,500):
                dataToDisplay.append(data.iloc[0][x])

            self.static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            self.__mainWindow.ui.chartLayout1.addWidget(NavigationToolbar(self.static_canvas, self.__mainWindow))
            self.__mainWindow.ui.chartLayout1.addWidget(self.static_canvas)

            self._static_ax = self.static_canvas.figure.subplots()
            self._static_ax.set_title("Frecuencia | Tiempo")
            self._static_ax.set_ylabel("Frecuencia")
            self._static_ax.set_xlabel("Tiempo")
            # self._static_ax.yaxis.set_visible(False)
            x = np.linspace(0, len(dataToDisplay)-1, len(dataToDisplay))
            y = np.array(dataToDisplay)
            # self._static_ax.scatter()
            self._static_ax.plot(x, y)

            # Dynamic Chart
            self.dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            self.__mainWindow.ui.chartLayout2.addWidget(NavigationToolbar(self.dynamic_canvas, self.__mainWindow))
            self.__mainWindow.ui.chartLayout2.addWidget(self.dynamic_canvas)

            self._dynamic_ax = self.dynamic_canvas.figure.subplots()
            self._dynamic_ax.set_title("Frecuencias Críticas y Fatales")
            self._dynamic_ax.set_ylabel("Frecuencia")
            self._dynamic_ax.set_xlabel("Tiempo")
            dataFiltered = dataToDisplay.copy()
            dataToFilter = dataToDisplay.copy()
            for value in dataToFilter:
                if(value <= 40):
                    dataFiltered.remove(value)
            xDynamic = np.linspace(0, len(dataFiltered)-1, len(dataFiltered))
            yDynamic = np.array(dataFiltered)
            self._dynamic_ax.plot(xDynamic,yDynamic)
            # Set up a Line2D.
            # self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
            # self._timer = dynamic_canvas.new_timer(6000)
            # self._timer.add_callback(self._update_canvas)
            # self._timer.start()
            
            # Pie Chart
            labels = 'Parámetros Críticos', 'Parámetros de Alerta', 'Parámetros Normales', 'Parámetros Fatales'
            sizeNormalParameters,countNormalParameters = self.countNormalParams(dataToDisplay)
            sizeAlertParameters,countAlertParameters = self.countAlertParams(dataToDisplay)
            sizeCriticalParameters,countCriticalParameters = self.countCriticalParams(dataToDisplay)
            sizeFatalParameters,countFatalParameters = self.countFatalParams(dataToDisplay)
            # print(sizeNormalParameters)
            # print(sizeAlertParameters)
            # print(sizeCriticalParameters)
            # print(sizeFatalParameters)
            sizes = [sizeCriticalParameters, sizeAlertParameters, sizeNormalParameters, sizeFatalParameters]
            explode = (0, 0, 0.1, 0)
            self.static_canvas_pie = FigureCanvas(Figure(figsize=(5, 3)))
            self.__mainWindow.ui.chartLayout3.addWidget(self.static_canvas_pie)
            self.__mainWindow.ui.chartLayout3.addWidget(NavigationToolbar(self.static_canvas_pie, self.__mainWindow))

            self._pie_ax = self.static_canvas_pie.figure.subplots()
            self._pie_ax.set_title("Porcentaje por Criticidad de los Valores")
            self._pie_ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
            self._pie_ax.axis('equal')
            self._pie_ax.plot()

            #Bar Chart 
            labels = ['Normales', 'Alerta', 'Críticos', 'Fatales']
            parameters = [countNormalParameters, countAlertParameters, countCriticalParameters, countFatalParameters]
            # women_means = [25, 32, 34, 20,]

            x = np.arange(len(labels))  # label locations
            width = 0.35  # width of the bars

            self.static_canvas_lines = FigureCanvas(Figure(figsize=(5,4)))
            self.__mainWindow.ui.chartLayout4.addWidget(self.static_canvas_lines)
            self.__mainWindow.ui.chartLayout4.addWidget(NavigationToolbar(self.static_canvas_lines,self.__mainWindow))
            self.lines_ax = self.static_canvas_lines.figure.subplots()
            rects1 = self.lines_ax.bar(x, parameters, width, label='Parámetros')
            # rects2 = self.lines_ax.bar(x + width/2, women_means, width, label='Femenino')

            self.lines_ax.set_ylabel('Valor')
            self.lines_ax.set_title('Parámetros por Criticidad')
            self.lines_ax.set_xticks(x, labels)
            self.lines_ax.legend()

            self.lines_ax.bar_label(rects1, padding=3)
            # self.lines_ax.bar_label(rects2, padding=3)

            self.static_canvas_lines.figure.tight_layout()
            self.lines_ax.plot()
            self.__mainWindow.graphicsLoaded = True

    def countNormalParams(self, data):
        count = 0
        for x in range(0, len(data)):
            if(data[x] <= 30):
                count = count + 1

        percent = count/len(data) * 100  
        return percent,count

    def countAlertParams(self, data):
        count = 0
        for x in range(0, len(data)):
            if(data[x] > 30 and data[x] <= 40):
                count = count + 1

        percent = count/len(data) * 100  
        return percent,count

    def countCriticalParams(self, data):
        count = 0
        for x in range(0, len(data)):
            if(data[x] > 40 and data[x] <= 80):
                count = count + 1

        percent = count/len(data) * 100  
        return percent,count

    def countFatalParams(self, data):
        count = 0
        for x in range(0, len(data)):
            if(data[x] > 80):
                count = count + 1

        percent = count/len(data) * 100  
        return percent,count

    def tightLayoutCharts(self):
        if(self.__mainWindow.graphicsLoaded):
            self.static_canvas.figure.tight_layout()
            self.dynamic_canvas.figure.tight_layout()
            self.static_canvas_pie.figure.tight_layout()
            self.static_canvas_lines.figure.tight_layout()