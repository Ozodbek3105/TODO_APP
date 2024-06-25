# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerdpPRWa.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QListWidget, QListWidgetItem,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import rec_rc


class Ui_TODO(object):
    def setupUi(self, TODO):
        if not TODO.objectName():
            TODO.setObjectName(u"TODO")
        TODO.resize(610, 410)
        TODO.setStyleSheet(u"background-color: rgb(170, 170, 127);")
        self.gridLayout = QGridLayout(TODO)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(TODO)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 2, 2)

        self.label = QLabel(TODO)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 italic 20pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addTask_lineEdit = QLineEdit(TODO)
        self.addTask_lineEdit.setObjectName(u"addTask_lineEdit")
        self.addTask_lineEdit.setMinimumSize(QSize(40, 40))
        font = QFont()
        font.setPointSize(15)
        self.addTask_lineEdit.setFont(font)
        self.addTask_lineEdit.setStyleSheet(u"background-color: rgb(236, 236, 236);")

        self.horizontalLayout.addWidget(self.addTask_lineEdit)

        self.addTask_btn = QPushButton(TODO)
        self.addTask_btn.setObjectName(u"addTask_btn")
        self.addTask_btn.setMinimumSize(QSize(40, 40))
        self.addTask_btn.setStyleSheet(u"border:none")
        icon = QIcon()
        icon.addFile(u":/images/icon/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addTask_btn.setIcon(icon)
        self.addTask_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.addTask_btn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tasks_listWidget = QListWidget(TODO)
        self.tasks_listWidget.setObjectName(u"tasks_listWidget")
        font1 = QFont()
        font1.setPointSize(16)
        self.tasks_listWidget.setFont(font1)
        self.tasks_listWidget.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.tasks_listWidget.setBatchSize(10)

        self.verticalLayout.addWidget(self.tasks_listWidget)

        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)

        self.retranslateUi(TODO)

        QMetaObject.connectSlotsByName(TODO)

    # setupUi

    def retranslateUi(self, TODO):
        TODO.setWindowTitle(QCoreApplication.translate("TODO", u"Form", None))
        self.label.setText(QCoreApplication.translate("TODO", u"TODO", None))
        self.addTask_btn.setText("")
    # retranslateUi
