# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'binarisationkZhlxB.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: #282c34;\n"
"")
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(16777215, 35))
        self.comboBox.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.frame_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(16777215, 35))
        self.spinBox.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:40px;\n"
"padding:2px;\n"
"border-radius: 5px;\n"
"}")
        self.spinBox.setMaximum(255)

        self.horizontalLayout_3.addWidget(self.spinBox)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignVCenter)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16777215, 35))
        self.pushButton_2.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:30px;\n"
"padding:2px;\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 35))
        self.pushButton.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"border: 1.5px solid #232323;\n"
"height:30px;\n"
"padding:2px;\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #232323;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Binarisation", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Type :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Par seuil", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"OTSU", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Seuil :", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Entrer", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi

