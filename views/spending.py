from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from datetime import date

from ui import *

from views.table_view import TableView
from views.yes_no_dialog import YesNoDialog
from models import *
from controllers import *

class SpendingView(TableView):
    def __init__(self, main):
        super(SpendingView, self).__init__(main)
        
        # manage UI
        self.add_btn.setText("Add Spending")

        self.title.setText("Spendings")

        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Account", "Category", "Date", "Amount", "Description", ""])

        self.table.setColumnWidth(0, 90)
        self.table.setColumnWidth(1, 90)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(3, 130)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 180)
        self.table.setColumnWidth(6, 90)

        self.search.setText('')
        self.search.hide()

        self.populate()
        
    def populate(self, rid=None, filter=''):
        self.prid = rid
        self.pfilter = filter
        self.table.setRowCount(0)

        if rid == None:
            records = SpendingController.all()
        else:
            records = SpendingController.search_by(rid, filter)
    
        for record in records:
            r = super().add_row()
            self.set_row_content(r, record)

        self.toggle_empty()

    def set_row_content(self, r:int, rec:SpendingModel):
        nm = QTableWidgetItem(SpendingModel.encode(rec.id))
        nm.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 0, nm)

        nam_el = QPushButton(BankAccountModel.encode(rec.account))
        nam_el.setProperty('class', 'LinkButton')
        nam_el.setCursor(Qt.PointingHandCursor)
        nam_el.clicked.connect(lambda: self.main.update_view('bank_account', rec.account, 'id'))
        self.table.setCellWidget(r, 1, nam_el)

        print(rec.category)
        cat_el = QTableWidgetItem(SpendingCategory.code(rec.category).capitalize())
        cat_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 2, cat_el)

        typ_el = QTableWidgetItem(date.strftime(rec.date, "%d %b %Y"))
        typ_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 3, typ_el)

        amt_el = QTableWidgetItem(f"{rec.amount:,.2f} {Currency.code(BankAccountController.get(rec.account).currency).upper()}")
        amt_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 4, amt_el)

        amr_el = QTableWidgetItem(rec.description)
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
        app_selection = AddEditSpendingView(self, SpendingModel())
        app_selection.exec()

    def remove_row(self, r):
        cid = SpendingModel.decode(self.table.item(r, 0).text())

        ynd = YesNoDialog(f"Are you sure to delete payment [{SpendingModel.encode(cid)}]?")
        ynd.exec()
        if ynd.resp == YesNoDialog.Yes:
            self.table.removeRow(r)
            SpendingController.delete(cid)

        self.populate()

    # def edit_row(self, r):
    #     idx = SpendingModel.decode(self.table.item(r, 0).text())
    #     model = SpendingController.get(idx)
    #     app_selection = AddEditSpendingView(self, model, r)
    #     app_selection.exec()

    def toggle_empty(self):
        if self.table.rowCount() == 0:
            self.table.hide()
            self.empty.show()
            if SpendingController.all() == []:
                self.empty.setText("Table is empty! Add elements to it")
            else:
                self.empty.setText("No element found for the current search!")
        else:
            self.table.show()
            self.empty.hide()

class AddEditSpendingView(QDialog, UI_AddEditSpending):
    def __init__(self, caller:SpendingView, model:SpendingModel, row:int=-1) -> None:
        super(AddEditSpendingView, self).__init__()
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
        
        self.amount.setValidator(QDoubleValidator(decimals=2))
        self.amount.setText(f"{model.amount:,.2f}")

        for acc in BankAccountController.all():
            self.account.addItem(acc.code)
        self.account.currentIndexChanged.connect(self.update_currencies)
        self.account.setCurrentText(BankAccountController.get(model.account).code)

        for cat in SpendingCategory.get():
            self.category.addItem(SpendingCategory.code(cat).capitalize())
        self.category.setCurrentText(SpendingCategory.code(model.category).capitalize())

        self.date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date.setDate(QDate(model.date.year, model.date.month, model.date.day))

        self.description.setPlainText(model.description)

        self.logo.setText(f"Spending #{SpendingModel.encode(model.id)}")

    def update_currencies(self):
        self.currency.setText(Currency.code(BankAccountController.search(self.account.currentText(), 'c')[0].currency).upper())
        
    def keyPressEvent(self, event:QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return: self.add_project()
        if event.key() == Qt.Key_Escape: self.close()

    def add_account(self):
        if self.validate():
            self.model.amount = self.amt
            self.model.account = self.acc
            self.model.category = self.cat
            self.model.description = self.dsc
            self.model.date = self.dat
            
            if self.row == -1:
                SpendingController.insert(self.model)
            else:
                SpendingController.update(self.model)
            self.caller.populate(self.caller.prid, self.caller.pfilter)

            self.close()

    def read_values(self):
        self.amt = float(self.amount.text().strip().replace(',', ''))
        self.acc = BankAccountController.search(self.account.currentText(), 'c')[0].id
        qd = self.date.date()
        self.dat = date(qd.year(), qd.month(), qd.day())
        self.cat = SpendingCategory.decode(self.category.currentText().lower())
        self.dsc = self.description.toPlainText()

    def validate(self):
        self.error.setText("")
        self.read_values()

        if self.amount == 0: 
            self.error.setText("Amount should be greater than zero!")
            return False
        
        return True

