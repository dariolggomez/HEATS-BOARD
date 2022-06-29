from PySide2.QtWidgets import QWidget, QMessageBox
from visuals.ui_login import Ui_Login
from services import user_service
from controllers.mainwindow import MainWindow



class Login(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.accept_button.clicked.connect(self.authenticate)

    def authenticate(self):
        username = self.ui.user_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        user = user_service.read_byUsername(username)
        if(user and user.password == password):
            mainwindow = MainWindow()
            self.close()
            mainwindow.show()
            mainwindow.activateWindow()
            mainwindow.raise_()
        else:
            msg = QMessageBox()
            msg.setText("Nombre de usuario o contraseña incorrecto.")
            msg.exec_()
