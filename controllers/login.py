from PySide2.QtWidgets import QWidget
from visuals.ui_login import Ui_Login


class Login(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        login = Ui_Login()
        login.setupUi(self)
        login.cancel_button.clicked.connect(self.close)