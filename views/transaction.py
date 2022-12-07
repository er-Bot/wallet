from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from datetime import date

from ui import *

from views.table_view import TableView
from views.yes_no_dialog import YesNoDialog
from models import *
from controllers import *

class TransactionView(TableView):
    def __init__(self, main):
        super(TransactionView, self).__init__(main)
        
        # manage UI
        self.add_btn.setText("Add Transaction")

        self.title.setText("Transactions")

        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Debtor", "Creditor", "Date", "Sent", "Received", ""])

        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 100)

        self.search.setText('')
        self.search.hide()

        self.populate()
        
    def populate(self, rid=None, filter=''):
        self.prid = rid
        self.pfilter = filter
        self.table.setRowCount(0)

        if rid == None:
            records = TransactionController.all()
        else:
            records = TransactionController.search_by(rid, filter)
    
        for record in records:
            r = super().add_row()
            self.set_row_content(r, record)

        self.toggle_empty()

    def set_row_content(self, r:int, rec:TransactionModel):
        nm = QTableWidgetItem(TransactionModel.encode(rec.id))
        nm.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 0, nm)

        nam_el = QPushButton(BankAccountModel.encode(rec.debtor))
        nam_el.setProperty('class', 'LinkButton')
        nam_el.setCursor(Qt.PointingHandCursor)
        nam_el.clicked.connect(lambda: self.main.update_view('bank_account', rec.debtor, 'id'))
        self.table.setCellWidget(r, 1, nam_el)

        bac_el = QPushButton(BankAccountModel.encode(rec.creditor))
        bac_el.setProperty('class', 'LinkButton')
        bac_el.setCursor(Qt.PointingHandCursor)
        bac_el.clicked.connect(lambda: self.main.update_view("bank_account", rec.creditor))
        self.table.setCellWidget(r, 2, bac_el)

        typ_el = QTableWidgetItem(date.strftime(rec.date, "%d %b %Y"))
        typ_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 3, typ_el)

        amt_el = QTableWidgetItem(f"{rec.sent:,.2f} {Currency.code(BankAccountController.get(rec.debtor).currency).upper()}")
        amt_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 4, amt_el)

        amr_el = QTableWidgetItem(f"{rec.received:,.2f} {Currency.code(BankAccountController.get(rec.creditor).currency).upper()}")
        amr_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 5, amr_el)

        wid = QWidget()
        wid.setStyleSheet("border: none;")
        lay = QBoxLayout(QBoxLayout.LeftToRight)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(5)
        
        rb = TableView.button(DELETE_ICON)
        rb.setToolTip("Remove transaction")
        rb.clicked.connect(lambda: self.remove_row(r))
        
        eb = TableView.button(EDIT_ICON, light=True)
        eb.setToolTip("Edit transaction")
        eb.clicked.connect(lambda: self.edit_row(r))
        
        lay.addWidget(eb, Qt.AlignCenter)        
        lay.addWidget(rb, Qt.AlignCenter)        
        wid.setLayout(lay)

        self.table.setCellWidget(r, self.table.columnCount() - 1, wid)

    def add_row(self):
        app_selection = AddEditTransactionView(self, TransactionModel())
        app_selection.exec()

    def remove_row(self, r):
        cid = TransactionModel.decode(self.table.item(r, 0).text())

        ynd = YesNoDialog(f"Are you sure to delete payment [{TransactionModel.encode(cid)}]?")
        ynd.exec()
        if ynd.resp == YesNoDialog.Yes:
            self.table.removeRow(r)
            TransactionController.delete(cid)

        self.populate()

    def edit_row(self, r):
        idx = TransactionModel.decode(self.table.item(r, 0).text())
        model = TransactionController.get(idx)
        app_selection = AddEditTransactionView(self, model, r)
        app_selection.exec()

    def toggle_empty(self):
        if self.table.rowCount() == 0:
            self.table.hide()
            self.empty.show()
            if TransactionController.all() == []:
                self.empty.setText("Table is empty! Add elements to it")
            else:
                self.empty.setText("No element found for the current search!")
        else:
            self.table.show()
            self.empty.hide()

class AddEditTransactionView(QDialog, UI_AddEditTransaction):
    def __init__(self, caller:TransactionView, model:TransactionModel, row:int=-1) -> None:
        super(AddEditTransactionView, self).__init__()
        self.caller = caller
        self.model = model
        self.row = row

        # Set ui
        self.setupUi(self) 
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.error.setText("")
        with open(STYLE_SHEET) as sc:
            self.setStyleSheet(sc.read())
        
        self.cancel_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.add_account)
        
        self.sent_amount.setValidator(QDoubleValidator(decimals=2))
        self.recv_amount.setValidator(QDoubleValidator(decimals=2))
        self.sent_amount.setText(f"{model.sent:,.2f}")
        self.recv_amount.setText(f"{model.received:,.2f}")
        for acc in BankAccountController.all():
            self.debtor.addItem(acc.code)
            self.creditor.addItem(acc.code)
        
        self.debtor.currentIndexChanged.connect(self.update_currencies)
        self.creditor.currentIndexChanged.connect(self.update_currencies)

        if model.debtor != -1:
            self.debtor.setCurrentText(BankAccountController.get(model.debtor).code)
            self.creditor.setCurrentText(BankAccountController.get(model.creditor).code)
        else:
            self.update_currencies()
            
        self.date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date.setDate(QDate(model.date.year, model.date.month, model.date.day))

        self.logo.setText(f"Transaction #{TransactionModel.encode(model.id)}")

    def update_currencies(self):
        self.sent_currency.setText(Currency.code(BankAccountController.search(self.debtor.currentText(), 'c')[0].currency).upper())
        self.recv_currency.setText(Currency.code(BankAccountController.search(self.creditor.currentText(), 'c')[0].currency).upper())


    def keyPressEvent(self, event:QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return: self.add_project()
        if event.key() == Qt.Key_Escape: self.close()

    def add_account(self):
        if self.validate():
            self.model.sent = self.sam
            self.model.received = self.ram
            self.model.debtor = self.sac
            self.model.creditor = self.rac
            self.model.date = self.dat
            
            if self.row == -1:
                TransactionController.insert(self.model)
            else:
                TransactionController.update(self.model)
            self.caller.populate(self.caller.prid, self.caller.pfilter)

            self.close()

    def read_values(self):
        self.sam = float(self.sent_amount.text().strip().replace(',', ''))
        self.ram = float(self.recv_amount.text().strip().replace(',', ''))
        self.sac = BankAccountController.search(self.debtor.currentText(), 'c')[0].id
        self.rac = BankAccountController.search(self.creditor.currentText(), 'c')[0].id
        qd = self.date.date()
        self.dat = date(qd.year(), qd.month(), qd.day())

    def validate(self):
        self.error.setText("")
        self.read_values()

        if self.sam == 0 or self.ram == 0: 
            self.error.setText("Amounts should be greater than zero!")
            return False
        
        return True

