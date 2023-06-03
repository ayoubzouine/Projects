# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainNMzAeq.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 587)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: #2c313a;;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
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
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
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
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(1000, 50))
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color: #21252b;margin-bottom:3.3px")
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.frame_toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color:#ffffff;\n"
"	border-left: 3px solid #21252b;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 7px solid #bd93f9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/icons8_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.btn_toggle)

        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_toggle, 0, Qt.AlignVCenter)

        self.frame_top = QFrame(self.top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.file_comboBox = QComboBox(self.frame_top)
        self.file_comboBox.addItem("")
        self.file_comboBox.addItem("")
        self.file_comboBox.addItem("")
        self.file_comboBox.setObjectName(u"file_comboBox")
        self.file_comboBox.setMaximumSize(QSize(250, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QFont.Weight(50))
        self.file_comboBox.setFont(font)
        self.file_comboBox.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"border: 1.5px solid #2d2d2d;\n"
"width:600px !important;\n"
"height:20px !important;\n"
"padding:2px 0 2px 6px;\n"
"margin:4px;\n"
"margin-left:70px;\n"
"border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_24.addWidget(self.file_comboBox)

        self.label_24 = QLabel(self.frame_top)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"padding-left:150px;")

        self.horizontalLayout_24.addWidget(self.label_24)

        self.frame_6 = QFrame(self.frame_top)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 5, 0)
        self.settingsTopBtn = QPushButton(self.frame_6)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsTopBtn.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.frame_6)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.frame_6)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(QFont.Weight(50))
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeRestoreAppBtn.setStyleSheet(u"border:none;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.frame_6)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setStyleSheet(u"border:none;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon4)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.closeAppBtn)


        self.horizontalLayout_24.addWidget(self.frame_6, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.top_bar, 0, Qt.AlignVCenter)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(155, 0))
        self.frame_left_menu.setMaximumSize(QSize(16777215, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: #21252b;padding-top:10px;")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setMinimumSize(QSize(165, 0))
        self.frame_top_menus.setFont(font)
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_top_menus)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setFont(font)
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-left: 3px solid #252930;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-top:9px;\n"
"	padding-bottom:9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 5px solid #bd93f9;\n"
"	background-color: #252930;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_basic = QPushButton(self.frame_top_menus)
        self.btn_basic.setObjectName(u"btn_basic")
        self.btn_basic.setMinimumSize(QSize(0, 30))
        self.btn_basic.setFont(font)
        self.btn_basic.setAutoFillBackground(False)
        self.btn_basic.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-left: 3px solid #252930;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-top:9px;\n"
"	padding-bottom:9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 5px solid #bd93f9;\n"
"	background-color: #252930;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_basic)

        self.btn_filtre = QPushButton(self.frame_top_menus)
        self.btn_filtre.setObjectName(u"btn_filtre")
        self.btn_filtre.setMinimumSize(QSize(0, 30))
        self.btn_filtre.setFont(font)
        self.btn_filtre.setAutoFillBackground(False)
        self.btn_filtre.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-left: 3px solid #252930;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-top:9px;\n"
"	padding-bottom:9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 5px solid #bd93f9;\n"
"	background-color: #252930;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_filtre)

        self.btn_contour = QPushButton(self.frame_top_menus)
        self.btn_contour.setObjectName(u"btn_contour")
        self.btn_contour.setMinimumSize(QSize(0, 30))
        self.btn_contour.setFont(font)
        self.btn_contour.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-left: 3px solid #252930;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-top:9px;\n"
"	padding-bottom:9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 5px solid #bd93f9;\n"
"	background-color: #252930;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_contour)

        self.btn_morpho = QPushButton(self.frame_top_menus)
        self.btn_morpho.setObjectName(u"btn_morpho")
        self.btn_morpho.setMinimumSize(QSize(0, 30))
        self.btn_morpho.setFont(font)
        self.btn_morpho.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-left: 3px solid #252930;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-top:9px;\n"
"	padding-bottom:9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 5px solid #bd93f9;\n"
"	background-color: #252930;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_morpho)

        self.btn_seg = QPushButton(self.frame_top_menus)
        self.btn_seg.setObjectName(u"btn_seg")
        self.btn_seg.setMinimumSize(QSize(0, 30))
        self.btn_seg.setFont(font)
        self.btn_seg.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-left: 3px solid #252930;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-top:9px;\n"
"	padding-bottom:9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 5px solid #bd93f9;\n"
"	background-color: #252930;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_seg)

        self.btn_interet = QPushButton(self.frame_top_menus)
        self.btn_interet.setObjectName(u"btn_interet")
        self.btn_interet.setMinimumSize(QSize(0, 30))
        self.btn_interet.setFont(font)
        self.btn_interet.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-left: 3px solid #252930;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-top:9px;\n"
"	padding-bottom:9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 5px solid #bd93f9;\n"
"	background-color: #252930;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_interet)

        self.btn_compression = QPushButton(self.frame_top_menus)
        self.btn_compression.setObjectName(u"btn_compression")
        self.btn_compression.setMinimumSize(QSize(0, 30))
        self.btn_compression.setFont(font)
        self.btn_compression.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-left: 3px solid #252930;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-top:9px;\n"
"	padding-bottom:9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 5px solid #bd93f9;\n"
"	background-color: #252930;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_compression)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.frame_top_menus)


        self.horizontalLayout_3.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"background-color: #282c34;")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.pages_widget.setStyleSheet(u"")
        self.page_pnts_interet = QWidget()
        self.page_pnts_interet.setObjectName(u"page_pnts_interet")
        self.verticalLayout_14 = QVBoxLayout(self.page_pnts_interet)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page_pnts_interet)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.label_2)

        self.label_img_interet = QLabel(self.frame_9)
        self.label_img_interet.setObjectName(u"label_img_interet")
        self.label_img_interet.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_15.addWidget(self.label_img_interet)


        self.horizontalLayout_6.addWidget(self.frame_9)

        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(1, 16777215))
        self.label.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"margin-bottom:11px;\n"
