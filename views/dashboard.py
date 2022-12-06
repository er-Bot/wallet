from datetime import date
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui import STYLE_SHEET, UI_Dashboard

class DashboardView(QWidget, UI_Dashboard):
    def __init__(self, main):
        super(DashboardView, self).__init__()

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.clients.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.clients.setSelectionMode(QAbstractItemView.NoSelection)
        self.projects.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.projects.setSelectionMode(QAbstractItemView.NoSelection)

        with open(STYLE_SHEET) as sc:
            self.setStyleSheet(sc.read())

        self.main = main
    
    def populate(self, rid=None, filter=''):
        last_month_income = 0
        paypl = 0
        fiver = 0
        first_day = date.today().replace(day=1)
        # prjs = list(ProjectController.findByDate(first_day).values())
        # print(len(prjs))
        # for prj in prjs:
        #     for pym in prj.payments:
        #         if pym.date >= first_day:
        #             last_month_income += pym.received
        #             if pym.method == PaymentMethod.Fiverr: fiver += pym.received
        #             elif pym.method == PaymentMethod.Paypal: paypl += pym.received
        # self.lm_income.setText(f"{last_month_income:.2f} $")
        # self.paypal_bal.setText(f"{paypl:.2f} $")
        # self.fiverr_bal.setText(f"{fiver:.2f} $")
        # self.lm_projects.setText(f"{len(prjs)}")