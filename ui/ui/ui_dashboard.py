# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(880, 590)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.head_frame = QFrame(Form)
        self.head_frame.setObjectName(u"head_frame")
        self.head_frame.setMinimumSize(QSize(0, 50))
        self.head_frame.setMaximumSize(QSize(16777215, 50))
        self.head_frame.setFrameShape(QFrame.StyledPanel)
        self.head_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.head_frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.head_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 0))
        self.label.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.head_frame)

        self.table_frame = QFrame(Form)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.table_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.table_frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.income_frame = QFrame(self.top_frame)
        self.income_frame.setObjectName(u"income_frame")
        self.income_frame.setMaximumSize(QSize(250, 16777215))
        self.income_frame.setFrameShape(QFrame.StyledPanel)
        self.income_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.income_frame)

        self.outcome_frame = QFrame(self.top_frame)
        self.outcome_frame.setObjectName(u"outcome_frame")
        self.outcome_frame.setFrameShape(QFrame.StyledPanel)
        self.outcome_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.outcome_frame)


        self.verticalLayout_2.addWidget(self.top_frame)

        self.bot_frame = QFrame(self.table_frame)
        self.bot_frame.setObjectName(u"bot_frame")
        self.bot_frame.setFrameShape(QFrame.StyledPanel)
        self.bot_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.bot_frame)


        self.verticalLayout.addWidget(self.table_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Dashboard", None))
    # retranslateUi