"margin-top:36px;")

        self.horizontalLayout_6.addWidget(self.label)

        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.label_5)

        self.label_rslt_interet = QLabel(self.frame_13)
        self.label_rslt_interet.setObjectName(u"label_rslt_interet")
        self.label_rslt_interet.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_16.addWidget(self.label_rslt_interet)


        self.horizontalLayout_6.addWidget(self.frame_13)


        self.verticalLayout_14.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.page_pnts_interet)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(28)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_calculer_interet = QPushButton(self.frame_7)
        self.btn_calculer_interet.setObjectName(u"btn_calculer_interet")
        self.btn_calculer_interet.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calculer_interet.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_calculer_interet)

        self.frame_23 = QFrame(self.frame_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_23)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.label_14)

        self.comboBox_interet = QComboBox(self.frame_23)
        self.comboBox_interet.addItem("")
        self.comboBox_interet.addItem("")
        self.comboBox_interet.addItem("")
        self.comboBox_interet.addItem("")
        self.comboBox_interet.setObjectName(u"comboBox_interet")
        self.comboBox_interet.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.comboBox_interet)


        self.horizontalLayout_4.addWidget(self.frame_23)


        self.verticalLayout_14.addWidget(self.frame_7)

        self.pages_widget.addWidget(self.page_pnts_interet)
        self.page_basic = QWidget()
        self.page_basic.setObjectName(u"page_basic")
        self.verticalLayout_6 = QVBoxLayout(self.page_basic)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_basic)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.label_original_2 = QLabel(self.frame_3)
        self.label_original_2.setObjectName(u"label_original_2")
        self.label_original_2.setMaximumSize(QSize(16777215, 25))
        self.label_original_2.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.label_original_2)

        self.label_image_menu_basic = QLabel(self.frame_3)
        self.label_image_menu_basic.setObjectName(u"label_image_menu_basic")
        self.label_image_menu_basic.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")
        self.label_image_menu_basic.setMargin(0)

        self.verticalLayout_13.addWidget(self.label_image_menu_basic)


        self.horizontalLayout_7.addWidget(self.frame_3)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(1, 16777215))
        self.label_3.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"margin-bottom:11px;\n"
