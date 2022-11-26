# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASEOPLcqs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 718)
        MainWindow.setMinimumSize(QSize(750, 550))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.central_widget_layout = QVBoxLayout(self.centralwidget)
        self.central_widget_layout.setSpacing(0)
        self.central_widget_layout.setObjectName(u"central_widget_layout")
        self.central_widget_layout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
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
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
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
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
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
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
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
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
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
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
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
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-screen-desktop.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(180, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_fullscreen = QPushButton(self.frame_btns_right)
        self.btn_fullscreen.setObjectName(u"btn_fullscreen")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_fullscreen.sizePolicy().hasHeightForWidth())
        self.btn_fullscreen.setSizePolicy(sizePolicy2)
        self.btn_fullscreen.setMinimumSize(QSize(40, 0))
        self.btn_fullscreen.setMaximumSize(QSize(40, 16777215))
        self.btn_fullscreen.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/20x20/icons/20x20/cil-fullscreen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fullscreen.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_fullscreen)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy3)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy3.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy3)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy3.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy3)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 60, 63);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMinimumSize(QSize(0, 20))
        self.label_top_info_1.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")
        self.label_top_info_1.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(210, 44, 65);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy4)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy4.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy4)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy5)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
"/*background-color: rgb(255, 255, 255);*/\n"
"color: rgb(210, 210, 210);")
        self.page_nodes_centre = QWidget()
        self.page_nodes_centre.setObjectName(u"page_nodes_centre")
        self.verticalLayout_26 = QVBoxLayout(self.page_nodes_centre)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(12, 0, 12, 0)
        self.nodes_centre_content = QFrame(self.page_nodes_centre)
        self.nodes_centre_content.setObjectName(u"nodes_centre_content")
        self.nodes_centre_content.setFrameShape(QFrame.NoFrame)
        self.nodes_centre_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.nodes_centre_content)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.top_nodes_centre_content = QFrame(self.nodes_centre_content)
        self.top_nodes_centre_content.setObjectName(u"top_nodes_centre_content")
        self.top_nodes_centre_content.setMaximumSize(QSize(16777215, 30))
        self.top_nodes_centre_content.setFrameShape(QFrame.NoFrame)
        self.top_nodes_centre_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.top_nodes_centre_content)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.nodes_connected_label = QLabel(self.top_nodes_centre_content)
        self.nodes_connected_label.setObjectName(u"nodes_connected_label")
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.nodes_connected_label.setFont(font5)

        self.horizontalLayout_13.addWidget(self.nodes_connected_label)


        self.verticalLayout_30.addWidget(self.top_nodes_centre_content)

        self.bottom_nodes_centre_content = QFrame(self.nodes_centre_content)
        self.bottom_nodes_centre_content.setObjectName(u"bottom_nodes_centre_content")
        self.bottom_nodes_centre_content.setFrameShape(QFrame.NoFrame)
        self.bottom_nodes_centre_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.bottom_nodes_centre_content)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.nodes_graphic_frame = QFrame(self.bottom_nodes_centre_content)
        self.nodes_graphic_frame.setObjectName(u"nodes_graphic_frame")
        self.nodes_graphic_frame.setFrameShape(QFrame.NoFrame)
        self.nodes_graphic_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.nodes_graphic_frame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.nodes_graphic_layout = QVBoxLayout()
        self.nodes_graphic_layout.setObjectName(u"nodes_graphic_layout")

        self.verticalLayout_32.addLayout(self.nodes_graphic_layout)


        self.horizontalLayout_12.addWidget(self.nodes_graphic_frame)

        self.nodes_tables_frame = QFrame(self.bottom_nodes_centre_content)
        self.nodes_tables_frame.setObjectName(u"nodes_tables_frame")
        self.nodes_tables_frame.setFrameShape(QFrame.StyledPanel)
        self.nodes_tables_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.nodes_tables_frame)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_net_nodes = QFrame(self.nodes_tables_frame)
        self.frame_net_nodes.setObjectName(u"frame_net_nodes")
        self.frame_net_nodes.setFrameShape(QFrame.NoFrame)
        self.frame_net_nodes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_net_nodes)
        self.verticalLayout_33.setSpacing(4)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_net_nodes)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 25))
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_33.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.netNodeStatusTable = QTableWidget(self.frame_net_nodes)
        self.netNodeStatusTable.setObjectName(u"netNodeStatusTable")
        self.netNodeStatusTable.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.netNodeStatusTable.sizePolicy().hasHeightForWidth())
        self.netNodeStatusTable.setSizePolicy(sizePolicy4)
        self.netNodeStatusTable.setMaximumSize(QSize(99999, 1000))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(30, 30, 30, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.netNodeStatusTable.setPalette(palette1)
        self.netNodeStatusTable.setFocusPolicy(Qt.NoFocus)
        self.netNodeStatusTable.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(30, 30, 30);\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	/*border-bottom: 1px solid rgb(44, 49, 60);*/\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(50, 50, 51);\n"
"	color: rgb(219, 219, 219);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
""
                        "    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(30,30,30);\n"
"	background-color: rgb(0, 122, 204);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0, 122, 204);\n"
"}\n"
"")
        self.netNodeStatusTable.setFrameShape(QFrame.NoFrame)
        self.netNodeStatusTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.netNodeStatusTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.netNodeStatusTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.netNodeStatusTable.setAutoScroll(True)
        self.netNodeStatusTable.setAutoScrollMargin(16)
        self.netNodeStatusTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.netNodeStatusTable.setAlternatingRowColors(False)
        self.netNodeStatusTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.netNodeStatusTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.netNodeStatusTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.netNodeStatusTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.netNodeStatusTable.setShowGrid(True)
        self.netNodeStatusTable.setGridStyle(Qt.SolidLine)
        self.netNodeStatusTable.setSortingEnabled(False)
        self.netNodeStatusTable.setWordWrap(True)
        self.netNodeStatusTable.setRowCount(0)
        self.netNodeStatusTable.horizontalHeader().setVisible(False)
        self.netNodeStatusTable.horizontalHeader().setCascadingSectionResizes(False)
        self.netNodeStatusTable.horizontalHeader().setDefaultSectionSize(200)
        self.netNodeStatusTable.horizontalHeader().setStretchLastSection(True)
        self.netNodeStatusTable.verticalHeader().setVisible(False)
        self.netNodeStatusTable.verticalHeader().setCascadingSectionResizes(False)
        self.netNodeStatusTable.verticalHeader().setMinimumSectionSize(30)
        self.netNodeStatusTable.verticalHeader().setDefaultSectionSize(30)
        self.netNodeStatusTable.verticalHeader().setHighlightSections(False)
        self.netNodeStatusTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_33.addWidget(self.netNodeStatusTable)


        self.verticalLayout_27.addWidget(self.frame_net_nodes)

        self.frame_rt_nodes = QFrame(self.nodes_tables_frame)
        self.frame_rt_nodes.setObjectName(u"frame_rt_nodes")
        self.frame_rt_nodes.setFrameShape(QFrame.NoFrame)
        self.frame_rt_nodes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_rt_nodes)
        self.verticalLayout_36.setSpacing(4)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_rt_nodes)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 25))
        self.label_8.setFont(font5)
        self.label_8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_36.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.rtNodeStatusTable = QTableWidget(self.frame_rt_nodes)
        self.rtNodeStatusTable.setObjectName(u"rtNodeStatusTable")
        self.rtNodeStatusTable.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.rtNodeStatusTable.sizePolicy().hasHeightForWidth())
        self.rtNodeStatusTable.setSizePolicy(sizePolicy4)
        self.rtNodeStatusTable.setMaximumSize(QSize(99999, 1000))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush19 = QBrush(QColor(210, 210, 210, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush20 = QBrush(QColor(210, 210, 210, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush21 = QBrush(QColor(210, 210, 210, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.rtNodeStatusTable.setPalette(palette2)
        self.rtNodeStatusTable.setFocusPolicy(Qt.NoFocus)
        self.rtNodeStatusTable.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(30, 30, 30);\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	/*border-bottom: 1px solid rgb(44, 49, 60);*/\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(50, 50, 51);\n"
"	color: rgb(219, 219, 219);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
""
                        "    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(30,30,30);\n"
"	background-color: rgb(0, 122, 204);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0, 122, 204);\n"
"}\n"
"")
        self.rtNodeStatusTable.setFrameShape(QFrame.NoFrame)
        self.rtNodeStatusTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.rtNodeStatusTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.rtNodeStatusTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.rtNodeStatusTable.setAutoScroll(True)
        self.rtNodeStatusTable.setAutoScrollMargin(16)
        self.rtNodeStatusTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.rtNodeStatusTable.setAlternatingRowColors(False)
        self.rtNodeStatusTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.rtNodeStatusTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.rtNodeStatusTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.rtNodeStatusTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.rtNodeStatusTable.setShowGrid(True)
        self.rtNodeStatusTable.setGridStyle(Qt.SolidLine)
        self.rtNodeStatusTable.setSortingEnabled(False)
        self.rtNodeStatusTable.setWordWrap(True)
        self.rtNodeStatusTable.setRowCount(0)
        self.rtNodeStatusTable.horizontalHeader().setVisible(False)
        self.rtNodeStatusTable.horizontalHeader().setCascadingSectionResizes(False)
        self.rtNodeStatusTable.horizontalHeader().setDefaultSectionSize(200)
        self.rtNodeStatusTable.horizontalHeader().setStretchLastSection(True)
        self.rtNodeStatusTable.verticalHeader().setVisible(False)
        self.rtNodeStatusTable.verticalHeader().setCascadingSectionResizes(False)
        self.rtNodeStatusTable.verticalHeader().setMinimumSectionSize(30)
        self.rtNodeStatusTable.verticalHeader().setDefaultSectionSize(30)
        self.rtNodeStatusTable.verticalHeader().setHighlightSections(False)
        self.rtNodeStatusTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_36.addWidget(self.rtNodeStatusTable)


        self.verticalLayout_27.addWidget(self.frame_rt_nodes)


        self.horizontalLayout_12.addWidget(self.nodes_tables_frame)


        self.verticalLayout_30.addWidget(self.bottom_nodes_centre_content)


        self.verticalLayout_26.addWidget(self.nodes_centre_content)

        self.stackedWidget.addWidget(self.page_nodes_centre)
        self.page_info_panel = QWidget()
        self.page_info_panel.setObjectName(u"page_info_panel")
        self.verticalLayout_38 = QVBoxLayout(self.page_info_panel)
        self.verticalLayout_38.setSpacing(8)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(9, 0, 9, 0)
        self.panel_top_menu = QFrame(self.page_info_panel)
        self.panel_top_menu.setObjectName(u"panel_top_menu")
        self.panel_top_menu.setMinimumSize(QSize(0, 50))
        self.panel_top_menu.setMaximumSize(QSize(16777215, 50))
        self.panel_top_menu.setStyleSheet(u"")
        self.panel_top_menu.setFrameShape(QFrame.NoFrame)
        self.panel_top_menu.setFrameShadow(QFrame.Raised)
        self.panel_top_menu.setLineWidth(1)
        self.panel_top_layout = QHBoxLayout(self.panel_top_menu)
        self.panel_top_layout.setSpacing(8)
        self.panel_top_layout.setObjectName(u"panel_top_layout")
        self.panel_top_layout.setContentsMargins(4, 4, 4, 4)

        self.verticalLayout_38.addWidget(self.panel_top_menu, 0, Qt.AlignLeft)

        self.frame_panel_stacked_widget = QFrame(self.page_info_panel)
        self.frame_panel_stacked_widget.setObjectName(u"frame_panel_stacked_widget")
        self.frame_panel_stacked_widget.setStyleSheet(u"background-color: rgb(41, 45, 56);")
        self.frame_panel_stacked_widget.setFrameShape(QFrame.NoFrame)
        self.frame_panel_stacked_widget.setFrameShadow(QFrame.Raised)
        self.frame_panel_stacked_widget.setLineWidth(1)
        self.verticalLayout_10 = QVBoxLayout(self.frame_panel_stacked_widget)
        self.verticalLayout_10.setSpacing(8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(12, 12, 12, 12)
        self.panel_stacked_widget = QStackedWidget(self.frame_panel_stacked_widget)
        self.panel_stacked_widget.setObjectName(u"panel_stacked_widget")
        self.page_poles = QWidget()
        self.page_poles.setObjectName(u"page_poles")
        self.verticalLayout_37 = QVBoxLayout(self.page_poles)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.panel_content_frame = QFrame(self.page_poles)
        self.panel_content_frame.setObjectName(u"panel_content_frame")
        self.panel_content_frame.setFrameShape(QFrame.NoFrame)
        self.panel_content_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.panel_content_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.maxAmpFrame = QFrame(self.panel_content_frame)
        self.maxAmpFrame.setObjectName(u"maxAmpFrame")
        self.maxAmpFrame.setMinimumSize(QSize(420, 0))
        self.maxAmpFrame.setStyleSheet(u"border-color: rgb(47, 47, 47);\n"
"border-radius: 5px")
        self.maxAmpFrame.setFrameShape(QFrame.StyledPanel)
        self.maxAmpFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.maxAmpFrame)
        self.verticalLayout_17.setSpacing(4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.maxAmpFrame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font5)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_17.addWidget(self.label)

        self.maxAmplitudeTable = QTableWidget(self.maxAmpFrame)
        self.maxAmplitudeTable.setObjectName(u"maxAmplitudeTable")
        self.maxAmplitudeTable.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.maxAmplitudeTable.sizePolicy().hasHeightForWidth())
        self.maxAmplitudeTable.setSizePolicy(sizePolicy4)
        self.maxAmplitudeTable.setMaximumSize(QSize(99999, 1000))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush22 = QBrush(QColor(210, 210, 210, 128))
        brush22.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush23 = QBrush(QColor(210, 210, 210, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush23)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush24 = QBrush(QColor(210, 210, 210, 128))
        brush24.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
#endif
        self.maxAmplitudeTable.setPalette(palette3)
        self.maxAmplitudeTable.setFocusPolicy(Qt.NoFocus)
        self.maxAmplitudeTable.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(30, 30, 30);\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	/*border-bottom: 1px solid rgb(44, 49, 60);*/\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(50, 50, 51);\n"
"	color: rgb(219, 219, 219);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
""
                        "    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(30,30,30);\n"
"	background-color: rgb(0, 122, 204);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0, 122, 204);\n"
"}\n"
"")
        self.maxAmplitudeTable.setFrameShape(QFrame.NoFrame)
        self.maxAmplitudeTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.maxAmplitudeTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.maxAmplitudeTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.maxAmplitudeTable.setAutoScroll(True)
        self.maxAmplitudeTable.setAutoScrollMargin(16)
        self.maxAmplitudeTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.maxAmplitudeTable.setAlternatingRowColors(False)
        self.maxAmplitudeTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.maxAmplitudeTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.maxAmplitudeTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.maxAmplitudeTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.maxAmplitudeTable.setShowGrid(True)
        self.maxAmplitudeTable.setGridStyle(Qt.SolidLine)
        self.maxAmplitudeTable.setSortingEnabled(False)
        self.maxAmplitudeTable.setWordWrap(True)
        self.maxAmplitudeTable.setRowCount(0)
        self.maxAmplitudeTable.horizontalHeader().setVisible(False)
        self.maxAmplitudeTable.horizontalHeader().setCascadingSectionResizes(False)
        self.maxAmplitudeTable.horizontalHeader().setDefaultSectionSize(200)
        self.maxAmplitudeTable.horizontalHeader().setStretchLastSection(True)
        self.maxAmplitudeTable.verticalHeader().setVisible(False)
        self.maxAmplitudeTable.verticalHeader().setCascadingSectionResizes(False)
        self.maxAmplitudeTable.verticalHeader().setMinimumSectionSize(30)
        self.maxAmplitudeTable.verticalHeader().setDefaultSectionSize(30)
        self.maxAmplitudeTable.verticalHeader().setHighlightSections(False)
        self.maxAmplitudeTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_17.addWidget(self.maxAmplitudeTable)


        self.gridLayout.addWidget(self.maxAmpFrame, 0, 0, 1, 1)

        self.maxAmpDistFrame = QFrame(self.panel_content_frame)
        self.maxAmpDistFrame.setObjectName(u"maxAmpDistFrame")
        self.maxAmpDistFrame.setFrameShape(QFrame.StyledPanel)
        self.maxAmpDistFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.maxAmpDistFrame)
        self.verticalLayout_18.setSpacing(4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.maxAmpDistFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font5)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_18.addWidget(self.label_2)

        self.maxAmpHistLayout = QVBoxLayout()
        self.maxAmpHistLayout.setObjectName(u"maxAmpHistLayout")

        self.verticalLayout_18.addLayout(self.maxAmpHistLayout)

        self.frameBottomMaxDist = QFrame(self.maxAmpDistFrame)
        self.frameBottomMaxDist.setObjectName(u"frameBottomMaxDist")
        self.frameBottomMaxDist.setMaximumSize(QSize(16777215, 50))
        self.frameBottomMaxDist.setFrameShape(QFrame.StyledPanel)
        self.frameBottomMaxDist.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frameBottomMaxDist)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(317, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)

        self.label_5 = QLabel(self.frameBottomMaxDist)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_5.setFont(font6)

        self.horizontalLayout_15.addWidget(self.label_5)

        self.maxAmpDistSpinBox = QSpinBox(self.frameBottomMaxDist)
        self.maxAmpDistSpinBox.setObjectName(u"maxAmpDistSpinBox")
        self.maxAmpDistSpinBox.setMaximumSize(QSize(50, 16777215))
        self.maxAmpDistSpinBox.setMinimum(1)
        self.maxAmpDistSpinBox.setMaximum(50)
        self.maxAmpDistSpinBox.setValue(10)

        self.horizontalLayout_15.addWidget(self.maxAmpDistSpinBox)


        self.verticalLayout_18.addWidget(self.frameBottomMaxDist)


        self.gridLayout.addWidget(self.maxAmpDistFrame, 0, 1, 1, 1)

        self.minAmpFrame = QFrame(self.panel_content_frame)
        self.minAmpFrame.setObjectName(u"minAmpFrame")
        self.minAmpFrame.setStyleSheet(u"border-color: rgb(47, 47, 47);\n"
"border-radius: 5px 5px")
        self.minAmpFrame.setFrameShape(QFrame.StyledPanel)
        self.minAmpFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.minAmpFrame)
        self.verticalLayout_19.setSpacing(4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.minAmpFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_19.addWidget(self.label_3)

        self.minAmplitudeTable = QTableWidget(self.minAmpFrame)
        self.minAmplitudeTable.setObjectName(u"minAmplitudeTable")
        self.minAmplitudeTable.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.minAmplitudeTable.sizePolicy().hasHeightForWidth())
        self.minAmplitudeTable.setSizePolicy(sizePolicy4)
        self.minAmplitudeTable.setMaximumSize(QSize(99999, 1000))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush25 = QBrush(QColor(210, 210, 210, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush25)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush26 = QBrush(QColor(210, 210, 210, 128))
        brush26.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush26)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush27 = QBrush(QColor(210, 210, 210, 128))
        brush27.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.minAmplitudeTable.setPalette(palette4)
        self.minAmplitudeTable.setFocusPolicy(Qt.NoFocus)
        self.minAmplitudeTable.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(30, 30, 30);\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	/*border-bottom: 1px solid rgb(44, 49, 60);*/\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(50, 50, 51);\n"
"	color: rgb(219, 219, 219);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
""
                        "    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(30,30,30);\n"
"	background-color: rgb(0, 122, 204);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0, 122, 204);\n"
"}\n"
"")
        self.minAmplitudeTable.setFrameShape(QFrame.NoFrame)
        self.minAmplitudeTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.minAmplitudeTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.minAmplitudeTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.minAmplitudeTable.setAutoScroll(True)
        self.minAmplitudeTable.setAutoScrollMargin(16)
        self.minAmplitudeTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.minAmplitudeTable.setAlternatingRowColors(False)
        self.minAmplitudeTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.minAmplitudeTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.minAmplitudeTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.minAmplitudeTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.minAmplitudeTable.setShowGrid(True)
        self.minAmplitudeTable.setGridStyle(Qt.SolidLine)
        self.minAmplitudeTable.setSortingEnabled(False)
        self.minAmplitudeTable.setWordWrap(True)
        self.minAmplitudeTable.setRowCount(0)
        self.minAmplitudeTable.horizontalHeader().setVisible(False)
        self.minAmplitudeTable.horizontalHeader().setCascadingSectionResizes(False)
        self.minAmplitudeTable.horizontalHeader().setDefaultSectionSize(200)
        self.minAmplitudeTable.horizontalHeader().setStretchLastSection(True)
        self.minAmplitudeTable.verticalHeader().setVisible(False)
        self.minAmplitudeTable.verticalHeader().setCascadingSectionResizes(False)
        self.minAmplitudeTable.verticalHeader().setMinimumSectionSize(30)
        self.minAmplitudeTable.verticalHeader().setDefaultSectionSize(30)
        self.minAmplitudeTable.verticalHeader().setHighlightSections(False)
        self.minAmplitudeTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_19.addWidget(self.minAmplitudeTable)


        self.gridLayout.addWidget(self.minAmpFrame, 1, 0, 1, 1)

        self.minAmpDistFrame = QFrame(self.panel_content_frame)
        self.minAmpDistFrame.setObjectName(u"minAmpDistFrame")
        self.minAmpDistFrame.setFrameShape(QFrame.NoFrame)
        self.minAmpDistFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.minAmpDistFrame)
        self.verticalLayout_20.setSpacing(4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.minAmpDistFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_20.addWidget(self.label_4)

        self.minAmpHistLayout = QVBoxLayout()
        self.minAmpHistLayout.setObjectName(u"minAmpHistLayout")

        self.verticalLayout_20.addLayout(self.minAmpHistLayout)

        self.frameBottomMinDist = QFrame(self.minAmpDistFrame)
        self.frameBottomMinDist.setObjectName(u"frameBottomMinDist")
        self.frameBottomMinDist.setMaximumSize(QSize(16777215, 50))
        self.frameBottomMinDist.setFrameShape(QFrame.StyledPanel)
        self.frameBottomMinDist.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frameBottomMinDist)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(317, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.label_6 = QLabel(self.frameBottomMinDist)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setFont(font6)

        self.horizontalLayout_16.addWidget(self.label_6)

        self.minAmpDistSpinBox = QSpinBox(self.frameBottomMinDist)
        self.minAmpDistSpinBox.setObjectName(u"minAmpDistSpinBox")
        self.minAmpDistSpinBox.setMaximumSize(QSize(50, 16777215))
        self.minAmpDistSpinBox.setMinimum(1)
        self.minAmpDistSpinBox.setMaximum(50)
        self.minAmpDistSpinBox.setValue(10)

        self.horizontalLayout_16.addWidget(self.minAmpDistSpinBox)


        self.verticalLayout_20.addWidget(self.frameBottomMinDist)


        self.gridLayout.addWidget(self.minAmpDistFrame, 1, 1, 1, 1)


        self.verticalLayout_37.addWidget(self.panel_content_frame)

        self.panel_stacked_widget.addWidget(self.page_poles)
        self.page_threshold = QWidget()
        self.page_threshold.setObjectName(u"page_threshold")
        self.verticalLayout_39 = QVBoxLayout(self.page_threshold)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.threshold_content = QFrame(self.page_threshold)
        self.threshold_content.setObjectName(u"threshold_content")
        self.threshold_content.setFrameShape(QFrame.NoFrame)
        self.threshold_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.threshold_content)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_threshold_table = QFrame(self.threshold_content)
        self.frame_threshold_table.setObjectName(u"frame_threshold_table")
        self.frame_threshold_table.setFrameShape(QFrame.NoFrame)
        self.frame_threshold_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_threshold_table)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.threshold_table_label = QLabel(self.frame_threshold_table)
        self.threshold_table_label.setObjectName(u"threshold_table_label")
        self.threshold_table_label.setMaximumSize(QSize(16777215, 25))
        self.threshold_table_label.setFont(font5)

        self.verticalLayout_41.addWidget(self.threshold_table_label)

        self.threshold_table = QTableWidget(self.frame_threshold_table)
        self.threshold_table.setObjectName(u"threshold_table")
        self.threshold_table.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.threshold_table.sizePolicy().hasHeightForWidth())
        self.threshold_table.setSizePolicy(sizePolicy4)
        self.threshold_table.setMaximumSize(QSize(99999, 1000))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush28 = QBrush(QColor(210, 210, 210, 128))
        brush28.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush29 = QBrush(QColor(210, 210, 210, 128))
        brush29.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush29)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush30 = QBrush(QColor(210, 210, 210, 128))
        brush30.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush30)
