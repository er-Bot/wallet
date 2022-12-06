from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from datetime import date

from ui import *

from views.table_view import TableView
from views.yes_no_dialog import YesNoDialog
from models import *
from controllers import *


class PaymentView(TableView):
    def __init__(self, main):
        super(PaymentView, self).__init__(main)
        
        # manage UI
        self.add_btn.setText("Add Payment")

        self.title.setText("Payments")

        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Project", "Account", "Date", "Amount", "Currency", ""])

        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 200)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 100)
        self.table.setColumnWidth(6, 100)

        self.search.setText('')
        self.add_btn.hide()
        self.search.hide()
        self.populate()
        
    def populate(self, rid=None, filter=''):
        self.table.setRowCount(0)

        prompt = self.search.text().strip()
        
        if prompt == '':
            if rid == None:
                records = PaymentController.all()
            else:
                records = PaymentController.search_by(rid, filter)
        else:
            records = PaymentController.search(prompt)

        for record in records:
            r = super().add_row()
            self.set_row_content(r, record)

        self.toggle_empty()

    def set_row_content(self, r:int, rec:PaymentModel):
        nm = QTableWidgetItem(PaymentModel.encode(rec.id))
        nm.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 0, nm)

        nam_el = QPushButton(ProjectModel.encode(rec.project))
        nam_el.setProperty('class', 'LinkButton')
        nam_el.setCursor(Qt.PointingHandCursor)
        nam_el.clicked.connect(lambda: self.main.update_view('project', rec.project, 'id'))
        self.table.setCellWidget(r, 1, nam_el)

        bac_el = QPushButton(BankAccountModel.encode(rec.account))
        bac_el.setProperty('class', 'LinkButton')
        bac_el.setCursor(Qt.PointingHandCursor)
        bac_el.clicked.connect(lambda: self.main.update_view("bank_account", rec.account))
        self.table.setCellWidget(r, 2, bac_el)

        typ_el = QTableWidgetItem(date.strftime(rec.date, "%A %d %B %Y"))
        typ_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 3, typ_el)

        amt_el = QTableWidgetItem(f"{rec.amount:,.2f}")
        amt_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 4, amt_el)

        cur_el = QTableWidgetItem(Currency.code(rec.currency).upper())
        cur_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 5, cur_el)

        wid = QWidget()
        wid.setStyleSheet("border: none;")
        lay = QBoxLayout(QBoxLayout.LeftToRight)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(5)
        
        rb = TableView.button(DELETE_ICON)
        rb.setToolTip("Remove payment")
        rb.clicked.connect(lambda: self.remove_row(r))
        
        lay.addWidget(rb, Qt.AlignCenter)        
        wid.setLayout(lay)

        self.table.setCellWidget(r, self.table.columnCount() - 1, wid)

    def remove_row(self, r):
        cid = PaymentModel.decode(self.table.cellWidget(r, 0).text())

        ynd = YesNoDialog(f"Are you sure to delete payment [{PaymentModel.encode(cid)}]?")
        ynd.exec()
        if ynd.resp == YesNoDialog.Yes:
            self.table.removeRow(r)
            PaymentController.delete(cid)

        self.populate()

    def toggle_empty(self):
        if self.table.rowCount() == 0:
            self.table.hide()
            self.empty.show()
            if PaymentController.all() == []:
                self.empty.setText("Table is empty! Add elements to it")
            else:
                self.empty.setText("No element found for the current search!")
        else:
            self.table.show()
            self.empty.hide()
