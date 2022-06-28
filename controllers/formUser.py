import email
from unittest import result
from urllib import request
from PySide2.QtWidgets import QDialog
from visuals.ui_formUser import Ui_Dialog
from PySide2.QtCore import Signal
import services.user_service as user_service
from validator import validate

class FormUser(QDialog):
    userCreatedSignal = Signal()
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.acceptBtn.clicked.connect(self.createUser)
        self.ui.cancelBtn.clicked.connect(lambda: self.close())
        self.userCreatedSignal.connect(parent.loadUserTable)

    def createUser(self):
        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        email = self.ui.emailLineEdit.text()

        request = {"username": username,
                   "password": password,
                   "email": email}

        rules = {"username": "required|min:3",
                 "password": "required|min:4",
                "email": "required|mail"}

        result, _, errors  = validate(request, rules, return_info=True)
        if(result and not user_service.checkUsernameExist(username) and not user_service.checkEmailExist(email)):
            user_service.create_user(username, password, email)
            self.userCreatedSignal.emit()
            self.close()
        else:
            print(str(errors))
        
