from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys

from ui import UI_Main, STYLE_SHEET
from views import DashboardView, ClientView, BankAccountView, PaymentView, ProjectView

class MainWindow(QMainWindow, UI_Main):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Erbo Wallet")
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        with open(STYLE_SHEET) as sc:
            self.setStyleSheet(sc.read())

        # reduce expendables
        self.freelancing_frame.hide()
        self.banking_frame.hide()

        # left menu button actions
        self.freelaning_btn.clicked.connect(lambda : self.expand('freelancing'))
        self.banking_btn.clicked.connect(lambda : self.expand('banking'))
        
        self.dashboard_btn.clicked.connect(lambda : self.update_view("dashboard"))
        self.clients_btn.clicked.connect(lambda : self.update_view("client"))
        self.accounts_btn.clicked.connect(lambda : self.update_view("bank_account"))
        self.payments_btn.clicked.connect(lambda : self.update_view("payment"))
        self.projects_btn.clicked.connect(lambda : self.update_view("project"))
        
        self.quit_btn.clicked.connect(self.quit)

        
        self.expandables = {
            'freelancing': self.freelancing_frame,
            'banking': self.banking_frame,
        }

        self.tables = {
            "dashboard": DashboardView(self),
            "client": ClientView(self),
            "bank_account": BankAccountView(self),
            "payment": PaymentView(self),
            "project": ProjectView(self),
        }

        self.view_layout = QVBoxLayout()
        for k in self.tables:
            self.view_layout.addWidget(self.tables[k])
        self.main_frame.setLayout(self.view_layout)

        self.update_view("project")

    def update_view(self, k, rid=None, filter=''):
        for _, v in self.tables.items():
            v.hide()

        self.tables[k].populate(rid, filter)
        self.tables[k].show()

    def expand(self, k):
        for _, v in self.expandables.items():
            v.hide()

        self.expandables[k].show()

    def quit(self):
        # ynd = YesNoDialog("Quit FreeMan?")
        # ynd.exec()
        # if ynd.resp == YesNoDialog.Yes:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
