# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formUseruBcSxV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(459, 390)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bg = QFrame(Form)
        self.bg.setObjectName(u"bg")
        self.bg.setStyleSheet(u"")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.contentFrame = QFrame(self.bg)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setStyleSheet(u"")
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.contentFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.contentFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 104, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.contentFrame)

        self.btnsFrame = QFrame(self.bg)
        self.btnsFrame.setObjectName(u"btnsFrame")
        self.btnsFrame.setMinimumSize(QSize(0, 50))
        self.btnsFrame.setMaximumSize(QSize(16777215, 50))
        self.btnsFrame.setStyleSheet(u"")
        self.btnsFrame.setFrameShape(QFrame.StyledPanel)
        self.btnsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.btnsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.applyBtn = QPushButton(self.btnsFrame)
        self.applyBtn.setObjectName(u"applyBtn")

        self.horizontalLayout.addWidget(self.applyBtn)

        self.acceptBtn = QPushButton(self.btnsFrame)
        self.acceptBtn.setObjectName(u"acceptBtn")

        self.horizontalLayout.addWidget(self.acceptBtn)

        self.cancelBtn = QPushButton(self.btnsFrame)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout_2.addWidget(self.btnsFrame)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.bg)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre de Usuario", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Email", None))
        self.applyBtn.setText(QCoreApplication.translate("Form", u"Aplicar", None))
        self.acceptBtn.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.cancelBtn.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