"margin-top:36px;")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(9, -1, 9, -1)
        self.label_result_2 = QLabel(self.frame_10)
        self.label_result_2.setObjectName(u"label_result_2")
        self.label_result_2.setMaximumSize(QSize(16777215, 25))
        self.label_result_2.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.label_result_2)

        self.label_result_basic = QLabel(self.frame_10)
        self.label_result_basic.setObjectName(u"label_result_basic")
        self.label_result_basic.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_17.addWidget(self.label_result_basic)


        self.horizontalLayout_7.addWidget(self.frame_10)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 110))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid #232323;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"*{\n"
"color:#ffffff\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 10, 1, 1)
        self.frame_12 = QFrame(self.groupBox)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.btn_selectioner = QPushButton(self.frame_12)
        self.btn_selectioner.setObjectName(u"btn_selectioner")
        self.btn_selectioner.setFont(font)
        self.btn_selectioner.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_selectioner.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_selectioner)

        self.btn_redimensionner = QPushButton(self.frame_12)
        self.btn_redimensionner.setObjectName(u"btn_redimensionner")
        self.btn_redimensionner.setFont(font)
        self.btn_redimensionner.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_redimensionner.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_redimensionner)

        self.btn_rotation = QPushButton(self.frame_12)
        self.btn_rotation.setObjectName(u"btn_rotation")
        self.btn_rotation.setFont(font)
        self.btn_rotation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rotation.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_rotation)

        self.btn_negatif = QPushButton(self.frame_12)
        self.btn_negatif.setObjectName(u"btn_negatif")
        self.btn_negatif.setFont(font)
        self.btn_negatif.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_negatif.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_negatif)

        self.btn_histogramme = QPushButton(self.frame_12)
        self.btn_histogramme.setObjectName(u"btn_histogramme")
        self.btn_histogramme.setFont(font)
        self.btn_histogramme.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_histogramme.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_histogramme)


        self.verticalLayout_18.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.groupBox)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 6, -1, -1)
        self.btn_binarisation = QPushButton(self.frame_11)
        self.btn_binarisation.setObjectName(u"btn_binarisation")
        self.btn_binarisation.setFont(font)
        self.btn_binarisation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_binarisation.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_binarisation)

        self.pushButton_18 = QPushButton(self.frame_11)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_18)

        self.btn_etirer = QPushButton(self.frame_11)
        self.btn_etirer.setObjectName(u"btn_etirer")
        self.btn_etirer.setFont(font)
        self.btn_etirer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_etirer.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_etirer)

        self.btn_egaliser = QPushButton(self.frame_11)
        self.btn_egaliser.setObjectName(u"btn_egaliser")
        self.btn_egaliser.setFont(font)
        self.btn_egaliser.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_egaliser.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_egaliser)


        self.verticalLayout_18.addWidget(self.frame_11)


        self.verticalLayout_7.addWidget(self.groupBox)


        self.verticalLayout_6.addWidget(self.frame)

        self.pages_widget.addWidget(self.page_basic)
        self.page_compression = QWidget()
        self.page_compression.setObjectName(u"page_compression")
        self.vboxLayout = QVBoxLayout(self.page_compression)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.page_compression)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_16)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.label_6)

        self.label_img_compress = QLabel(self.frame_16)
        self.label_img_compress.setObjectName(u"label_img_compress")
        self.label_img_compress.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_21.addWidget(self.label_img_compress)


        self.horizontalLayout_12.addWidget(self.frame_16)

        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(1, 16777215))
        self.label_8.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"margin-bottom:11px;\n"
