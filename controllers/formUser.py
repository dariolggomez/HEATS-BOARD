import email
from unittest import result
from urllib import request
from PySide2.QtWidgets import QDialog, QMessageBox
from visuals.ui_formUser import Ui_Dialog
from PySide2.QtCore import Signal
import services.user_service as user_service
from validator import validate
import hashlib

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
        role = self.ui.comboBox.currentIndex()

        request = {"username": username,
                   "password": password,
                   "email": email}

        rules = {"username": "required|min:3",
                 "password": "required|min:4",
                "email": "required|mail"}

        result, _, errors  = validate(request, rules, return_info=True)
        if(result):
            if(not user_service.checkUsernameExist(username)):
                if(not user_service.checkEmailExist(email)):
                    passwordEncrypted = hashlib.sha256(password.encode()).hexdigest()
                    user_service.create_user(username, passwordEncrypted, email, role)
                    self.userCreatedSignal.emit()
                    self.close()
                else:
                    msg = QMessageBox()
                    msg.setText("Ya existe ese email.")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setText("Ya existe ese nombre de usuario.")
                msg.exec_()
        else:
            print(str(errors))
            if("username" in errors):
                if("Required" in errors["username"]):
                    msg = QMessageBox()
                    msg.setText("Nombre de usuario requerido.")
                    msg.exec_()
                else:    
                    if("Min" in errors["username"]):
                        msg = QMessageBox()
                        msg.setText("El nombre de usuario debe tener al menos 3 caracteres.")
                        msg.exec_()
            else:
                if("email" in errors):
                    if("Required" in errors["email"]):
                        msg = QMessageBox()
                        msg.setText("Email requerido.")
                        msg.exec_()
                    else:
                        if("Mail" in errors["email"]):
                            msg = QMessageBox()
                            msg.setText("El email debe tener un formato correcto, ejemplo: usuario@mail.com")
                            msg.exec_()
                else:
                    if("password" in errors):
                        if("Required" in errors["password"]):
                            msg = QMessageBox()
                            msg.setText("Contraseña requerida.")
                            msg.exec_()
                        else:
                            if("Min" in errors["password"]):
                                msg = QMessageBox()
                                msg.setText("La contraseña debe tener al menos 4 caracteres.")
                                msg.exec_()


        