#endif
        self.threshold_table.setPalette(palette5)
        self.threshold_table.setFocusPolicy(Qt.NoFocus)
        self.threshold_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(30, 30, 30);\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	/*border-bottom: 1px solid rgb(44, 49, 60);*/\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(50, 50, 51);\n"
"	color: rgb(219, 219, 219);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
""
                        "    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(30,30,30);\n"
"	background-color: rgb(0, 122, 204);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0, 122, 204);\n"
"}\n"
"")
        self.threshold_table.setFrameShape(QFrame.NoFrame)
        self.threshold_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.threshold_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.threshold_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.threshold_table.setAutoScroll(True)
        self.threshold_table.setAutoScrollMargin(16)
        self.threshold_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.threshold_table.setAlternatingRowColors(False)
        self.threshold_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.threshold_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.threshold_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.threshold_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.threshold_table.setShowGrid(True)
        self.threshold_table.setGridStyle(Qt.SolidLine)
        self.threshold_table.setSortingEnabled(False)
        self.threshold_table.setWordWrap(True)
        self.threshold_table.setRowCount(0)
        self.threshold_table.horizontalHeader().setVisible(False)
        self.threshold_table.horizontalHeader().setCascadingSectionResizes(False)
        self.threshold_table.horizontalHeader().setDefaultSectionSize(200)
        self.threshold_table.horizontalHeader().setStretchLastSection(True)
        self.threshold_table.verticalHeader().setVisible(False)
        self.threshold_table.verticalHeader().setCascadingSectionResizes(False)
        self.threshold_table.verticalHeader().setMinimumSectionSize(30)
        self.threshold_table.verticalHeader().setDefaultSectionSize(30)
        self.threshold_table.verticalHeader().setHighlightSections(False)
        self.threshold_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_41.addWidget(self.threshold_table)


        self.horizontalLayout_17.addWidget(self.frame_threshold_table)

        self.frame_threshold_config = QFrame(self.threshold_content)
        self.frame_threshold_config.setObjectName(u"frame_threshold_config")
        self.frame_threshold_config.setMinimumSize(QSize(250, 0))
        self.frame_threshold_config.setMaximumSize(QSize(250, 16777215))
        self.frame_threshold_config.setFrameShape(QFrame.StyledPanel)
        self.frame_threshold_config.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_threshold_config)
        self.verticalLayout_42.setSpacing(7)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.threshold_label = QLabel(self.frame_threshold_config)
        self.threshold_label.setObjectName(u"threshold_label")
        self.threshold_label.setMaximumSize(QSize(16777215, 25))
        self.threshold_label.setFont(font5)

        self.verticalLayout_42.addWidget(self.threshold_label)

        self.frame_threshold_cof_bg = QFrame(self.frame_threshold_config)
        self.frame_threshold_cof_bg.setObjectName(u"frame_threshold_cof_bg")
        self.frame_threshold_cof_bg.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"border-radius: 5px;")
        self.frame_threshold_cof_bg.setFrameShape(QFrame.StyledPanel)
        self.frame_threshold_cof_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_threshold_cof_bg)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(12, 12, 12, 12)
        self.frame_threshold_value = QFrame(self.frame_threshold_cof_bg)
        self.frame_threshold_value.setObjectName(u"frame_threshold_value")
        self.frame_threshold_value.setFrameShape(QFrame.StyledPanel)
        self.frame_threshold_value.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_threshold_value)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_threshold_ind = QLabel(self.frame_threshold_value)
        self.label_threshold_ind.setObjectName(u"label_threshold_ind")
        self.label_threshold_ind.setMaximumSize(QSize(16777215, 30))
        self.label_threshold_ind.setFont(font5)

        self.horizontalLayout_20.addWidget(self.label_threshold_ind)

        self.threshold_actual_value = QLabel(self.frame_threshold_value)
        self.threshold_actual_value.setObjectName(u"threshold_actual_value")
        self.threshold_actual_value.setMaximumSize(QSize(16777215, 30))
        self.threshold_actual_value.setFont(font5)

        self.horizontalLayout_20.addWidget(self.threshold_actual_value)


        self.verticalLayout_40.addWidget(self.frame_threshold_value)

        self.threshold_spin_box = QSpinBox(self.frame_threshold_cof_bg)
        self.threshold_spin_box.setObjectName(u"threshold_spin_box")
        font7 = QFont()
        font7.setFamily(u"Segoe UI Semibold")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.threshold_spin_box.setFont(font7)
        self.threshold_spin_box.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.threshold_spin_box.setMinimum(80)
        self.threshold_spin_box.setMaximum(160)
        self.threshold_spin_box.setValue(140)

        self.verticalLayout_40.addWidget(self.threshold_spin_box)

        self.apply_threshold_btn = QPushButton(self.frame_threshold_cof_bg)
        self.apply_threshold_btn.setObjectName(u"apply_threshold_btn")
        self.apply_threshold_btn.setMinimumSize(QSize(100, 30))
        self.apply_threshold_btn.setMaximumSize(QSize(85, 16777215))
        self.apply_threshold_btn.setFont(font7)
        self.apply_threshold_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.verticalLayout_40.addWidget(self.apply_threshold_btn, 0, Qt.AlignRight)


        self.verticalLayout_42.addWidget(self.frame_threshold_cof_bg, 0, Qt.AlignTop)


        self.horizontalLayout_17.addWidget(self.frame_threshold_config)


        self.verticalLayout_39.addWidget(self.threshold_content)

        self.panel_stacked_widget.addWidget(self.page_threshold)

        self.verticalLayout_10.addWidget(self.panel_stacked_widget)


        self.verticalLayout_38.addWidget(self.frame_panel_stacked_widget)

        self.stackedWidget.addWidget(self.page_info_panel)
        self.page_users = QWidget()
        self.page_users.setObjectName(u"page_users")
        self.verticalLayout_16 = QVBoxLayout(self.page_users)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.page_users)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.content)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_9 = QFrame(self.content)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.labelHeaderUser = QLabel(self.frame_9)
        self.labelHeaderUser.setObjectName(u"labelHeaderUser")
        self.labelHeaderUser.setMaximumSize(QSize(16777215, 25))
        self.labelHeaderUser.setFont(font1)
        self.labelHeaderUser.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.labelHeaderUser)

        self.userTableWidget = QTableWidget(self.frame_9)
        self.userTableWidget.setObjectName(u"userTableWidget")
        self.userTableWidget.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.userTableWidget.sizePolicy().hasHeightForWidth())
        self.userTableWidget.setSizePolicy(sizePolicy4)
        self.userTableWidget.setMaximumSize(QSize(99999, 1000))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush31 = QBrush(QColor(39, 44, 54, 255))
        brush31.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush31)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush31)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush31)
        brush32 = QBrush(QColor(210, 210, 210, 128))
        brush32.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush32)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush31)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush31)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush31)
        brush33 = QBrush(QColor(210, 210, 210, 128))
        brush33.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush33)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush31)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush31)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush31)
        brush34 = QBrush(QColor(210, 210, 210, 128))
        brush34.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush34)
