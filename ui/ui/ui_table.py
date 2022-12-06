# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tableVSJgiQ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

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
        self.head_frame.setMinimumSize(QSize(0, 75))
        self.head_frame.setMaximumSize(QSize(16777215, 75))
        self.head_frame.setFrameShape(QFrame.StyledPanel)
        self.head_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.head_frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.head_frame)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(200, 0))
        self.title.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.title)

        self.horizontalSpacer_2 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.search = QLineEdit(self.head_frame)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(300, 30))
        self.search.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_3.addWidget(self.search)

        self.clear_btn = QPushButton(self.head_frame)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setMinimumSize(QSize(75, 30))
        self.clear_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.clear_btn)


        self.verticalLayout.addWidget(self.head_frame)

        self.table_frame = QFrame(Form)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.table_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.empty = QLabel(self.table_frame)
        self.empty.setObjectName(u"empty")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.empty.sizePolicy().hasHeightForWidth())
        self.empty.setSizePolicy(sizePolicy)
        self.empty.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.empty.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.empty)

        self.table = QTableWidget(self.table_frame)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setDragEnabled(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(40)

        self.horizontalLayout_2.addWidget(self.table)


        self.verticalLayout.addWidget(self.table_frame)

        self.control_frame = QFrame(Form)
        self.control_frame.setObjectName(u"control_frame")
        self.control_frame.setMaximumSize(QSize(16777215, 70))
        self.control_frame.setFrameShape(QFrame.StyledPanel)
        self.control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.control_frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.error = QLabel(self.control_frame)
        self.error.setObjectName(u"error")
        self.error.setMinimumSize(QSize(500, 0))
        self.error.setStyleSheet(u"font: 700 8pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.error)

        self.horizontalSpacer = QSpacerItem(213, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_btn = QPushButton(self.control_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(150, 40))

        self.horizontalLayout.addWidget(self.add_btn)


        self.verticalLayout.addWidget(self.control_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.search.setPlaceholderText(QCoreApplication.translate("Form", u"Search...", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.clear_btn.setProperty("class", QCoreApplication.translate("Form", u"SecondaryButton", None))
        self.empty.setText(QCoreApplication.translate("Form", u"Table is empty!", None))
        self.error.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
    # retranslateUi