"margin-top:36px;")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_17)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 25))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.label_9)

        self.label_rslt_compress = QLabel(self.frame_17)
        self.label_rslt_compress.setObjectName(u"label_rslt_compress")
        self.label_rslt_compress.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_22.addWidget(self.label_rslt_compress)


        self.horizontalLayout_12.addWidget(self.frame_17)


        self.vboxLayout.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.page_compression)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 55))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(28)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_compress = QPushButton(self.frame_15)
        self.btn_compress.setObjectName(u"btn_compress")
        self.btn_compress.setMinimumSize(QSize(0, 0))
        self.btn_compress.setFont(font)
        self.btn_compress.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_compress.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height: 60px !important;\n"
"padding:4px 2px 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_compress)

        self.frame_22 = QFrame(self.frame_15)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_22)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.comboBox_compress = QComboBox(self.frame_22)
        self.comboBox_compress.addItem("")
        self.comboBox_compress.addItem("")
        self.comboBox_compress.addItem("")
        self.comboBox_compress.addItem("")
        self.comboBox_compress.setObjectName(u"comboBox_compress")
        self.comboBox_compress.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_15.addWidget(self.comboBox_compress)


        self.horizontalLayout_11.addWidget(self.frame_22)


        self.vboxLayout.addWidget(self.frame_15)

        self.pages_widget.addWidget(self.page_compression)
        self.page_fltr_median = QWidget()
        self.page_fltr_median.setObjectName(u"page_fltr_median")
        self.verticalLayout_23 = QVBoxLayout(self.page_fltr_median)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.page_fltr_median)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_10 = QLabel(self.frame_20)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 25))
        self.label_10.setStyleSheet(u"")

        self.verticalLayout_24.addWidget(self.label_10)

        self.label_img_med = QLabel(self.frame_20)
        self.label_img_med.setObjectName(u"label_img_med")
        self.label_img_med.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_24.addWidget(self.label_img_med)


        self.horizontalLayout_14.addWidget(self.frame_20)

        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(1, 16777215))
        self.label_11.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"margin-bottom:11px;\n"
"margin-top:36px;")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_21)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_12 = QLabel(self.frame_21)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 25))
        self.label_12.setStyleSheet(u"")

        self.verticalLayout_25.addWidget(self.label_12)

        self.label_rslt_med = QLabel(self.frame_21)
        self.label_rslt_med.setObjectName(u"label_rslt_med")
        self.label_rslt_med.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_25.addWidget(self.label_rslt_med)


        self.horizontalLayout_14.addWidget(self.frame_21)


        self.verticalLayout_23.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.page_fltr_median)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 100))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_27.setSpacing(28)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.btn_fltr_med = QPushButton(self.frame_19)
        self.btn_fltr_med.setObjectName(u"btn_fltr_med")
        self.btn_fltr_med.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fltr_med.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_27.addWidget(self.btn_fltr_med)

        self.frame_41 = QFrame(self.frame_19)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_41)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_41)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 50))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_24)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_31)

        self.comboBox_filtre = QComboBox(self.frame_24)
        self.comboBox_filtre.addItem("")
        self.comboBox_filtre.addItem("")
        self.comboBox_filtre.addItem("")
        self.comboBox_filtre.addItem("")
        self.comboBox_filtre.setObjectName(u"comboBox_filtre")
        self.comboBox_filtre.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_13.addWidget(self.comboBox_filtre)


        self.verticalLayout_10.addWidget(self.frame_24)

        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_42)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_32)

        self.comboBox2_filtre = QComboBox(self.frame_42)
        self.comboBox2_filtre.addItem("")
        self.comboBox2_filtre.addItem("")
        self.comboBox2_filtre.addItem("")
        self.comboBox2_filtre.addItem("")
        self.comboBox2_filtre.addItem("")
        self.comboBox2_filtre.addItem("")
        self.comboBox2_filtre.setObjectName(u"comboBox2_filtre")
        self.comboBox2_filtre.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.comboBox2_filtre)


        self.verticalLayout_10.addWidget(self.frame_42)


        self.horizontalLayout_27.addWidget(self.frame_41)


        self.verticalLayout_23.addWidget(self.frame_19)

        self.pages_widget.addWidget(self.page_fltr_median)
        self.page_contour = QWidget()
        self.page_contour.setObjectName(u"page_contour")
        self.verticalLayout_26 = QVBoxLayout(self.page_contour)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.page_contour)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_27)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_16 = QLabel(self.frame_27)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 25))
        self.label_16.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.label_16)

        self.label_img_contour = QLabel(self.frame_27)
        self.label_img_contour.setObjectName(u"label_img_contour")
        self.label_img_contour.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_27.addWidget(self.label_img_contour)


        self.horizontalLayout_18.addWidget(self.frame_27)

        self.label_17 = QLabel(self.frame_25)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(1, 16777215))
        self.label_17.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"margin-bottom:11px;\n"
"margin-top:36px;")

        self.horizontalLayout_18.addWidget(self.label_17)

        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_28)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_18 = QLabel(self.frame_28)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 25))
        self.label_18.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.label_18)

        self.label_rslt_contour = QLabel(self.frame_28)
        self.label_rslt_contour.setObjectName(u"label_rslt_contour")
        self.label_rslt_contour.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.label_rslt_contour)


        self.horizontalLayout_18.addWidget(self.frame_28)


        self.verticalLayout_26.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.page_contour)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 50))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setSpacing(28)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btn_calculer_contour = QPushButton(self.frame_26)
        self.btn_calculer_contour.setObjectName(u"btn_calculer_contour")
        self.btn_calculer_contour.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calculer_contour.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_19.addWidget(self.btn_calculer_contour)

        self.frame_33 = QFrame(self.frame_26)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_33)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_22.addWidget(self.label_22)

        self.comboBox_contour = QComboBox(self.frame_33)
        self.comboBox_contour.addItem("")
        self.comboBox_contour.addItem("")
        self.comboBox_contour.addItem("")
        self.comboBox_contour.addItem("")
        self.comboBox_contour.addItem("")
        self.comboBox_contour.setObjectName(u"comboBox_contour")
        self.comboBox_contour.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.comboBox_contour)


        self.horizontalLayout_19.addWidget(self.frame_33)


        self.verticalLayout_26.addWidget(self.frame_26)

        self.pages_widget.addWidget(self.page_contour)
        self.page_morpho = QWidget()
        self.page_morpho.setObjectName(u"page_morpho")
        self.verticalLayout_29 = QVBoxLayout(self.page_morpho)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.page_morpho)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_31)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.label_19 = QLabel(self.frame_31)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 25))
        self.label_19.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.label_19)

        self.label_img_morpho = QLabel(self.frame_31)
        self.label_img_morpho.setObjectName(u"label_img_morpho")
        self.label_img_morpho.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_30.addWidget(self.label_img_morpho)


        self.horizontalLayout_20.addWidget(self.frame_31)

        self.label_20 = QLabel(self.frame_29)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(1, 16777215))
        self.label_20.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"margin-bottom:11px;\n"