#endif
        self.userTableWidget.setPalette(palette6)
        self.userTableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.userTableWidget.setFrameShape(QFrame.NoFrame)
        self.userTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.userTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.userTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.userTableWidget.setAutoScroll(True)
        self.userTableWidget.setAutoScrollMargin(16)
        self.userTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.userTableWidget.setAlternatingRowColors(False)
        self.userTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.userTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.userTableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.userTableWidget.setShowGrid(True)
        self.userTableWidget.setGridStyle(Qt.SolidLine)
        self.userTableWidget.setSortingEnabled(False)
        self.userTableWidget.setWordWrap(True)
        self.userTableWidget.setRowCount(0)
        self.userTableWidget.horizontalHeader().setVisible(False)
        self.userTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.userTableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.userTableWidget.horizontalHeader().setStretchLastSection(True)
        self.userTableWidget.verticalHeader().setVisible(False)
        self.userTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.userTableWidget.verticalHeader().setMinimumSectionSize(30)
        self.userTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.userTableWidget.verticalHeader().setHighlightSections(False)
        self.userTableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_13.addWidget(self.userTableWidget)

        self.verticalLayout_13.setStretch(0, 5)

        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.content)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(351, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editBtn = QPushButton(self.frame_10)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setMinimumSize(QSize(80, 30))
        font8 = QFont()
        font8.setPointSize(9)
        self.editBtn.setFont(font8)
        self.editBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout.addWidget(self.editBtn)

        self.createBtn = QPushButton(self.frame_10)
        self.createBtn.setObjectName(u"createBtn")
        self.createBtn.setMinimumSize(QSize(80, 30))
        self.createBtn.setFont(font8)
        self.createBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout.addWidget(self.createBtn)

        self.eliminateBtn = QPushButton(self.frame_10)
        self.eliminateBtn.setObjectName(u"eliminateBtn")
        self.eliminateBtn.setEnabled(True)
        self.eliminateBtn.setMinimumSize(QSize(80, 30))
        self.eliminateBtn.setFont(font8)
        self.eliminateBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout.addWidget(self.eliminateBtn)


        self.verticalLayout_12.addWidget(self.frame_10)


        self.verticalLayout_16.addWidget(self.content)

        self.stackedWidget.addWidget(self.page_users)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.labelBoxHeaderSettings = QLabel(self.frame_title_wid_1)
        self.labelBoxHeaderSettings.setObjectName(u"labelBoxHeaderSettings")
        self.labelBoxHeaderSettings.setMinimumSize(QSize(0, 20))
        self.labelBoxHeaderSettings.setMaximumSize(QSize(16777215, 25))
        self.labelBoxHeaderSettings.setFont(font1)
        self.labelBoxHeaderSettings.setStyleSheet(u"")
        self.labelBoxHeaderSettings.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.labelBoxHeaderSettings)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_settings_fullscreen = QPushButton(self.frame_content_wid_1)
        self.btn_settings_fullscreen.setObjectName(u"btn_settings_fullscreen")
        self.btn_settings_fullscreen.setMinimumSize(QSize(200, 30))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(9)
        self.btn_settings_fullscreen.setFont(font9)
        self.btn_settings_fullscreen.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_settings_fullscreen)

        self.backupCheckBox = QCheckBox(self.frame_content_wid_1)
        self.backupCheckBox.setObjectName(u"backupCheckBox")
        self.backupCheckBox.setAutoFillBackground(False)
        self.backupCheckBox.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.backupCheckBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_11.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_widgets)
        self.page_network = QWidget()
        self.page_network.setObjectName(u"page_network")
        self.verticalLayout_22 = QVBoxLayout(self.page_network)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.content_network = QFrame(self.page_network)
        self.content_network.setObjectName(u"content_network")
        self.content_network.setStyleSheet(u"")
        self.content_network.setFrameShape(QFrame.StyledPanel)
        self.content_network.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.content_network)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_network_1 = QFrame(self.content_network)
        self.frame_network_1.setObjectName(u"frame_network_1")
        self.frame_network_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.frame_network_1.setFrameShape(QFrame.StyledPanel)
        self.frame_network_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_network_1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.labelHeaderUser_2 = QLabel(self.frame_network_1)
        self.labelHeaderUser_2.setObjectName(u"labelHeaderUser_2")
        self.labelHeaderUser_2.setMaximumSize(QSize(16777215, 30))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setWeight(75)
        self.labelHeaderUser_2.setFont(font10)
        self.labelHeaderUser_2.setStyleSheet(u"")

        self.verticalLayout_24.addWidget(self.labelHeaderUser_2)

        self.frame_11 = QFrame(self.frame_network_1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_12)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.labelHeaderUser_3 = QLabel(self.frame_12)
        self.labelHeaderUser_3.setObjectName(u"labelHeaderUser_3")
        self.labelHeaderUser_3.setMaximumSize(QSize(16777215, 25))
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(9)
        font11.setBold(True)
        font11.setWeight(75)
        self.labelHeaderUser_3.setFont(font11)
        self.labelHeaderUser_3.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.labelHeaderUser_3)

        self.hostLineEdit = QLineEdit(self.frame_12)
        self.hostLineEdit.setObjectName(u"hostLineEdit")
        self.hostLineEdit.setStyleSheet(u"QLineEdit {\n"
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
"}")

        self.verticalLayout_21.addWidget(self.hostLineEdit)

        self.verticalSpacer = QSpacerItem(20, 331, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer)


        self.horizontalLayout_14.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_13)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.labelHeaderUser_4 = QLabel(self.frame_13)
        self.labelHeaderUser_4.setObjectName(u"labelHeaderUser_4")
        self.labelHeaderUser_4.setMaximumSize(QSize(16777215, 25))
        self.labelHeaderUser_4.setFont(font11)
        self.labelHeaderUser_4.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.labelHeaderUser_4)

        self.hostPortLineEdit = QLineEdit(self.frame_13)
        self.hostPortLineEdit.setObjectName(u"hostPortLineEdit")
        self.hostPortLineEdit.setStyleSheet(u"QLineEdit {\n"
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
"}")
        self.hostPortLineEdit.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_23.addWidget(self.hostPortLineEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 331, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_2)


        self.horizontalLayout_14.addWidget(self.frame_13)

        self.horizontalSpacer_3 = QSpacerItem(256, 38, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.verticalLayout_24.addWidget(self.frame_11)


        self.verticalLayout_14.addWidget(self.frame_network_1)

        self.frame_network_2 = QFrame(self.content_network)
        self.frame_network_2.setObjectName(u"frame_network_2")
        self.frame_network_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.frame_network_2.setFrameShape(QFrame.StyledPanel)
        self.frame_network_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_network_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(351, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.disconnectBtn = QPushButton(self.frame_network_2)
        self.disconnectBtn.setObjectName(u"disconnectBtn")
        self.disconnectBtn.setEnabled(True)
        self.disconnectBtn.setMinimumSize(QSize(100, 30))
        self.disconnectBtn.setFont(font8)
        self.disconnectBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_11.addWidget(self.disconnectBtn)

        self.connectBtn = QPushButton(self.frame_network_2)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setEnabled(True)
        self.connectBtn.setMinimumSize(QSize(80, 30))
        self.connectBtn.setFont(font8)
        self.connectBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_11.addWidget(self.connectBtn)


        self.verticalLayout_14.addWidget(self.frame_network_2)


        self.verticalLayout_22.addWidget(self.content_network)

        self.stackedWidget.addWidget(self.page_network)
        self.page_rt_graphics = QWidget()
        self.page_rt_graphics.setObjectName(u"page_rt_graphics")
        self.verticalLayout_15 = QVBoxLayout(self.page_rt_graphics)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.rt_graphics_content = QFrame(self.page_rt_graphics)
        self.rt_graphics_content.setObjectName(u"rt_graphics_content")
        self.rt_graphics_content.setFrameShape(QFrame.StyledPanel)
        self.rt_graphics_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.rt_graphics_content)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.upsideGraphics = QFrame(self.rt_graphics_content)
        self.upsideGraphics.setObjectName(u"upsideGraphics")
        self.upsideGraphics.setFrameShape(QFrame.NoFrame)
        self.upsideGraphics.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.upsideGraphics)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_waveform = QFrame(self.upsideGraphics)
        self.frame_waveform.setObjectName(u"frame_waveform")
        self.frame_waveform.setFrameShape(QFrame.NoFrame)
        self.frame_waveform.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_waveform)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.waveform_layout = QVBoxLayout()
        self.waveform_layout.setObjectName(u"waveform_layout")

        self.verticalLayout_31.addLayout(self.waveform_layout)


        self.horizontalLayout_18.addWidget(self.frame_waveform)

        self.frame_fft_transform = QFrame(self.upsideGraphics)
        self.frame_fft_transform.setObjectName(u"frame_fft_transform")
        self.frame_fft_transform.setFrameShape(QFrame.NoFrame)
        self.frame_fft_transform.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_fft_transform)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.fft_transform_layout = QVBoxLayout()
        self.fft_transform_layout.setObjectName(u"fft_transform_layout")

        self.verticalLayout_34.addLayout(self.fft_transform_layout)


        self.horizontalLayout_18.addWidget(self.frame_fft_transform)


        self.verticalLayout_28.addWidget(self.upsideGraphics)

        self.downsideGraphics = QFrame(self.rt_graphics_content)
        self.downsideGraphics.setObjectName(u"downsideGraphics")
        self.downsideGraphics.setFrameShape(QFrame.NoFrame)
        self.downsideGraphics.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.downsideGraphics)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.spectrogram_frame = QFrame(self.downsideGraphics)
        self.spectrogram_frame.setObjectName(u"spectrogram_frame")
        self.spectrogram_frame.setFrameShape(QFrame.NoFrame)
        self.spectrogram_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.spectrogram_frame)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.spectrogram_layout = QVBoxLayout()
        self.spectrogram_layout.setObjectName(u"spectrogram_layout")

        self.verticalLayout_35.addLayout(self.spectrogram_layout)


        self.horizontalLayout_19.addWidget(self.spectrogram_frame)

        self.frame_interactions_btns = QFrame(self.downsideGraphics)
        self.frame_interactions_btns.setObjectName(u"frame_interactions_btns")
        self.frame_interactions_btns.setMaximumSize(QSize(150, 16777215))
        self.frame_interactions_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_interactions_btns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_interactions_btns)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 4, -1, 12)
        self.receptor_node = QComboBox(self.frame_interactions_btns)
        self.receptor_node.setObjectName(u"receptor_node")

        self.verticalLayout_29.addWidget(self.receptor_node)

        self.start_btn = QPushButton(self.frame_interactions_btns)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMinimumSize(QSize(65, 30))
        self.start_btn.setFont(font7)
        self.start_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.verticalLayout_29.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.frame_interactions_btns)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMinimumSize(QSize(65, 30))
        self.stop_btn.setFont(font7)
        self.stop_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.verticalLayout_29.addWidget(self.stop_btn)

        self.reset_btn = QPushButton(self.frame_interactions_btns)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setMinimumSize(QSize(65, 30))
        self.reset_btn.setFont(font7)
        self.reset_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.verticalLayout_29.addWidget(self.reset_btn)

        self.save_btn = QPushButton(self.frame_interactions_btns)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(65, 30))
        self.save_btn.setFont(font7)
        self.save_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.verticalLayout_29.addWidget(self.save_btn)


        self.horizontalLayout_19.addWidget(self.frame_interactions_btns)


        self.verticalLayout_28.addWidget(self.downsideGraphics)


        self.verticalLayout_15.addWidget(self.rt_graphics_content)

        self.stackedWidget.addWidget(self.page_rt_graphics)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_console = QFrame(self.frame_content_right)
        self.frame_console.setObjectName(u"frame_console")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_console.sizePolicy().hasHeightForWidth())
        self.frame_console.setSizePolicy(sizePolicy6)
        self.frame_console.setMinimumSize(QSize(0, 130))
        self.frame_console.setMaximumSize(QSize(16777215, 150))
        self.frame_console.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.frame_console.setFrameShape(QFrame.StyledPanel)
        self.frame_console.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_console)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(12, 0, 12, 6)
        self.console = QPlainTextEdit(self.frame_console)
        self.console.setObjectName(u"console")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy7)
        self.console.setMinimumSize(QSize(0, 0))
        font12 = QFont()
        font12.setPointSize(10)
        self.console.setFont(font12)
        self.console.setFocusPolicy(Qt.NoFocus)
        self.console.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.console.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.console.setReadOnly(True)
        self.console.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_25.addWidget(self.console)


        self.verticalLayout_4.addWidget(self.frame_console)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.central_widget_layout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.panel_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window", None))
