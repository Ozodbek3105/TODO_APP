# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeroUmyfs.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QPushButton, QLineEdit)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(582, 81)
        Form.setMinimumSize(QSize(582, 81))
        Form.setMaximumSize(QSize(582, 81))

        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_is_checked = QPushButton(Form)
        self.btn_is_checked.setObjectName(u"pushButton")
        self.btn_is_checked.setMaximumSize(QSize(40, 40))
        self.btn_is_checked.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/images/icon/uncheck.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/icon/check.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_is_checked.setIcon(icon)
        self.btn_is_checked.setIconSize(QSize(40, 40))
        self.btn_is_checked.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_is_checked)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgb(193, 255, 245);\n"
                                    "font: 600 16pt \"Segoe UI\";\n"
                                    "border-radius:15px;"
                                    "padding-left:10;")
        #
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)
        self.top_btn = QPushButton(Form)
        self.top_btn.setObjectName(u"pushButton_2")
        self.top_btn.setMinimumSize(QSize(40, 40))
        self.top_btn.setMaximumSize(QSize(40, 40))
        self.top_btn.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/images/icon/untop.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/icon/top.png", QSize(), QIcon.Normal, QIcon.On)
        self.top_btn.setIcon(icon1)
        self.top_btn.setIconSize(QSize(40, 40))
        self.top_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.top_btn)

        self.delete_btn = QPushButton(Form)
        self.delete_btn.setObjectName(u"pushButton_3")
        self.delete_btn.setMaximumSize(QSize(40, 40))
        self.delete_btn.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/images/icon/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon2)
        self.delete_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.delete_btn)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_is_checked.setText("")
        self.lineEdit.setText(QCoreApplication.translate("Form", u"Vazifa", None))
        self.top_btn.setText("")
        self.delete_btn.setText("")
    # retranslateUi