"margin-top:36px;")

        self.horizontalLayout_20.addWidget(self.label_20)

        self.frame_32 = QFrame(self.frame_29)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_32)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(-1, -1, -1, 0)
        self.label_21 = QLabel(self.frame_32)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 25))
        self.label_21.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_21)

        self.label_rslt_morpho = QLabel(self.frame_32)
        self.label_rslt_morpho.setObjectName(u"label_rslt_morpho")
        self.label_rslt_morpho.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_31.addWidget(self.label_rslt_morpho)


        self.horizontalLayout_20.addWidget(self.frame_32)


        self.verticalLayout_29.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.page_morpho)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 100))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_21.setSpacing(28)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_calculer_morpho = QPushButton(self.frame_30)
        self.btn_calculer_morpho.setObjectName(u"btn_calculer_morpho")
        self.btn_calculer_morpho.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calculer_morpho.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout_21.addWidget(self.btn_calculer_morpho)

        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_34)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_34)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_23)

        self.comboBox_morpho = QComboBox(self.frame_5)
        self.comboBox_morpho.addItem("")
        self.comboBox_morpho.addItem("")
        self.comboBox_morpho.addItem("")
        self.comboBox_morpho.addItem("")
        self.comboBox_morpho.addItem("")
        self.comboBox_morpho.addItem("")
        self.comboBox_morpho.setObjectName(u"comboBox_morpho")
        self.comboBox_morpho.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.comboBox_morpho)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_34)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_29)

        self.comboBox_morpho_elem = QComboBox(self.frame_4)
        self.comboBox_morpho_elem.addItem("")
        self.comboBox_morpho_elem.addItem("")
        self.comboBox_morpho_elem.addItem("")
        self.comboBox_morpho_elem.addItem("")
        self.comboBox_morpho_elem.addItem("")
        self.comboBox_morpho_elem.addItem("")
        self.comboBox_morpho_elem.addItem("")
        self.comboBox_morpho_elem.setObjectName(u"comboBox_morpho_elem")
        self.comboBox_morpho_elem.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.comboBox_morpho_elem)


        self.verticalLayout_8.addWidget(self.frame_4)


        self.horizontalLayout_21.addWidget(self.frame_34)


        self.verticalLayout_29.addWidget(self.frame_30)

        self.pages_widget.addWidget(self.page_morpho)
        self.page_segmentation = QWidget()
        self.page_segmentation.setObjectName(u"page_segmentation")
        self.verticalLayout_32 = QVBoxLayout(self.page_segmentation)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.page_segmentation)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_37)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_25 = QLabel(self.frame_37)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 25))
        self.label_25.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.label_25)

        self.label_img_segmentation = QLabel(self.frame_37)
        self.label_img_segmentation.setObjectName(u"label_img_segmentation")
        self.label_img_segmentation.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_33.addWidget(self.label_img_segmentation)


        self.horizontalLayout_25.addWidget(self.frame_37)

        self.label_26 = QLabel(self.frame_35)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(1, 16777215))
        self.label_26.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"margin-bottom:11px;\n"
