# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loginBpKiMa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(500, 350)
        Login.setMinimumSize(QSize(350, 300))
        Login.setMaximumSize(QSize(500, 350))
        Login.setStyleSheet(u"background-color: rgb(24, 26, 33);")
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bg = QFrame(Login)
        self.bg.setObjectName(u"bg")
        self.bg.setStyleSheet(u"/* LINE EDIT */\n"
"background-color: rgb(24, 26, 33);\n"
"color: rgb(85, 170, 255);\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    bor"
                        "der: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollB"
                        "ar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid"
                        " rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repe"
                        "at: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover "
                        "{\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bg)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.inputs_frame = QFrame(self.bg)
        self.inputs_frame.setObjectName(u"inputs_frame")
        self.inputs_frame.setMinimumSize(QSize(0, 0))
        self.inputs_frame.setFrameShape(QFrame.StyledPanel)
        self.inputs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.inputs_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_user = QLabel(self.inputs_frame)
        self.label_user.setObjectName(u"label_user")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_user.setFont(font)

        self.verticalLayout_2.addWidget(self.label_user)

        self.user_lineEdit = QLineEdit(self.inputs_frame)
        self.user_lineEdit.setObjectName(u"user_lineEdit")
        self.user_lineEdit.setMinimumSize(QSize(0, 40))
        self.user_lineEdit.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.user_lineEdit.setFont(font1)
        self.user_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(50, 53, 60);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color: rgb(235, 235, 235);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_2.addWidget(self.user_lineEdit)

        self.label_password = QLabel(self.inputs_frame)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font)

        self.verticalLayout_2.addWidget(self.label_password)

        self.password_lineEdit = QLineEdit(self.inputs_frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMinimumSize(QSize(0, 40))
        self.password_lineEdit.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(10)
        self.password_lineEdit.setFont(font2)
        self.password_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(50, 53, 60);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	color: rgb(235, 235, 235);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_lineEdit)


        self.verticalLayout_3.addWidget(self.inputs_frame)

        self.buttons_frame = QFrame(self.bg)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.accept_button = QPushButton(self.buttons_frame)
        self.accept_button.setObjectName(u"accept_button")
        self.accept_button.setMinimumSize(QSize(180, 50))
        self.accept_button.setMaximumSize(QSize(180, 50))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.accept_button.setFont(font3)
        self.accept_button.setFocusPolicy(Qt.NoFocus)
        self.accept_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(23, 145, 239);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(23, 145, 239);\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 155, 249);\n"
"	border: 2px solid rgb(23, 145, 239);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(38, 159, 254);\n"
"	border: 2px solid rgb(38, 159, 254);\n"
"}")

        self.horizontalLayout.addWidget(self.accept_button, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.buttons_frame)


        self.verticalLayout.addWidget(self.bg)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"HEATS-BOARD", None))
        self.label_user.setText(QCoreApplication.translate("Login", u"Usuario", None))
        self.label_password.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
        self.accept_button.setText(QCoreApplication.translate("Login", u"Iniciar sesi\u00f3n", None))
#if QT_CONFIG(shortcut)
        self.accept_button.setShortcut(QCoreApplication.translate("Login", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

