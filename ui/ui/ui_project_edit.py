# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_editbyygHF.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDialog, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(688, 550)
        Dialog.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dialog_window = QFrame(Dialog)
        self.dialog_window.setObjectName(u"dialog_window")
        self.dialog_window.setFrameShape(QFrame.StyledPanel)
        self.dialog_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.dialog_window)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.title_frame = QFrame(self.dialog_window)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMinimumSize(QSize(0, 60))
        self.title_frame.setMaximumSize(QSize(16777215, 60))
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.title_frame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.title_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"font: 900 16pt \"Segoe UI Black\";")
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.logo)


        self.verticalLayout_5.addWidget(self.title_frame)

        self.frame_5 = QFrame(self.dialog_window)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(80, 0))
        self.label_10.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_17.addWidget(self.label_10)

        self.title = QLineEdit(self.frame_8)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QSize(200, 30))
        self.title.setMaximumSize(QSize(1000, 30))

        self.horizontalLayout_17.addWidget(self.title)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.name_frame = QFrame(self.frame_5)
        self.name_frame.setObjectName(u"name_frame")
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.name_frame)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.name_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(1000, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(80, 0))
        self.label_12.setMaximumSize(QSize(80, 16777215))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_20.addWidget(self.label_12)

        self.price = QLineEdit(self.frame_10)
        self.price.setObjectName(u"price")
        sizePolicy.setHeightForWidth(self.price.sizePolicy().hasHeightForWidth())
        self.price.setSizePolicy(sizePolicy)
        self.price.setMinimumSize(QSize(150, 30))
        self.price.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_20.addWidget(self.price)

        self.currency = QComboBox(self.frame_10)
        self.currency.setObjectName(u"currency")
        self.currency.setMinimumSize(QSize(80, 30))
        self.currency.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_20.addWidget(self.currency)


        self.horizontalLayout_18.addWidget(self.frame_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.frame_7 = QFrame(self.name_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(200, 0))
        self.frame_7.setMaximumSize(QSize(1000, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(80, 16777215))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_16.addWidget(self.label_7)

        self.state = QComboBox(self.frame_7)
        self.state.setObjectName(u"state")
        self.state.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_16.addWidget(self.state)


        self.horizontalLayout_18.addWidget(self.frame_7)


        self.verticalLayout_8.addWidget(self.name_frame)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))
        self.label_5.setMaximumSize(QSize(80, 16777215))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.start_date = QDateEdit(self.frame_11)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setMinimumSize(QSize(30, 30))
        self.start_date.setMaximumSize(QSize(1000, 16777215))
        self.start_date.setCurrentSection(QDateTimeEdit.DaySection)
        self.start_date.setCalendarPopup(False)

        self.horizontalLayout_6.addWidget(self.start_date)


        self.horizontalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_12)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))
        self.label.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label)

        self.due_date = QDateEdit(self.frame_12)
        self.due_date.setObjectName(u"due_date")
        self.due_date.setMinimumSize(QSize(30, 30))
        self.due_date.setMaximumSize(QSize(1000, 16777215))
        self.due_date.setCurrentSection(QDateTimeEdit.DaySection)
        self.due_date.setCalendarPopup(False)

        self.horizontalLayout_4.addWidget(self.due_date)


        self.horizontalLayout_5.addWidget(self.frame_12)

        self.end_date_frame = QFrame(self.frame_9)
        self.end_date_frame.setObjectName(u"end_date_frame")
        self.end_date_frame.setMinimumSize(QSize(218, 0))
        self.end_date_frame.setMaximumSize(QSize(218, 16777215))
        self.end_date_frame.setFrameShape(QFrame.StyledPanel)
        self.end_date_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.end_date_frame)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.end_date_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))
        self.label_6.setMaximumSize(QSize(80, 16777215))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_19.addWidget(self.label_6)

        self.end_date = QDateEdit(self.end_date_frame)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setMinimumSize(QSize(30, 30))
        self.end_date.setMaximumSize(QSize(1000, 16777215))
        self.end_date.setCurrentSection(QDateTimeEdit.DaySection)
        self.end_date.setCalendarPopup(False)

        self.horizontalLayout_19.addWidget(self.end_date)


        self.horizontalLayout_5.addWidget(self.end_date_frame)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 0))
        self.label_8.setMaximumSize(QSize(80, 16777215))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.description = QPlainTextEdit(self.frame)
        self.description.setObjectName(u"description")

        self.horizontalLayout_12.addWidget(self.description)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 60))
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 0))
        self.label_9.setMaximumSize(QSize(80, 16777215))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.comment = QPlainTextEdit(self.frame_4)
        self.comment.setObjectName(u"comment")

        self.horizontalLayout_3.addWidget(self.comment)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 1000000))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.payments = QTableWidget(self.frame_2)
        self.payments.setObjectName(u"payments")
        self.payments.setMinimumSize(QSize(50, 80))
        self.payments.setMaximumSize(QSize(1000000, 16777215))
        self.payments.horizontalHeader().setVisible(True)
        self.payments.horizontalHeader().setMinimumSectionSize(30)
        self.payments.horizontalHeader().setStretchLastSection(True)
        self.payments.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.payments)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.account = QComboBox(self.frame_3)
        self.account.setObjectName(u"account")
        self.account.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_2.addWidget(self.account)

        self.amount = QLineEdit(self.frame_3)
        self.amount.setObjectName(u"amount")
        self.amount.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.amount)

        self.payment_currency = QComboBox(self.frame_3)
        self.payment_currency.setObjectName(u"payment_currency")
        self.payment_currency.setMinimumSize(QSize(80, 30))
        self.payment_currency.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.payment_currency)

        self.payment_date = QDateEdit(self.frame_3)
        self.payment_date.setObjectName(u"payment_date")
        self.payment_date.setMinimumSize(QSize(131, 30))

        self.horizontalLayout_2.addWidget(self.payment_date)

        self.add_pay = QPushButton(self.frame_3)
        self.add_pay.setObjectName(u"add_pay")
        self.add_pay.setMinimumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.add_pay)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.control_frame = QFrame(self.dialog_window)
        self.control_frame.setObjectName(u"control_frame")
        self.control_frame.setMinimumSize(QSize(0, 50))
        self.control_frame.setMaximumSize(QSize(16777215, 50))
        self.control_frame.setFrameShape(QFrame.StyledPanel)
        self.control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.control_frame)
        self.horizontalLayout.setSpacing(5)
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


        self.verticalLayout_5.addWidget(self.control_frame)


        self.verticalLayout.addWidget(self.dialog_window)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.logo.setText(QCoreApplication.translate("Dialog", u"Project #0001", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Title", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Price", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"State", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Start Date", None))
        self.start_date.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MM-yyyy", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Due Date", None))
        self.due_date.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MM-yyyy", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Delivery Date", None))
        self.end_date.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MM-yyyy", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Comment", None))
        self.amount.setPlaceholderText(QCoreApplication.translate("Dialog", u"Amount...", None))
        self.payment_date.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MM-yyyy", None))
        self.add_pay.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.error.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.cancel_btn.setProperty("class", QCoreApplication.translate("Dialog", u"SecondaryButton", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