"margin-top:36px;")

        self.horizontalLayout_25.addWidget(self.label_26)

        self.frame_38 = QFrame(self.frame_35)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_38)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_27 = QLabel(self.frame_38)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 25))
        self.label_27.setStyleSheet(u"")

        self.verticalLayout_34.addWidget(self.label_27)

        self.label_rslt_segmentation = QLabel(self.frame_38)
        self.label_rslt_segmentation.setObjectName(u"label_rslt_segmentation")
        self.label_rslt_segmentation.setStyleSheet(u"*{\n"
"border: 1.5px solid #232323;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_34.addWidget(self.label_rslt_segmentation)


        self.horizontalLayout_25.addWidget(self.frame_38)


        self.verticalLayout_32.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.page_segmentation)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 50))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_36)
        self.horizontalLayout.setSpacing(28)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_calculer_seg = QPushButton(self.frame_36)
        self.btn_calculer_seg.setObjectName(u"btn_calculer_seg")
        self.btn_calculer_seg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calculer_seg.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:25px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_calculer_seg)

        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_39)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_26.addWidget(self.label_28)

        self.comboBox_seg = QComboBox(self.frame_39)
        self.comboBox_seg.addItem("")
        self.comboBox_seg.addItem("")
        self.comboBox_seg.addItem("")
        self.comboBox_seg.addItem("")
        self.comboBox_seg.setObjectName(u"comboBox_seg")
        self.comboBox_seg.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_26.addWidget(self.comboBox_seg)


        self.horizontalLayout.addWidget(self.frame_39)


        self.verticalLayout_32.addWidget(self.frame_36)

        self.pages_widget.addWidget(self.page_segmentation)

        self.verticalLayout_5.addWidget(self.pages_widget)


        self.horizontalLayout_3.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText("")
        self.file_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"File operations", None))
        self.file_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"add", None))
        self.file_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"save", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Designed by SDSI team.", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_basic.setText(QCoreApplication.translate("MainWindow", u"Basic ops", None))
        self.btn_filtre.setText(QCoreApplication.translate("MainWindow", u"filtres", None))
        self.btn_contour.setText(QCoreApplication.translate("MainWindow", u"contour", None))
        self.btn_morpho.setText(QCoreApplication.translate("MainWindow", u"morphologie", None))
        self.btn_seg.setText(QCoreApplication.translate("MainWindow", u"segmentation", None))
        self.btn_interet.setText(QCoreApplication.translate("MainWindow", u"pnts interet", None))
        self.btn_compression.setText(QCoreApplication.translate("MainWindow", u"compression", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"                              Image originale", None))
        self.label_img_interet.setText("")
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"                            pionts d'interet ", None))
        self.label_rslt_interet.setText("")
        self.btn_calculer_interet.setText(QCoreApplication.translate("MainWindow", u"Chercher", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Type Filtre :", None))
        self.comboBox_interet.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir un filtre", None))
        self.comboBox_interet.setItemText(1, QCoreApplication.translate("MainWindow", u"Hough", None))
        self.comboBox_interet.setItemText(2, QCoreApplication.translate("MainWindow", u"Gabor", None))
        self.comboBox_interet.setItemText(3, QCoreApplication.translate("MainWindow", u"Shi-Tomasi", None))

        self.label_original_2.setText(QCoreApplication.translate("MainWindow", u"                           Image originale", None))
        self.label_image_menu_basic.setText("")
        self.label_3.setText("")
        self.label_result_2.setText(QCoreApplication.translate("MainWindow", u"                                      resultat", None))
        self.label_result_basic.setText("")
        self.groupBox.setTitle("")
        self.btn_selectioner.setText(QCoreApplication.translate("MainWindow", u"selectioner", None))
        self.btn_redimensionner.setText(QCoreApplication.translate("MainWindow", u"redimensionner", None))
#if QT_CONFIG(tooltip)
        self.btn_rotation.setToolTip(QCoreApplication.translate("MainWindow", u"rotation de 45 deg", None))
#endif // QT_CONFIG(tooltip)
        self.btn_rotation.setText(QCoreApplication.translate("MainWindow", u"rotation", None))
        self.btn_negatif.setText(QCoreApplication.translate("MainWindow", u"negatif", None))
        self.btn_histogramme.setText(QCoreApplication.translate("MainWindow", u"histogramme", None))
        self.btn_binarisation.setText(QCoreApplication.translate("MainWindow", u"binarisation", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_etirer.setText(QCoreApplication.translate("MainWindow", u"etirer", None))
        self.btn_egaliser.setText(QCoreApplication.translate("MainWindow", u"egaliser", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"                               Image originale", None))
        self.label_img_compress.setText("")
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"                               Image originale", None))
        self.label_rslt_compress.setText("")
        self.btn_compress.setText(QCoreApplication.translate("MainWindow", u"Compresser", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Type compression :", None))
        self.comboBox_compress.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir un type", None))
        self.comboBox_compress.setItemText(1, QCoreApplication.translate("MainWindow", u"Huffman", None))
        self.comboBox_compress.setItemText(2, QCoreApplication.translate("MainWindow", u"LZW", None))
        self.comboBox_compress.setItemText(3, QCoreApplication.translate("MainWindow", u"Ondelette", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"                           Image originale", None))
        self.label_img_med.setText("")
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"                               resultat du filtrer", None))
        self.label_rslt_med.setText("")
        self.btn_fltr_med.setText(QCoreApplication.translate("MainWindow", u"Filtrer", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Type filtre :", None))
        self.comboBox_filtre.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir un filtre", None))
        self.comboBox_filtre.setItemText(1, QCoreApplication.translate("MainWindow", u"Gaussien", None))
        self.comboBox_filtre.setItemText(2, QCoreApplication.translate("MainWindow", u"Moyenneur", None))
        self.comboBox_filtre.setItemText(3, QCoreApplication.translate("MainWindow", u"Median", None))

        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Element structurent :", None))
        self.comboBox2_filtre.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir l'\u00e9lement", None))
        self.comboBox2_filtre.setItemText(1, QCoreApplication.translate("MainWindow", u"3x3", None))
        self.comboBox2_filtre.setItemText(2, QCoreApplication.translate("MainWindow", u"5x5", None))
        self.comboBox2_filtre.setItemText(3, QCoreApplication.translate("MainWindow", u"7x7", None))
        self.comboBox2_filtre.setItemText(4, QCoreApplication.translate("MainWindow", u"11x11", None))
        self.comboBox2_filtre.setItemText(5, QCoreApplication.translate("MainWindow", u"45x45", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"                           Image originale", None))
        self.label_img_contour.setText("")
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"                               resultat contour", None))
        self.label_rslt_contour.setText("")
        self.btn_calculer_contour.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Type contour :", None))
        self.comboBox_contour.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir filtre", None))
        self.comboBox_contour.setItemText(1, QCoreApplication.translate("MainWindow", u"Gradient", None))
        self.comboBox_contour.setItemText(2, QCoreApplication.translate("MainWindow", u"Sobel", None))
        self.comboBox_contour.setItemText(3, QCoreApplication.translate("MainWindow", u"Robert", None))
        self.comboBox_contour.setItemText(4, QCoreApplication.translate("MainWindow", u"Laplacien", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"                              Image originale", None))
        self.label_img_morpho.setText("")
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"                            resultat morphologique", None))
        self.label_rslt_morpho.setText("")
        self.btn_calculer_morpho.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Type morpholoqie :", None))
        self.comboBox_morpho.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir l'op\u00e9ation", None))
        self.comboBox_morpho.setItemText(1, QCoreApplication.translate("MainWindow", u"Erosion", None))
        self.comboBox_morpho.setItemText(2, QCoreApplication.translate("MainWindow", u"Dilatation", None))
        self.comboBox_morpho.setItemText(3, QCoreApplication.translate("MainWindow", u"Fermeture", None))
        self.comboBox_morpho.setItemText(4, QCoreApplication.translate("MainWindow", u"Ouverture", None))
        self.comboBox_morpho.setItemText(5, QCoreApplication.translate("MainWindow", u"Filtrage morpho", None))

        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Element structurent :", None))
        self.comboBox_morpho_elem.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir l'\u00e9lement", None))
        self.comboBox_morpho_elem.setItemText(1, QCoreApplication.translate("MainWindow", u"3x3", None))
        self.comboBox_morpho_elem.setItemText(2, QCoreApplication.translate("MainWindow", u"4x4", None))
        self.comboBox_morpho_elem.setItemText(3, QCoreApplication.translate("MainWindow", u"5x5", None))
        self.comboBox_morpho_elem.setItemText(4, QCoreApplication.translate("MainWindow", u"7x7", None))
        self.comboBox_morpho_elem.setItemText(5, QCoreApplication.translate("MainWindow", u"11x11", None))
        self.comboBox_morpho_elem.setItemText(6, QCoreApplication.translate("MainWindow", u"45x45", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"                           Image originale", None))
        self.label_img_segmentation.setText("")
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"                            resultat segmentation", None))
        self.label_rslt_segmentation.setText("")
        self.btn_calculer_seg.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Type segmentation :", None))
        self.comboBox_seg.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir l'op\u00e9ation", None))
        self.comboBox_seg.setItemText(1, QCoreApplication.translate("MainWindow", u" Croissance de r\u00e9gions D", None))
        self.comboBox_seg.setItemText(2, QCoreApplication.translate("MainWindow", u" Partition de r\u00e9gions D", None))
        self.comboBox_seg.setItemText(3, QCoreApplication.translate("MainWindow", u" M\u00e9thode des k-means", None))

    # retranslateUi

