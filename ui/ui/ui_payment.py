# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'payment.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(579, 199)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dialog_window = QFrame(Dialog)
        self.dialog_window.setObjectName(u"dialog_window")
        self.dialog_window.setFrameShape(QFrame.StyledPanel)
        self.dialog_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.dialog_window)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title_frame = QFrame(self.dialog_window)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMinimumSize(QSize(0, 60))
        self.title_frame.setMaximumSize(QSize(16777215, 60))
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.title_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.title_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"font: 900 16pt \"Segoe UI Black\";")
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.logo)


        self.verticalLayout_4.addWidget(self.title_frame)

        self.main_frame = QFrame(self.dialog_window)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name_frame = QFrame(self.main_frame)
        self.name_frame.setObjectName(u"name_frame")
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.name_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.name_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(75, 0))
        self.label.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label)

        self.amount = QLineEdit(self.frame)
        self.amount.setObjectName(u"amount")
        self.amount.setMinimumSize(QSize(150, 30))
        self.amount.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_3.addWidget(self.amount)

        self.currency = QLabel(self.frame)
        self.currency.setObjectName(u"currency")

        self.horizontalLayout_3.addWidget(self.currency)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(self.name_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(75, 0))
        self.label_2.setMaximumSize(QSize(50, 16777215))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.date = QDateEdit(self.frame_4)
        self.date.setObjectName(u"date")
        self.date.setMinimumSize(QSize(150, 30))
        self.date.setMaximumSize(QSize(150, 16777215))
        self.date.setCurrentSection(QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(False)

        self.horizontalLayout_4.addWidget(self.date)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.name_frame)


        self.verticalLayout_4.addWidget(self.main_frame)

        self.control_frame = QFrame(self.dialog_window)
        self.control_frame.setObjectName(u"control_frame")
        self.control_frame.setMinimumSize(QSize(0, 50))
        self.control_frame.setMaximumSize(QSize(16777215, 50))
        self.control_frame.setFrameShape(QFrame.StyledPanel)
        self.control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.control_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.error = QLabel(self.control_frame)
        self.error.setObjectName(u"error")
        self.error.setMinimumSize(QSize(300, 0))
        self.error.setStyleSheet(u"font: 700 8pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.error)

        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(self.control_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(100, 40))
        self.cancel_btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(self.control_frame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.save_btn)


        self.verticalLayout_4.addWidget(self.control_frame)


        self.verticalLayout.addWidget(self.dialog_window)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.logo.setText(QCoreApplication.translate("Dialog", u"Payment #0001", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.currency.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.date.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MM-yyyy", None))
        self.error.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.cancel_btn.setProperty("class", QCoreApplication.translate("Dialog", u"SecondaryButton", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

