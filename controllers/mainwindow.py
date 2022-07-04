from copy import deepcopy
from datetime import datetime
from queue import Empty
import sys
import platform
import time
import numpy as np
import pandas as pd
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, Slot, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QIntValidator)
from PySide2.QtWidgets import *
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from threading import Thread, Timer
import matplotlib.pyplot as plt
from sqlalchemy import true
import controllers.login as Login 
import services.user_service as user_service
import network.client as client
from controllers.singleton import SingletonClass

# GUI FILE
from visuals.ui_main import Ui_MainWindow
from controllers.formUser import FormUser
from controllers.formUpdateUser import FormUpdateUser
from styles.ui_styles import Style
GLOBAL_STATE = 0
GLOBAL_FULLSCREEN = 0
GLOBAL_TITLE_BAR = True
GLOBAL_BACKUP = 1

class MainWindow(QMainWindow):
    count = 1
    graphicsLoaded = False
    # authenticatedUser = None
    def __init__(self, authenticatedUser = None):
        try:
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            ########################################################################
            ## START - WINDOW ATTRIBUTES
            ########################################################################
            
            ## REMOVE ==> STANDARD TITLE BAR
            self.removeTitleBar(True)
            ## ==> END ##

            ## SET ==> WINDOW TITLE
            self.setWindowTitle('HEATS-BOARD')
            self.labelTitle('HEATS-BOARD')
            self.labelDescription('App Description')
            ## ==> END ##

            ## WINDOW SIZE ==> DEFAULT SIZE
            startSize = QSize(1280, 900)
            self.resize(startSize)
            self.setMinimumSize(startSize)
            global GLOBAL_STATE
            global GLOBAL_FULLSCREEN
            GLOBAL_STATE = 0
            GLOBAL_FULLSCREEN = 0
            # self.enableMaximumSize(self, 500, 720)
            ## ==> END ##

            ## ==> CREATE MENUS
            ########################################################################

            ## ==> TOGGLE MENU SIZE
            self.ui.btn_toggle_menu.clicked.connect(lambda: self.toggleMenu(220, True))
            ## ==> END ##

            ## ==> ADD CUSTOM MENUS
            self.ui.stackedWidget.setMinimumWidth(20)
            self.addNewMenu("Dashboard", "btn_home", "url(:/16x16/icons/16x16/cil-chart.png)", True)
            if (authenticatedUser is not None and authenticatedUser.role == 1):
                self.addNewMenu("Usuarios", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
            self.addNewMenu("Conexión", "btn_network", "url(:/16x16/icons/16x16/cil-rss.png)", True)
            self.addNewMenu("Configuración", "btn_settings", "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
            self.addNewMenu("Consola", "btn_console", "url(:/16x16/icons/16x16/cil-terminal.png)", False)
            self.addNewMenu("Cerrar Sesión", "btn_logout", "url(:/16x16/icons/16x16/cil-account-logout.png)", False)
            ## ==> END ##

            # START MENU => SELECTION
            self.selectStandardMenu("btn_home")
            ## ==> END ##
            
            ## USER ICON ==> SHOW HIDE
            # self.userIcon("AL", "", True)
            ## ==> END ##

            # self.loadUserTable()


            ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
            ########################################################################
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if self.returnStatus() == 1:
                    self.maximize_restore()

                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

            # WIDGET TO MOVE
            self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
            ## ==> END ##

            ## ==> LOAD DEFINITIONS
            ########################################################################
            self.uiDefinitions()
            ## ==> END ##

            ## ==> QTableWidget RARAMETERS
            ########################################################################
            # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            ## ==> END ##


            #####
            ## CONNECTIONS
            #####

            self.ui.eliminateBtn.clicked.connect(self.eliminateCurrentRow)
            self.ui.createBtn.clicked.connect(self.showCreateUsersDialog)
            self.ui.editBtn.clicked.connect(self.showUpdateUsersDialog)
            self.ui.connectBtn.clicked.connect(self.connectToHost)

            ########################################################################
            #                                                                      #
            ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
            #                                                                      #
            ############################## ---/--/--- ##############################
            
            #HOST PORT INPUT MASK
            self.intValidator = QIntValidator()
            self.intValidator.setBottom(0)
            self.intValidator.setTop(65535)
            self.ui.hostPortLineEdit.setValidator(self.intValidator)
            self.ui.hostPortLineEdit.setMaxLength(5)
            

            self.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> HEATS-BOARD Inicializado.\r")
            #LOAD DASHBOARD GRAPHICS
            self.loadGraphics()
            
            # LOAD SETTINGS
            try:    
                loadSettingsThread = Thread(target=self.loadSettings)
                loadSettingsThread.start()
            except Exception as e:
                print(str(e))
            
            # BACKUP THREAD
            try:
                backupExecutionTimer = Timer(30.0, self.checkIfBackupOn)
                backupExecutionTimer.daemon = True
                backupExecutionTimer.start()
            except Exception as e:
                print(str(e))

            # Static Chart
            # layout = QtWidgets.QGridLayout(self.ui.page_home)

            # STATES CHANGES CONNECTIONS
            self.ui.backupCheckBox.stateChanged.connect(self.synchronizeBackupWithSettings)

            ## ==> START PAGE
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.tightLayoutCharts()
            ## ==> END ##

            ## SHOW ==> MAIN WINDOW
            ########################################################################
            # self.show()
            ## ==> END ##
        except Exception as e:
            print(str(e))

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.loadGraphics()
            self.resetStyle("btn_home")
            self.labelPage("Home")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))
            self.tightLayoutCharts()

        # PAGE USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_users)
            self.loadUserTable()
            self.resetStyle("btn_new_user")
            self.labelPage("Users")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))

        # PAGE SETTINGS
        if btnWidget.objectName() == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            self.resetStyle("btn_settings")
            self.labelPage("Settings")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))
        
        # PAGE NETWORK
        if btnWidget.objectName() == "btn_network":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_network)
            self.resetStyle("btn_network")
            self.labelPage("Network")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))

        # CONSOLE BTN
        if btnWidget.objectName() == "btn_console":
            self.toggleConsole(150, True)
        
        # LOGOUT BTN
        if btnWidget.objectName() == "btn_logout":
            self.saveBeforeExit()
            login = Login.Login()
            login.show()
            login.activateWindow()
            login.raise_()

    def loadGraphics(self):
        localFileReaded = False
        try:
            data = pd.read_csv("network/log.txt", nrows=20, sep="/", header=None)
            localFileReaded = True
        except:
            self.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> No se encontró el archivo proveniente de HEATS-NET. Debe conectarse al servidor.\r")
            self.ui.console.setFocus()
        if(not localFileReaded):
            try:
                data = pd.read_csv("backup/log.txt", nrows=20, sep="/", header=None)
                self.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> Se cargará la última información guardada.\r")
            except:
                self.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> No se encontró el archivo salva, no se podrá mostrar información.\r")
                self.ui.console.setFocus()
                return
        if(data is not None and self.graphicsLoaded == False):
            dataToDisplay = []
            for x in range(300,500):
                dataToDisplay.append(data.iloc[0][x])

            self.static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            self.ui.chartLayout1.addWidget(NavigationToolbar(self.static_canvas, self))
            self.ui.chartLayout1.addWidget(self.static_canvas)

            self._static_ax = self.static_canvas.figure.subplots()
            self._static_ax.set_title("Frecuencia | Valor")
            self._static_ax.set_ylabel("Frecuencia")
            self._static_ax.set_xlabel("Valor")
            # self._static_ax.yaxis.set_visible(False)
            x = np.linspace(0, len(dataToDisplay), len(dataToDisplay))
            y = np.array(dataToDisplay)
            # self._static_ax.scatter()
            self._static_ax.plot(x, y)

            # Dynamic Chart
            self.dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            self.ui.chartLayout2.addWidget(NavigationToolbar(self.dynamic_canvas, self))
            self.ui.chartLayout2.addWidget(self.dynamic_canvas)

            self._dynamic_ax = self.dynamic_canvas.figure.subplots()
            self._dynamic_ax.set_title("Frecuencias Críticas y Fatales")
            self._dynamic_ax.set_ylabel("Frecuencia")
            self._dynamic_ax.set_xlabel("Valor")
            dataFiltered = dataToDisplay.copy()
            dataToFilter = dataToDisplay.copy()
            for value in dataToFilter:
                if(value <= 40):
                    dataFiltered.remove(value)
            xDynamic = np.linspace(0, len(dataFiltered), len(dataFiltered))
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
            self.ui.chartLayout3.addWidget(self.static_canvas_pie)
            self.ui.chartLayout3.addWidget(NavigationToolbar(self.static_canvas_pie, self))

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
            self.ui.chartLayout4.addWidget(self.static_canvas_lines)
            self.ui.chartLayout4.addWidget(NavigationToolbar(self.static_canvas_lines,self))
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
            self.graphicsLoaded = True
        
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


    def _update_canvas(self):
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._line.set_data(t, np.sin(t + time.time()))
        self._line.figure.canvas.draw()

    def eliminateCurrentRow(self):
        item = self.ui.userTableWidget.currentItem()
        if(item is not None):
            user = item.data(Qt.UserRole+1)
            if(user.role == 1):
                operators = user_service.getAllOperators()
                if(len(operators) > 1):
                    user_service.delete_user(user)
                    self.loadUserTable()
                else:
                    errMsgBox = QMessageBox()
                    errMsgBox.setText("Debe dejar al menos un operador en el sistema.")
                    errMsgBox.exec_()
            else:
                user_service.delete_user(user)
                self.loadUserTable()
            # self.ui.eliminateBtn.setEnabled(False)
        else:
            msgBox = QMessageBox()
            msgBox.setText("Debe seleccionar un usuario.")
            msgBox.exec_()

    # def enableEliminateBtn(self):
    #     self.ui.eliminateBtn.setEnabled(True)
    
    @Slot()
    def loadUserTable(self):
        # self.ui.userTableWidget.resizeRowsToContents()
        rows = []
        for user in user_service.read_all():
            rows.append((user.id, user.username, user.email, user.date_created.date()))
        self.ui.userTableWidget.setColumnCount(4)
        self.ui.userTableWidget.setHorizontalHeaderLabels(("ID", "Username", "Email", "Date Created"))
        self.ui.userTableWidget.horizontalHeader().setVisible(True)
        self.ui.userTableWidget.setRowCount(len(rows))
        for row, cols in enumerate(rows):
            for col, text in enumerate(cols):
                table_item = QTableWidgetItem(str(text))
                table_item.setData(QtCore.Qt.UserRole+1, user_service.read_byID(rows[row][0]))
                self.ui.userTableWidget.setItem(row, col, table_item)

    def synchronizeBackupWithSettings(self):
        global GLOBAL_BACKUP
        if(self.ui.backupCheckBox.isChecked()):
            GLOBAL_BACKUP = 1
        else:
            GLOBAL_BACKUP = 0

    def checkIfBackupOn(self):
        global GLOBAL_BACKUP
        if(GLOBAL_BACKUP):
            try:
                backupThread = Thread(target=self.backupTemporaryFile)
                backupThread.daemon = True
                backupThread.start()
            except Exception as e:
                print(str(e))
        try:
            checkIfBackupTimer = Timer(30.0, self.checkIfBackupOn)
            checkIfBackupTimer.daemon = True
            checkIfBackupTimer.start()
        except Exception as e:
            print(str(e))


    def saveBeforeExit(self):
        try:
            saveThread = Thread(target=self.saveSettings)
            saveThread.daemon = True
            saveThread.start()
        except Exception as e:
            print(str(e))
        self.close()    
    
    def saveSettings(self):
        backup = self.ui.backupCheckBox.isChecked()
        try:
            with open("settings.txt", "w") as file:
                if(backup):
                    file.write("True")
                else:
                    file.write("False")
        except Exception as e:
            print(str(e))

    def loadSettings(self):
        global GLOBAL_BACKUP
        content = ""
        try:
            with open("settings.txt", "r") as file:
                content = file.read()
        except Exception as e:
            print(str(e))
        if(content != ""):
            if("True" in content):
                GLOBAL_BACKUP = 1
                self.ui.backupCheckBox.setChecked(True)
            else: 
                if("False" in content):
                    GLOBAL_BACKUP = 0
                    self.ui.backupCheckBox.setChecked(False)
        else:
            GLOBAL_BACKUP = 1
            self.ui.backupCheckBox.setChecked(True)


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def tightLayoutCharts(self):
        if(self.graphicsLoaded):
            self.static_canvas.figure.tight_layout()
            self.dynamic_canvas.figure.tight_layout()
            self.static_canvas_pie.figure.tight_layout()
            self.static_canvas_lines.figure.tight_layout()

    def winFullscreen(self):
        global GLOBAL_FULLSCREEN
        global GLOBAL_STATE
        status = GLOBAL_FULLSCREEN
        if status == 0:
            self.showFullScreen()
            self.tightLayoutCharts()
            GLOBAL_FULLSCREEN = 1
            GLOBAL_STATE = 1
            self.ui.central_widget_layout.setContentsMargins(0,0,0,0)
            self.ui.frame_top_btns.setMaximumHeight(0)
            self.ui.frame_size_grip.hide()
        else:
            self.showNormal()
            self.tightLayoutCharts()
            GLOBAL_FULLSCREEN = 0
            GLOBAL_STATE = 0
            self.ui.central_widget_layout.setContentsMargins(10,10,10,10)
            self.ui.frame_top_btns.setMaximumHeight(42)
            self.ui.frame_size_grip.show()
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            self.tightLayoutCharts()
            GLOBAL_STATE = 1
            self.ui.central_widget_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.tightLayoutCharts()
            self.resize(self.width()+1, self.height()+1)
            self.ui.central_widget_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()
    
    def returnStatus(self):
        return GLOBAL_STATE

    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def toggleConsole(self, maxHeight, enable):
        if enable:
            # GET WIDTH
            height = self.ui.frame_console.height()
            maxExtend = maxHeight
            standard = 0

            # SET MAX WIDTH
            if height == 8:
                heightExtended = maxExtend
            else:
                heightExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_console, b"minimumHeight")
            self.animation.setDuration(300)
            self.animation.setStartValue(height)
            self.animation.setEndValue(heightExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(self, status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(self.count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)
        

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    def selectMenu(self, getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        return select

    ## ==> DESELECT
    def deselectMenu(self, getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(self.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ## ==> USER ICON
    ########################################################################
    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            # SET TEXT
            self.ui.label_user_icon.setText(initialsTooltip)

            # SET ICON
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    def showCreateUsersDialog(self):
        formUser = FormUser(self)
        formUser.show()

    def showUpdateUsersDialog(self):
        item = self.ui.userTableWidget.currentItem()
        if(item is not None):
            user = item.data(Qt.UserRole + 1)
            formUser = FormUpdateUser(self)
            formUser.setLinesEditsValues(user)
            formUser.show()
        else:
            msgBox = QMessageBox()
            msgBox.setText("Debe seleccionar un usuario.")
            msgBox.exec_()

    def connectToHost(self):
        host = self.ui.hostLineEdit.text()
        hostPortStr = self.ui.hostPortLineEdit.text()
        if(hostPortStr != '' and host != ''):
            self.ui.connectBtn.setEnabled(False)
            hostPort = int(self.ui.hostPortLineEdit.text())
            connectionThread = Thread(target = client.connectToHost, args= (self, host,hostPort))
            connectionThread.start()
        else:
            msgBox = QMessageBox()
            msgBox.setText("La dirección del servidor o el puerto de red no puede estar vacío.")
            msgBox.exec_()

    def backupTemporaryFile(self):
        contentReaded = False
        global GLOBAL_BACKUP
        if(GLOBAL_BACKUP):
            try:
                with open("network/log.txt", "r") as localFile:
                    content = localFile.readlines()
                    contentReaded = True
            except Exception as e:
                print(str(e))
                print(f"No se encuentra el archivo local.")
                self.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> No se encuentra el archivo de información local\r")
            if(contentReaded and len(content) > 0):
                try:
                    with open("backup/log.txt", "w") as backupFile:
                        backupFile.writelines(content)
                except Exception as e:
                    print(str(e))
                    print(f"Ocurrió un error al intentar hacer la salva de la información")
                    self.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> Ocurrió un error al intentar hacer la salva de la información.")
            


    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################

    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: self.maximize_restore())

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.central_widget_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()


        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: self.maximize_restore())

        ## ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(self.saveBeforeExit)

        ## ==> FULLSCREEN
        self.ui.btn_fullscreen.clicked.connect(self.winFullscreen)
        self.ui.btn_settings_fullscreen.clicked.connect(self.winFullscreen) 


    ########################################################################
    ## END - GUI DEFINITIONS
    ######################################################################## 

    ## ==> END ##


