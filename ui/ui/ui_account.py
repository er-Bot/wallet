# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(584, 250)
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
        self.horizontalLayout_3.setSpacing(0)
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

        self.name = QLineEdit(self.frame)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(200, 30))
        self.name.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_3.addWidget(self.name)


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
        self.label_2.setMaximumSize(QSize(75, 16777215))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.code = QLineEdit(self.frame_4)
        self.code.setObjectName(u"code")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.code.sizePolicy().hasHeightForWidth())
        self.code.setSizePolicy(sizePolicy)
        self.code.setMinimumSize(QSize(200, 30))
        self.code.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_4.addWidget(self.code)


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
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(75, 0))
        self.label_5.setMaximumSize(QSize(75, 16777215))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.atype = QComboBox(self.frame_5)
        self.atype.addItem("")
        self.atype.addItem("")
        self.atype.setObjectName(u"atype")
        sizePolicy.setHeightForWidth(self.atype.sizePolicy().hasHeightForWidth())
        self.atype.setSizePolicy(sizePolicy)
        self.atype.setMinimumSize(QSize(200, 30))
        self.atype.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_5.addWidget(self.atype)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.contact_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.amo = QLabel(self.frame_6)
        self.amo.setObjectName(u"amo")
        self.amo.setMinimumSize(QSize(75, 0))
        self.amo.setMaximumSize(QSize(75, 16777215))
        self.amo.setFont(font)
        self.amo.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.amo)

        self.amount = QLineEdit(self.frame_6)
        self.amount.setObjectName(u"amount")
        sizePolicy.setHeightForWidth(self.amount.sizePolicy().hasHeightForWidth())
        self.amount.setSizePolicy(sizePolicy)
        self.amount.setMinimumSize(QSize(110, 30))
        self.amount.setMaximumSize(QSize(110, 30))
        self.amount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.amount)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.currency = QComboBox(self.frame_6)
        self.currency.addItem("")
        self.currency.addItem("")
        self.currency.setObjectName(u"currency")
        sizePolicy.setHeightForWidth(self.currency.sizePolicy().hasHeightForWidth())
        self.currency.setSizePolicy(sizePolicy)
        self.currency.setMinimumSize(QSize(80, 30))
        self.currency.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_6.addWidget(self.currency)


        self.horizontalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.contact_frame)


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
        self.logo.setText(QCoreApplication.translate("Dialog", u"Bank Account #0001", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Code", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.atype.setItemText(0, QCoreApplication.translate("Dialog", u"Checking", None))
        self.atype.setItemText(1, QCoreApplication.translate("Dialog", u"Savings", None))

        self.amo.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.currency.setItemText(0, QCoreApplication.translate("Dialog", u"USD", None))
        self.currency.setItemText(1, QCoreApplication.translate("Dialog", u"MAD", None))

        self.error.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.cancel_btn.setProperty("class", QCoreApplication.translate("Dialog", u"SecondaryButton", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

