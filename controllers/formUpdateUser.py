import email
from unittest import result
from urllib import request
from PySide2.QtWidgets import QDialog, QMessageBox
from visuals.ui_formUser import Ui_Dialog
from PySide2.QtCore import Signal, Qt
import services.user_service as user_service
from validator import validate

class FormUpdateUser(QDialog):
    userUpdatedSignal = Signal()
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.acceptBtn.clicked.connect(lambda: self.updateUser(parent))
        self.ui.cancelBtn.clicked.connect(lambda: self.close())
        self.userUpdatedSignal.connect(parent.loadUserTable)

    def updateUser(self, parent):
        username = self.ui.usernameLineEdit.text()
        email = self.ui.emailLineEdit.text()
        item = parent.ui.userTableWidget.currentItem()
        user = item.data(Qt.UserRole+1)

        request = {"username": username,
                   "email": email}

        rules = {"username": "required|min:3",
                "email": "required|mail"}

        result, _, errors  = validate(request, rules, return_info=True)
        print(username)
        print(user.username)
        print(email)
        print(user.email)
        if(username != user.username):
            if(not user_service.checkUsernameExist(username)):
                if(email != user.email):
                    if(not user_service.checkEmailExist(email)):
                        if(result):
                            user.username = username
                            user.email = email
                            user_service.update_user(user)
                            self.userUpdatedSignal.emit()
                            self.close()
                        else:
                            print(str(errors))
                    else:
                        msgBox = QMessageBox()
                        msgBox.setText("Ya existe un usuario con ese email.")
                        msgBox.exec_()
                else:
                    if(result):
                        user.username = username
                        user.email = email
                        user_service.update_user(user)
                        self.userUpdatedSignal.emit()
                        self.close()
                    else:
                        print(str(errors))
            else:
                msgBox = QMessageBox()
                msgBox.setText("Ya existe ese nombre de usuario.")
                msgBox.exec_()        
        else:
            if(email != user.email):
                if(not user_service.checkEmailExist(email)):
                    if(result):
                        user.username = username
                        user.email = email
                        user_service.update_user(user)
                        self.userUpdatedSignal.emit()
                        self.close()
                    else:
                        print(str(errors))
                else:
                    msgBox = QMessageBox()
                    msgBox.setText("Ya existe un usuario con ese email.")
                    msgBox.exec_()
            else:
                self.close()

            
        
    def setLinesEditsValues(self, user):
        self.ui.usernameLineEdit.setText(user.username)
        self.ui.emailLineEdit.setText(user.email)
