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
        email = self.ui.emailLineEdit.text()

        request = {"username": username,
                   "email": email}

        rules = {"username": "required|min:3",
                "email": "required|mail"}

        result, _, errors  = validate(request, rules, return_info=True)
        if(result and not user_service.checkUsernameExist(username) and not user_service.checkEmailExist(email)):
            user_service.create_user(username, email)
            self.userCreatedSignal.emit()
            self.close()
        else:
            print(str(errors))
        
    def setLinesEditsValues(self, user):
        self.ui.usernameLineEdit.setText(user.username)
        self.ui.emailLineEdit.setText(user.email)
