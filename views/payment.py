from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from datetime import date

from ui import UI_AddEditAccount, STYLE_SHEET

from views.table_view import TableView
from views.yes_no_dialog import YesNoDialog
from models import PaymentModel, AccountType, Currency, ClientModel, BankAccountModel
from controllers import PaymentController


class PaymentView(TableView):
    def __init__(self, main):
        super(PaymentView, self).__init__(main)
        
        # manage UI
        self.add_btn.setText("Add Payment")

        self.title.setText("Payments")

        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Client", "Account", "Date", "Amount", "Currency", ""])

        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 180)
        self.table.setColumnWidth(4, 180)
        self.table.setColumnWidth(5, 100)
        self.table.setColumnWidth(6, 120)

        self.search.setText('')
        self.populate()
        
    def populate(self):
        self.table.setRowCount(0)

        prompt = self.search.text().strip()
        
        if prompt == '':
            records = PaymentController.all()
        else:
            records = PaymentController.search(prompt)

        for record in records:
            r = super().add_row()
            self.set_row_content(r, record)

        self.toggle_empty()

    def set_row_content(self, r:int, rec:PaymentModel):
        nm = QTableWidgetItem(PaymentModel.encode(rec.id))
        self.table.setItem(r, 0, nm)

        nam_el = QPushButton(ClientModel.encode(rec.client))
        nam_el.setProperty('class', 'LinkButton')
        nam_el.setCursor(Qt.PointingHandCursor)
        nam_el.clicked.connect(lambda: self.main.update_view("client", rec.client))
        self.table.setCellWidget(r, 1, nam_el)

        cod_el = QTableWidgetItem(BankAccountModel.encode(rec.account))
        cod_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 2, cod_el)

        typ_el = QTableWidgetItem(date.strftime(rec.date, "%d %b %Y"))
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
        
        rb = TableView.remove_button()
        rb.setToolTip("Remove payment")
        rb.clicked.connect(lambda: self.remove_row(r))
        
        eb = TableView.edit_button()
        eb.setToolTip("Edit payment")
        eb.clicked.connect(lambda: self.edit_row(r))

        lay.addWidget(eb, Qt.AlignCenter)        
        lay.addWidget(rb, Qt.AlignCenter)        
        wid.setLayout(lay)

        self.table.setCellWidget(r, self.table.columnCount() - 1, wid)

    def add_row(self):
        pass
        # app_selection = AddEditAccountView(self, PaymentModel())
        # app_selection.exec()
                
    def edit_row(self, r):
        pass
        # idx = PaymentModel.decode(self.table.item(r, 0).text())
        # model = PaymentController.get(idx)
        # app_selection = AddEditAccountView(self, model, r)
        # app_selection.exec()

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

# class AddEditPaymentView(QDialog, UI_AddEditAccount):
#     def __init__(self, caller:PaymentView, model:PaymentModel, row:int=-1) -> None:
#         super(AddEditAccountView, self).__init__()
#         self.caller = caller
#         self.model = model
#         self.row = row

#         # Set ui
#         self.setupUi(self) 
#         self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
#         self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#         self.error.setText("")
#         with open(STYLE_SHEET) as sc:
#             self.setStyleSheet(sc.read())
        
#         self.cancel_btn.clicked.connect(self.close)
#         self.save_btn.clicked.connect(self.add_account)
        
#         self.name.setText(model.name)
#         self.code.setText(model.code.upper())
#         self.atype.setCurrentText(AccountType.code(model.type).capitalize())
#         self.currency.setCurrentText(Currency.code(model.currency).upper())
#         self.amount.setText(f"{model.amount:,.2f}")

#         self.logo.setText(f"Payment #{PaymentModel.encode(model.id)}")

#     def keyPressEvent(self, event:QKeyEvent) -> None:
#         if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return: self.add_project()
#         if event.key() == Qt.Key_Escape: self.close()

#     def add_account(self):
#         if self.validate():
#             self.model.name = self.nam
#             self.model.code = self.cod
#             self.model.type = AccountType.decode(self.atp)
#             self.model.currency = Currency.decode(self.cur)
#             self.model.amount = self.amt
            
#             if self.row == -1:
#                 PaymentController.insert(self.model)
#             else:
#                 PaymentController.update(self.model)
#             self.caller.populate()

#             self.close()

#     def read_values(self):
#         self.nam = self.name.text().strip()
#         self.cod = self.code.text().strip()
#         self.atp = self.atype.currentText().lower()
#         self.cur = self.currency.currentText().lower()
#         self.amt = float(self.amount.text().strip().replace(',', ''))

#     def validate(self):
#         self.error.setText("")
#         self.read_values()

#         if self.nam == "": 
#             self.error.setText("The field 'name' should not be empty!")
#             return False
#         else:
#             if PaymentController.exists(self.nam, filter='n', ignore=[self.model.id]):
#                 self.error.setText(f"The Name '{self.nam}' already exist!")
#                 return False

#         if self.cod != "":
#             if PaymentController.exists(self.cod, 'c', [self.model.id]):
#                 self.error.setText(f"The Code '{self.cod}' already exist!")
#                 return False

#         if self.cur == "": 
#             self.error.setText("Currency most not empty!")
#             return False

#         if self.atp == "": 
#             self.error.setText("Type most not empty!")
#             return False

#         return True
