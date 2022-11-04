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
from controllers.dashboard import DashboardController 
import services.user_service as user_service
import network.app_server as server
from controllers.singleton import SingletonClass
from controllers import graphics, nodesCentre

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
    __net_nodes_in_use = list()
    def __init__(self, authenticatedUser = None):
        try:
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.serverController = server.ServerController(self)
            self.nodesCentreController = nodesCentre.NodesCentreController(self)
            self.graphicsController = graphics.GraphicsController(self)
            ########################################################################
            ## START - WINDOW ATTRIBUTES
            ########################################################################
            
            ## REMOVE ==> STANDARD TITLE BAR
            self.removeTitleBar(True)
            ## ==> END ##

            ## SET ==> WINDOW TITLE
            self.setWindowTitle('HEATS-BOARD')
            self.labelTitle('HEATS-BOARD')
            self.labelDescription('Herramienta para la Visualización Centralizada de Información')
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
            self.addNewMenu("Centro de Nodos", "btn_nodes", "url(:/16x16/icons/16x16/cil-layers.png)", True)
            self.addNewMenu("Dashboard", "btn_dashboard", "url(:/16x16/icons/16x16/cil-chart-line.png)", True)
            self.addNewMenu("Gráficas", "btn_rt_graphics", "url(:/16x16/icons/16x16/cil-chart.png)", True)
            if (authenticatedUser is not None and authenticatedUser.role == 1):
                self.addNewMenu("Usuarios", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
            self.addNewMenu("Conexión", "btn_network", "url(:/16x16/icons/16x16/cil-rss.png)", True)
            self.addNewMenu("Configuración", "btn_settings", "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
            self.addNewMenu("Consola", "btn_console", "url(:/16x16/icons/16x16/cil-terminal.png)", False)
            self.addNewMenu("Cerrar Sesión", "btn_logout", "url(:/16x16/icons/16x16/cil-account-logout.png)", False)
            ## ==> END ##

            # START MENU => SELECTION
            self.selectStandardMenu("btn_nodes")
            self.labelPage("Centro de Nodos")
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
            self.ui.disconnectBtn.clicked.connect(self.disconnectServer)

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
            self.dashboardController = DashboardController(self)
            self.dashboardController.loadGraphics()
            
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
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_nodes_centre)
            self.dashboardController.tightLayoutCharts()
            ## ==> END ##

            ## SHOW ==> MAIN WINDOW
            ########################################################################
            # self.show()
            ## ==> END ##
        except Exception as e:
            print(str(e))

    def getNetNodesInUse(self):
        return self.__net_nodes_in_use
    @Slot()
    def addNetNodeInUse(self, netNodeDict):
        exist = False
        for netNodeDict in self.__net_nodes_in_use:
            if netNodeDict.get("id") == netNodeDict.get("id"):
                exist = True
                raise ValueError(f"Ocurrió un error al establecer el uso del nodo.")
        if not exist:
            self.__net_nodes_in_use.append(netNodeDict) 
            
    @Slot()
    def removeNetNodeInUse(self, netId):
        if(self.__net_nodes_in_use.count(netId) == 1):
            self.__net_nodes_in_use.remove(netId)
        else:    
            raise ValueError(f"No se encontró el nodo a desconectar.")
    @Slot()
    def checkIfNetNodeInUse(self, netId):
        if(self.__net_nodes_in_use.count(netId) == 1):
            return True
        else:
            return False

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        
        btnWidget = self.sender()

        # Page Nodes Centre
        if btnWidget.objectName() == "btn_nodes":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_nodes_centre)
            self.resetStyle("btn_nodes")
            self.labelPage("Centro de Nodos")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))

        # PAGE Dashboard
        if btnWidget.objectName() == "btn_dashboard":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            if(self.graphicsLoaded == False):
                self.dashboardController.loadGraphics()
            self.resetStyle("btn_dashboard")
            self.labelPage("Dashboard")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))
            self.dashboardController.tightLayoutCharts()
        
        # RT Graphics
        if btnWidget.objectName() == "btn_rt_graphics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_rt_graphics)
            self.resetStyle("btn_rt_graphics")
            self.labelPage("Gráficas")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))

        # PAGE USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_users)
            self.loadUserTable()
            self.resetStyle("btn_new_user")
            self.labelPage("Usuarios")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))

        # PAGE SETTINGS
        if btnWidget.objectName() == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            self.resetStyle("btn_settings")
            self.labelPage("Configuración")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))
        
        # PAGE NETWORK
        if btnWidget.objectName() == "btn_network":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_network)
            self.resetStyle("btn_network")
            self.labelPage("Conexión")
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
            rows.append((user.id, user.role, user.username, user.email, user.date_created.date()))
        self.ui.userTableWidget.setColumnCount(5)
        self.ui.userTableWidget.setHorizontalHeaderLabels(("ID","Rol", "Nombre de Usuario", "Correo", "Fecha de Creación"))
        self.ui.userTableWidget.horizontalHeader().setVisible(True)
        self.ui.userTableWidget.setRowCount(len(rows))
        for row, cols in enumerate(rows):
            for col, text in enumerate(cols):
                if(col == 1):
                    if(text == 0):
                        text = "Usuario"
                    else:
                        text = "Operador"
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
        self.destroy()    
    
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

    # def tightLayoutCharts(self):
    #     if(self.graphicsLoaded):
    #         self.static_canvas.figure.tight_layout()
    #         self.dynamic_canvas.figure.tight_layout()
    #         self.static_canvas_pie.figure.tight_layout()
    #         self.static_canvas_lines.figure.tight_layout()

    def winFullscreen(self):
        global GLOBAL_FULLSCREEN
        global GLOBAL_STATE
        status = GLOBAL_FULLSCREEN
        if status == 0:
            self.showFullScreen()
            self.dashboardController.tightLayoutCharts()
            GLOBAL_FULLSCREEN = 1
            GLOBAL_STATE = 1
            self.ui.central_widget_layout.setContentsMargins(0,0,0,0)
            self.ui.frame_top_btns.setMaximumHeight(0)
            self.ui.frame_size_grip.hide()
        else:
            self.showNormal()
            self.dashboardController.tightLayoutCharts()
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
            self.dashboardController.tightLayoutCharts()
            GLOBAL_STATE = 1
            self.ui.central_widget_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.dashboardController.tightLayoutCharts()
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

    @Slot()
    def showConsoleMessage(self, message):
        self.ui.console.insertPlainText(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} >> {message}\r")

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
            port = int(self.ui.hostPortLineEdit.text())
            connectionThread = Thread(target = self.serverController.start_server, args= (host,port))
            connectionThread.daemon = True
            connectionThread.start()
            # server.start_server(host,hostPort, self)
        else:
            msgBox = QMessageBox()
            msgBox.setText("La dirección del servidor o el puerto de red no puede estar vacío.")
            msgBox.exec_()

    def disconnectServer(self):
        self.serverController.stop_server()
        self.ui.connectBtn.setEnabled(True)

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
    @Slot()        
    def update_waveform(self, valuesList):
        self.graphicsController.update_waveform(valuesList)

    @Slot()
    def update_fft(self, values):
        self.graphicsController.update_fft(values)

    @Slot()
    def update_spectrogram(self, values):
        self.graphicsController.update_spectrogram_data(values)

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


