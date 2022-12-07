from datetime import date
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui import STYLE_SHEET, UI_Dashboard
from controllers import *
from models import *

class DashboardView(QWidget, UI_Dashboard):
    def __init__(self, main):
        super(DashboardView, self).__init__()

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        # self.clients.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.clients.setSelectionMode(QAbstractItemView.NoSelection)
        # self.projects.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.projects.setSelectionMode(QAbstractItemView.NoSelection)

        with open(STYLE_SHEET) as sc:
            self.setStyleSheet(sc.read())

        self.main = main
    
    def populate(self, rid=None, filter=''):
        self.vb = QVBoxLayout(self.income_frame)
        self.vb.setContentsMargins(0, 0, 0, 0)
        self.vb.setSpacing(5)

        # income part
        self.make_attribute("Month's Income :", f"{DashboardController.count_profit_by_project(ProjectController.all()):,.2f} USD")
        l = DashboardController.count_profit_by_account()
        for k, v in l.items():
            if k == "FVRR":
                self.make_attribute(f"{k} :", f"{.8*v['total']:,.2f} {Currency.code(v['currency']).upper()}")
            else:
                self.make_attribute(f"{k} :", f"{v['total']:,.2f} {Currency.code(v['currency']).upper()}")
        
        spacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vb.addItem(spacer)

    def make_attribute(self, attr, val):
        attr_frame = QFrame(self.income_frame)
        attr_frame.setFrameShape(QFrame.StyledPanel)
        attr_frame.setFrameShadow(QFrame.Raised)
        hb = QHBoxLayout(attr_frame)
        hb.setSpacing(5)
        hb.setContentsMargins(0,0,0,0)
        albl = QLabel(attr_frame)
        albl.setText(attr)
        albl.setStyleSheet('font: 700 9pt "Segoe UI";')
        hb.addWidget(albl)
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hb.addItem(spacer)
        vlbl = QLabel(attr_frame)
        vlbl.setText(val)
        hb.addWidget(vlbl)
        self.vb.addWidget(attr_frame)