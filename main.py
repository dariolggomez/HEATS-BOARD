import sys
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from controllers.mainwindow import MainWindow
from services import user_service

# print(sys.path)
if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    # user_service.create_user("New UserTest6", "newusertest6@mail.com")
    window.show()
    window.activateWindow()
    window.raise_()
    sys.exit(app.exec_())