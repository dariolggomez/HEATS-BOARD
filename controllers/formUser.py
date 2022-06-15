import email
from PySide2.QtWidgets import QDialog
from visuals.ui_formUser import Ui_Form
import services.user_service as user_service


class FormUser(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.acceptBtn.clicked.connect(self.createUser())
        self.ui.cancelBtn.clicked.connect(self.close())

    def createUser(self):
        username = self.ui.usernameLineEdit.text()
        email = self.ui.emailLineEdit.text()
        user_service.create_user(username, email)

