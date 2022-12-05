from PySide6.QtWidgets import *
from PySide6.QtCore import *

from ui import UI_Yes_No_Dialog, STYLE_SHEET

class YesNoDialog(QDialog, UI_Yes_No_Dialog):
    Yes = 0
    No = 1

    def __init__(self, prompt):
        super(YesNoDialog, self).__init__()

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        with open(STYLE_SHEET) as sc:
            self.setStyleSheet(sc.read())

        self.logo.setText(prompt)

        self.cancel_btn.clicked.connect(lambda: self.response(YesNoDialog.No))
        self.save_btn.clicked.connect(lambda: self.response(YesNoDialog.Yes))

    def response(self, resp):
        self.resp = resp
        self.accept()