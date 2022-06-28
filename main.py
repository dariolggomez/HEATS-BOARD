import sys
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from controllers.login import Login
from services import user_service

if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    # window = MainWindow()
    # window.show()
    # window.activateWindow()
    # window.raise_()
    login = Login()
    login.show()
    login.activateWindow()
    login.raise_()
    sys.exit(app.exec_())