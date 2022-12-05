# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainVxVuIL.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 700)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(200, 0))
        self.left_frame.setMaximumSize(QSize(200, 16777215))
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo_frame = QFrame(self.left_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMinimumSize(QSize(0, 150))
        self.logo_frame.setMaximumSize(QSize(16777215, 150))
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.logo_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.logo_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"font: 900 16pt \"Segoe UI Black\";")
        self.logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.logo)


        self.verticalLayout.addWidget(self.logo_frame)

        self.menu_frame = QFrame(self.left_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.dashboard_btn = QPushButton(self.menu_frame)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.dashboard_btn)

        self.freelaning_btn = QPushButton(self.menu_frame)
        self.freelaning_btn.setObjectName(u"freelaning_btn")
        self.freelaning_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.freelaning_btn)

        self.freelancing_frame = QFrame(self.menu_frame)
        self.freelancing_frame.setObjectName(u"freelancing_frame")
        self.freelancing_frame.setMinimumSize(QSize(0, 0))
        self.freelancing_frame.setFrameShape(QFrame.StyledPanel)
        self.freelancing_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.freelancing_frame)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.clients_btn = QPushButton(self.freelancing_frame)
        self.clients_btn.setObjectName(u"clients_btn")
        self.clients_btn.setMinimumSize(QSize(0, 40))
#if QT_CONFIG(accessibility)
        self.clients_btn.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)

        self.verticalLayout_4.addWidget(self.clients_btn)

        self.projects_btn = QPushButton(self.freelancing_frame)
        self.projects_btn.setObjectName(u"projects_btn")
        self.projects_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.projects_btn)


        self.verticalLayout_2.addWidget(self.freelancing_frame)

        self.spendings_btn = QPushButton(self.menu_frame)
        self.spendings_btn.setObjectName(u"spendings_btn")
        self.spendings_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.spendings_btn)

        self.banking_btn = QPushButton(self.menu_frame)
        self.banking_btn.setObjectName(u"banking_btn")
        self.banking_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.banking_btn)

        self.banking_frame = QFrame(self.menu_frame)
        self.banking_frame.setObjectName(u"banking_frame")
        self.banking_frame.setMinimumSize(QSize(0, 0))
        self.banking_frame.setFrameShape(QFrame.StyledPanel)
        self.banking_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.banking_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.accounts_btn = QPushButton(self.banking_frame)
        self.accounts_btn.setObjectName(u"accounts_btn")
        self.accounts_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_5.addWidget(self.accounts_btn)

        self.payments_btn = QPushButton(self.banking_frame)
        self.payments_btn.setObjectName(u"payments_btn")
        self.payments_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_5.addWidget(self.payments_btn)

        self.transactions_btn = QPushButton(self.banking_frame)
        self.transactions_btn.setObjectName(u"transactions_btn")
        self.transactions_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_5.addWidget(self.transactions_btn)


        self.verticalLayout_2.addWidget(self.banking_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.menu_frame)

        self.control_frame = QFrame(self.left_frame)
        self.control_frame.setObjectName(u"control_frame")
        self.control_frame.setMinimumSize(QSize(0, 0))
        self.control_frame.setMaximumSize(QSize(16777215, 150))
        self.control_frame.setFrameShape(QFrame.StyledPanel)
        self.control_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.control_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 81, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.quit_btn = QPushButton(self.control_frame)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setMinimumSize(QSize(0, 40))
        self.quit_btn.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.quit_btn)


        self.verticalLayout.addWidget(self.control_frame)


        self.horizontalLayout.addWidget(self.left_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"Erbo\n"
"Wallet", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.freelaning_btn.setText(QCoreApplication.translate("MainWindow", u"Freelancing", None))
        self.clients_btn.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.clients_btn.setProperty("class", QCoreApplication.translate("MainWindow", u"InnerButton", None))
        self.projects_btn.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
        self.projects_btn.setProperty("class", QCoreApplication.translate("MainWindow", u"InnerButton", None))
        self.spendings_btn.setText(QCoreApplication.translate("MainWindow", u"Spendings", None))
        self.banking_btn.setText(QCoreApplication.translate("MainWindow", u"Banking", None))
        self.accounts_btn.setText(QCoreApplication.translate("MainWindow", u"Bank Accounts", None))
        self.accounts_btn.setProperty("class", QCoreApplication.translate("MainWindow", u"InnerButton", None))
        self.payments_btn.setText(QCoreApplication.translate("MainWindow", u"Payments", None))
        self.payments_btn.setProperty("class", QCoreApplication.translate("MainWindow", u"InnerButton", None))
        self.transactions_btn.setText(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.transactions_btn.setProperty("class", QCoreApplication.translate("MainWindow", u"InnerButton", None))
        self.quit_btn.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.quit_btn.setProperty("class", QCoreApplication.translate("MainWindow", u"SecondaryButton", None))
    # retranslateUi

