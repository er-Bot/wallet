# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardzoeAXc.ui'
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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.statistics = QFrame(self.table_frame)
        self.statistics.setObjectName(u"statistics")
        self.statistics.setFrameShape(QFrame.StyledPanel)
        self.statistics.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.statistics)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.statistics)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(21, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.lm_income = QLabel(self.frame_4)
        self.lm_income.setObjectName(u"lm_income")
        self.lm_income.setMinimumSize(QSize(100, 0))
        self.lm_income.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.lm_income.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lm_income)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, 0)
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(122, 0))
        self.label_8.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.paypal_bal = QLabel(self.frame_6)
        self.paypal_bal.setObjectName(u"paypal_bal")
        self.paypal_bal.setMinimumSize(QSize(100, 0))
        self.paypal_bal.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.paypal_bal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.paypal_bal)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, 0, 0)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(122, 0))
        self.label_9.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.fiverr_bal = QLabel(self.frame_7)
        self.fiverr_bal.setObjectName(u"fiverr_bal")
        self.fiverr_bal.setMinimumSize(QSize(100, 0))
        self.fiverr_bal.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.fiverr_bal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.fiverr_bal)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, 0, 0)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.horizontalSpacer_4 = QSpacerItem(59, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.lm_projects = QLabel(self.frame_5)
        self.lm_projects.setObjectName(u"lm_projects")
        self.lm_projects.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.lm_projects)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.statistics)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.statistics)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.statistics)

        self.client_projects = QFrame(self.table_frame)
        self.client_projects.setObjectName(u"client_projects")
        self.client_projects.setMaximumSize(QSize(16777215, 200))
        self.client_projects.setFrameShape(QFrame.StyledPanel)
        self.client_projects.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.client_projects)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_clients = QFrame(self.client_projects)
        self.top_clients.setObjectName(u"top_clients")
        self.top_clients.setFrameShape(QFrame.StyledPanel)
        self.top_clients.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.top_clients)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.clients_empty = QLabel(self.top_clients)
        self.clients_empty.setObjectName(u"clients_empty")

        self.horizontalLayout_4.addWidget(self.clients_empty)

        self.clients = QTableWidget(self.top_clients)
        self.clients.setObjectName(u"clients")

        self.horizontalLayout_4.addWidget(self.clients)


        self.horizontalLayout_2.addWidget(self.top_clients)

        self.ongoing_projects = QFrame(self.client_projects)
        self.ongoing_projects.setObjectName(u"ongoing_projects")
        self.ongoing_projects.setFrameShape(QFrame.StyledPanel)
        self.ongoing_projects.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.ongoing_projects)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.projects_empty = QLabel(self.ongoing_projects)
        self.projects_empty.setObjectName(u"projects_empty")

        self.horizontalLayout_5.addWidget(self.projects_empty)

        self.projects = QTableWidget(self.ongoing_projects)
        self.projects.setObjectName(u"projects")

        self.horizontalLayout_5.addWidget(self.projects)


        self.horizontalLayout_2.addWidget(self.ongoing_projects)


        self.verticalLayout_2.addWidget(self.client_projects)


        self.verticalLayout.addWidget(self.table_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Last Month Income:", None))
        self.lm_income.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"PayPal :", None))
        self.paypal_bal.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Fiverr :", None))
        self.fiverr_bal.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Last Month Projects:", None))
        self.lm_projects.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.clients_empty.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.projects_empty.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