#if QT_CONFIG(tooltip)
        self.btn_fullscreen.setToolTip(QCoreApplication.translate("MainWindow", u"Pantalla Completa", None))
#endif // QT_CONFIG(tooltip)
        self.btn_fullscreen.setText("")
#if QT_CONFIG(shortcut)
        self.btn_fullscreen.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"AL", None))
        self.nodes_connected_label.setText(QCoreApplication.translate("MainWindow", u"Nodos conectados", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nodos NET", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nodos RT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"M\u00e1xima amplitud de onda", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Distribuci\u00f3n de m\u00e1xima amplitud", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Saltos", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M\u00ednima amplitud de onda", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Distribuci\u00f3n de m\u00ednima amplitud", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Saltos", None))
        self.threshold_table_label.setText(QCoreApplication.translate("MainWindow", u"Rotura del umbral", None))
        self.threshold_label.setText(QCoreApplication.translate("MainWindow", u"Umbral de potencia", None))
        self.label_threshold_ind.setText(QCoreApplication.translate("MainWindow", u"Valor actual:", None))
        self.threshold_actual_value.setText(QCoreApplication.translate("MainWindow", u"140", None))
        self.apply_threshold_btn.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.labelHeaderUser.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.editBtn.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.createBtn.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.eliminateBtn.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.labelBoxHeaderSettings.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.btn_settings_fullscreen.setText(QCoreApplication.translate("MainWindow", u"Pantalla Completa    F11", None))
        self.backupCheckBox.setText(QCoreApplication.translate("MainWindow", u"Salvas Peri\u00f3dicas", None))
        self.labelHeaderUser_2.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n del Cliente", None))
        self.labelHeaderUser_3.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n del Servidor", None))
        self.labelHeaderUser_4.setText(QCoreApplication.translate("MainWindow", u"Puerto del Servidor", None))
        self.disconnectBtn.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Detener", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Restablecer", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.label_credits.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

