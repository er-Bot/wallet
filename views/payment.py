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
        self.prid = rid
        self.pfilter = filter
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
        
        eb = TableView.button(EDIT_ICON, light=True)
        eb.setToolTip("Edit payment")
        eb.clicked.connect(lambda: self.edit_row(r))
        
        lay.addWidget(eb, Qt.AlignCenter)        
        lay.addWidget(rb, Qt.AlignCenter)        
        wid.setLayout(lay)

        self.table.setCellWidget(r, self.table.columnCount() - 1, wid)

    def remove_row(self, r):
        cid = PaymentModel.decode(self.table.item(r, 0).text())

        ynd = YesNoDialog(f"Are you sure to delete payment [{PaymentModel.encode(cid)}]?")
        ynd.exec()
        if ynd.resp == YesNoDialog.Yes:
            self.table.removeRow(r)
            PaymentController.delete(cid)

        self.populate()

    def edit_row(self, r):
        idx = PaymentModel.decode(self.table.item(r, 0).text())
        model = PaymentController.get(idx)
        app_selection = EditPaymentView(self, model, r)
        app_selection.exec()

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

class EditPaymentView(QDialog, UI_EditPayment):
    def __init__(self, caller:PaymentView, model:PaymentModel, row:int=-1) -> None:
        super(EditPaymentView, self).__init__()
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
        self.currency.setText(Currency.code(model.currency).upper())

        self.date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date.setDate(QDate(model.date.year, model.date.month, model.date.day))

        self.logo.setText(f"Payment #{PaymentModel.encode(model.id)}")

    def keyPressEvent(self, event:QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return: self.add_project()
        if event.key() == Qt.Key_Escape: self.close()

    def add_account(self):
        if self.validate():
            self.model.amount = self.amt
            self.model.date = self.dat
            
            PaymentController.update(self.model)
            self.caller.populate(self.caller.prid, self.caller.pfilter)

            self.close()

    def read_values(self):
        self.amt = float(self.amount.text().strip().replace(',', ''))
        qd = self.date.date()
        self.dat = date(qd.year(), qd.month(), qd.day())

    def validate(self):
        self.error.setText("")
        self.read_values()

        if self.amt == 0: 
            self.error.setText("Amount should be greater than zero!")
            return False
        
        if self.dat < ProjectController.get(self.model.project).start_date:
            self.error.setText(f"Payment date is older than project start date!")
            return False

        return True

