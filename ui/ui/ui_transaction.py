# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transaction.ui'
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
        Dialog.resize(664, 263)
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
        self.label.setMaximumSize(QSize(75, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label)

        self.debtor = QComboBox(self.frame)
        self.debtor.setObjectName(u"debtor")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debtor.sizePolicy().hasHeightForWidth())
        self.debtor.setSizePolicy(sizePolicy)
        self.debtor.setMinimumSize(QSize(230, 30))
        self.debtor.setMaximumSize(QSize(240, 30))

        self.horizontalLayout_3.addWidget(self.debtor)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(self.name_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(75, 0))
        self.label_2.setMaximumSize(QSize(75, 16777215))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.creditor = QComboBox(self.frame_4)
        self.creditor.setObjectName(u"creditor")
        sizePolicy.setHeightForWidth(self.creditor.sizePolicy().hasHeightForWidth())
        self.creditor.setSizePolicy(sizePolicy)
        self.creditor.setMinimumSize(QSize(230, 30))
        self.creditor.setMaximumSize(QSize(240, 30))

        self.horizontalLayout_4.addWidget(self.creditor)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.name_frame)

        self.contact_frame = QFrame(self.main_frame)
        self.contact_frame.setObjectName(u"contact_frame")
        self.contact_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.contact_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.contact_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(75, 0))
        self.label_3.setMaximumSize(QSize(75, 16777215))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.sent_amount = QLineEdit(self.frame_5)
        self.sent_amount.setObjectName(u"sent_amount")
        sizePolicy.setHeightForWidth(self.sent_amount.sizePolicy().hasHeightForWidth())
        self.sent_amount.setSizePolicy(sizePolicy)
        self.sent_amount.setMinimumSize(QSize(150, 30))
        self.sent_amount.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_5.addWidget(self.sent_amount)

        self.sent_currency = QLabel(self.frame_5)
        self.sent_currency.setObjectName(u"sent_currency")

        self.horizontalLayout_5.addWidget(self.sent_currency)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.contact_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(75, 0))
        self.label_4.setMaximumSize(QSize(75, 16777215))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.recv_amount = QLineEdit(self.frame_6)
        self.recv_amount.setObjectName(u"recv_amount")
        sizePolicy.setHeightForWidth(self.recv_amount.sizePolicy().hasHeightForWidth())
        self.recv_amount.setSizePolicy(sizePolicy)
        self.recv_amount.setMinimumSize(QSize(150, 30))
        self.recv_amount.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_6.addWidget(self.recv_amount)

        self.recv_currency = QLabel(self.frame_6)
        self.recv_currency.setObjectName(u"recv_currency")

        self.horizontalLayout_6.addWidget(self.recv_currency)


        self.horizontalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.contact_frame)

        self.frame_3 = QFrame(self.main_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(75, 0))
        self.label_5.setMaximumSize(QSize(75, 16777215))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.date = QDateEdit(self.frame_3)
        self.date.setObjectName(u"date")
        self.date.setMinimumSize(QSize(235, 30))
        self.date.setMaximumSize(QSize(240, 16777215))
        self.date.setCurrentSection(QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(False)

        self.horizontalLayout_8.addWidget(self.date)

        self.horizontalSpacer_2 = QSpacerItem(315, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_3)


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
        self.logo.setText(QCoreApplication.translate("Dialog", u"Transaction #0001", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Debtor", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Creditor", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Sent", None))
        self.sent_currency.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Received", None))
        self.recv_currency.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.date.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MM-yyyy", None))
        self.error.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.cancel_btn.setProperty("class", QCoreApplication.translate("Dialog", u"SecondaryButton", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

