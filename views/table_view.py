from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui import UI_Table, STYLE_SHEET

class TableView(QWidget, UI_Table):
    def __init__(self, main):
        super(TableView, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)

        with open(STYLE_SHEET) as sc:
            self.setStyleSheet(sc.read())

        self.add_btn.clicked.connect(self.add_row)
        self.clear_btn.clicked.connect(self.populate)
        self.search.textChanged.connect(self.populate)

        self.error.setText("")
        self.main = main

    def add_row(self):
        r = self.table.rowCount()
        self.table.setRowCount(r + 1)

        return r

    def remove_row(self, r):
        self.table.removeRow(r)

    def edit_row(self, r):
        raise NotImplemented("method not yet implemented!")

    def populate(self, id=None, filter=''):
        raise NotImplemented("method not yet implemented!")

    def button(icon, light=False):
        b = QPushButton(QIcon(icon), "")
        b.setFixedSize(30, 30)
        if light:
            b.setStyleSheet("QPushButton {background: #545454;} QPushButton:hover {background: #747474;}")
        return b
        
