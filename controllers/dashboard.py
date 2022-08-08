from controllers.mainwindow import *
class DashboardController():
    def loadGraphics(parent):
        localFileReaded = False
        try:
            data = pd.read_csv("network/log.txt", nrows=20, sep="/", header=None)
            localFileReaded = True
        except:
            parent.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> No se encontró el archivo proveniente de HEATS-NET. Debe conectarse al servidor.\r")
            parent.ui.console.setFocus()
        if(not localFileReaded):
            try:
                data = pd.read_csv("backup/log.txt", nrows=20, sep="/", header=None)
                parent.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> Se cargará la última información guardada.\r")
            except:
                parent.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> No se encontró el archivo salva, no se podrá mostrar información.\r")
                parent.ui.console.setFocus()
                return
        if(data is not None and parent.graphicsLoaded == False):
            dataToDisplay = []
            for x in range(300,500):
                dataToDisplay.append(data.iloc[0][x])

            parent.static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            parent.ui.chartLayout1.addWidget(NavigationToolbar(parent.static_canvas, parent))
            parent.ui.chartLayout1.addWidget(parent.static_canvas)

            parent._static_ax = parent.static_canvas.figure.subplots()
            parent._static_ax.set_title("Frecuencia | Tiempo")
            parent._static_ax.set_ylabel("Frecuencia")
            parent._static_ax.set_xlabel("Tiempo")
            # self._static_ax.yaxis.set_visible(False)
            x = np.linspace(0, len(dataToDisplay)-1, len(dataToDisplay))
            y = np.array(dataToDisplay)
            # self._static_ax.scatter()
            parent._static_ax.plot(x, y)

            # Dynamic Chart
            parent.dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            parent.ui.chartLayout2.addWidget(NavigationToolbar(parent.dynamic_canvas, parent))
            parent.ui.chartLayout2.addWidget(parent.dynamic_canvas)

            parent._dynamic_ax = parent.dynamic_canvas.figure.subplots()
            parent._dynamic_ax.set_title("Frecuencias Críticas y Fatales")
            parent._dynamic_ax.set_ylabel("Frecuencia")
            parent._dynamic_ax.set_xlabel("Tiempo")
            dataFiltered = dataToDisplay.copy()
            dataToFilter = dataToDisplay.copy()
            for value in dataToFilter:
                if(value <= 40):
                    dataFiltered.remove(value)
            xDynamic = np.linspace(0, len(dataFiltered)-1, len(dataFiltered))
            yDynamic = np.array(dataFiltered)
            parent._dynamic_ax.plot(xDynamic,yDynamic)
            # Set up a Line2D.
            # self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
            # self._timer = dynamic_canvas.new_timer(6000)
            # self._timer.add_callback(self._update_canvas)
            # self._timer.start()
            
            # Pie Chart
            labels = 'Parámetros Críticos', 'Parámetros de Alerta', 'Parámetros Normales', 'Parámetros Fatales'
            sizeNormalParameters,countNormalParameters = parent.countNormalParams(dataToDisplay)
            sizeAlertParameters,countAlertParameters = parent.countAlertParams(dataToDisplay)
            sizeCriticalParameters,countCriticalParameters = parent.countCriticalParams(dataToDisplay)
            sizeFatalParameters,countFatalParameters = parent.countFatalParams(dataToDisplay)
            # print(sizeNormalParameters)
            # print(sizeAlertParameters)
            # print(sizeCriticalParameters)
            # print(sizeFatalParameters)
            sizes = [sizeCriticalParameters, sizeAlertParameters, sizeNormalParameters, sizeFatalParameters]
            explode = (0, 0, 0.1, 0)
            parent.static_canvas_pie = FigureCanvas(Figure(figsize=(5, 3)))
            parent.ui.chartLayout3.addWidget(parent.static_canvas_pie)
            parent.ui.chartLayout3.addWidget(NavigationToolbar(parent.static_canvas_pie, parent))

            parent._pie_ax = parent.static_canvas_pie.figure.subplots()
            parent._pie_ax.set_title("Porcentaje por Criticidad de los Valores")
            parent._pie_ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
            parent._pie_ax.axis('equal')
            parent._pie_ax.plot()

            #Bar Chart 
            labels = ['Normales', 'Alerta', 'Críticos', 'Fatales']
            parameters = [countNormalParameters, countAlertParameters, countCriticalParameters, countFatalParameters]
            # women_means = [25, 32, 34, 20,]

            x = np.arange(len(labels))  # label locations
            width = 0.35  # width of the bars

            parent.static_canvas_lines = FigureCanvas(Figure(figsize=(5,4)))
            parent.ui.chartLayout4.addWidget(parent.static_canvas_lines)
            parent.ui.chartLayout4.addWidget(NavigationToolbar(parent.static_canvas_lines,parent))
            parent.lines_ax = parent.static_canvas_lines.figure.subplots()
            rects1 = parent.lines_ax.bar(x, parameters, width, label='Parámetros')
            # rects2 = self.lines_ax.bar(x + width/2, women_means, width, label='Femenino')

            parent.lines_ax.set_ylabel('Valor')
            parent.lines_ax.set_title('Parámetros por Criticidad')
            parent.lines_ax.set_xticks(x, labels)
            parent.lines_ax.legend()

            parent.lines_ax.bar_label(rects1, padding=3)
            # self.lines_ax.bar_label(rects2, padding=3)

            parent.static_canvas_lines.figure.tight_layout()
            parent.lines_ax.plot()
            parent.graphicsLoaded = True