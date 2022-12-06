from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui import *

from views.table_view import TableView
from views.yes_no_dialog import YesNoDialog
from controllers import *
from models import *
from datetime import date, datetime

class ProjectView(TableView):
    def __init__(self, main):
        super(ProjectView, self).__init__(main)
        
        # manage UI
        self.add_btn.setText("Add Project")

        self.title.setText("Projects")

        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["ID", "Client", "State", "Date", "Price", "Profit", "Title", ""])

        self.table.setColumnWidth(0, 90)
        self.table.setColumnWidth(1, 90)
        self.table.setColumnWidth(2, 80)
        self.table.setColumnWidth(3, 90)
        self.table.setColumnWidth(4, 100)
        self.table.setColumnWidth(5, 100)
        self.table.setColumnWidth(6, 230)
        self.table.setColumnWidth(7,  70)

        self.add_btn.hide()

        self.search.setText('')
        self.populate()

    def populate(self, rid=None, filter=''):
        self.table.setRowCount(0)

        prompt = self.search.text().strip()
        
        if prompt == '':
            if rid == None:
                records = ProjectController.all()
            else:
                records = ProjectController.search_by(rid, filter)
        else:
            records = ProjectController.search(prompt)

        for record in records:
            r = super().add_row()
            self.set_row_content(r, record)

        su = sum([sum([py.amount for py in PaymentController.search_by(p.id, 'id')  if py.currency == Currency.USD]) for p in ProjectController.all()])
        sm = sum([sum([py.amount for py in PaymentController.search_by(p.id, 'id')  if py.currency == Currency.MAD]) for p in ProjectController.all()])
        self.error.setText(f"Total Profit: {su + .1 * sm:,.2f} USD")
        self.toggle_empty()

    def set_row_content(self, r:int, record:ProjectModel):
        nam_el = QTableWidgetItem(ProjectModel.encode(record.id))
        nam_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 0, nam_el)

        nm = QPushButton(ClientModel.encode(record.client))
        nm.setProperty('class', 'LinkButton')
        nm.setCursor(Qt.PointingHandCursor)
        nm.clicked.connect(lambda:self.main.update_view('client', record.client))
        self.table.setCellWidget(r, 1, nm)

        stt_el = QTableWidgetItem(ProjectState.code(record.state).capitalize())
        stt_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 2, stt_el)

        dat_el = QTableWidgetItem(date.strftime(record.due_date if record.state == ProjectState.Ongoing else record.delivery_date, "%d-%m-%Y"))
        dat_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 3, dat_el)

        prc_el = QTableWidgetItem(f"{record.price:,.2f} {Currency.code(record.currency).upper()}")
        prc_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 4, prc_el)

        s = sum([p.amount for p in PaymentController.search_by(record.id, 'project')])
        pro_el = QTableWidgetItem(f"{s:,.2f} {Currency.code(record.currency).upper()}")
        pro_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 5, pro_el)


        tit_el = QTableWidgetItem(record.title.capitalize())
        tit_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 6, tit_el)

        wid = QWidget()
        wid.setStyleSheet("border: none;")
        lay = QBoxLayout(QBoxLayout.LeftToRight)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(5)
        
        rb = TableView.button(DELETE_ICON)
        rb.setToolTip("Remove client")
        rb.clicked.connect(lambda: self.remove_row(r))
        
        eb = TableView.button(EDIT_ICON)
        eb.setToolTip("Edit client")
        eb.clicked.connect(lambda: self.edit_row(r))
     
        lay.addWidget(eb, Qt.AlignCenter)        
        lay.addWidget(rb, Qt.AlignCenter)        
        wid.setLayout(lay)

        self.table.setCellWidget(r, self.table.columnCount() - 1, wid)
                
    def edit_row(self, r):
        idx = ProjectModel.decode(self.table.item(r, 0).text())
        model = ProjectController.get(idx)
        app_selection = EditProjectView(self, model, r)
        app_selection.exec()

    def remove_row(self, r):
        cid = ProjectModel.decode(self.table.item(r, 0).text())

        ynd = YesNoDialog(f"Are you sure to delete client [{ProjectModel.encode(cid)}]?")
        ynd.exec()
        if ynd.resp == YesNoDialog.Yes:
            self.table.removeRow(r)
            ProjectController.delete(cid)

        self.populate()

    # def add_project(self, cid):
    #     app_selection = AddProjectView(ProjectModel(cid))
    #     app_selection.exec()

    # def list_projects(self, id):
    #     self.main.update_view("project", id)

    def toggle_empty(self):
        if self.table.rowCount() == 0:
            self.table.hide()
            self.empty.show()
            if ProjectController.all() == []:
                self.empty.setText("Table is empty! Add elements to it")
            else:
                self.empty.setText("No element found for the current search!")
        else:
            self.table.show()
            self.empty.hide()
        
class EditProjectView(QDialog, UI_EditProjet):
    def __init__(self, caller:ProjectView, model:ProjectModel, row:int=-1) -> None:
        super(EditProjectView, self).__init__()
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
        self.save_btn.clicked.connect(self.edit_project)
        self.state.currentIndexChanged.connect(self.mark_done)
        self.account.currentIndexChanged.connect(self.set_currency)

        for stt in ProjectState.get():
            self.state.addItem(ProjectState.code(stt).capitalize())
        for cur in Currency.get():
            self.currency.addItem(Currency.code(cur).upper())
        for acc in BankAccountController.all():
            self.account.addItem(acc.code)
        
        self.start_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.due_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.end_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.payment_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        
        self.price.setValidator(QDoubleValidator(decimals=2))
        self.amount.setValidator(QDoubleValidator(decimals=2))

        self.title.setText(model.title)
        self.price.setText(f"{model.price:,.2f}")
        self.currency.setCurrentText(Currency.code(model.currency))
        self.start_date.setDate(QDate(model.start_date.year, model.start_date.month, model.start_date.day))
        self.due_date.setDate(QDate(model.due_date.year, model.due_date.month, model.due_date.day))
        self.payment_date.setDate(QDate(date.today().year, date.today().month, date.today().day))
        if model.state == ProjectState.Ongoing:
            self.end_date_frame.hide()
        else:
            self.end_date.setDate(QDate(model.delivery_date.year, model.delivery_date.month, model.delivery_date.day))
        self.description.setPlainText(model.description)
        self.comment.setPlainText(model.comment)
        
        self.logo.setText(f"Project #{ProjectModel.encode(model.id)}")

        self.payments.setColumnCount(6)
        self.payments.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.payments.setHorizontalHeaderLabels(["ID", "Account", "Date", "Total", "Currency", ""])
        self.payments.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.payments.setSelectionMode(QAbstractItemView.NoSelection)
        self.payments.setColumnWidth(0, 100)
        self.payments.setColumnWidth(1, 100)
        self.payments.setColumnWidth(2, 200)
        self.payments.setColumnWidth(3, 100)
        self.payments.setColumnWidth(4, 100)
        self.payments.setColumnWidth(5, 60)
        self.update_payments()

        self.add_pay.setIcon(QIcon(ADD_ICON))
        self.add_pay.setText("")
        self.add_pay.setToolTip("Add payment")
        self.add_pay.clicked.connect(self.add_payment)

    def mark_done(self):
        if self.state.currentText().lower() == ProjectState.code(ProjectState.Ongoing):
            self.end_date_frame.hide()
        else:
            self.end_date_frame.show()
            self.end_date.setDate(QDate(date.today().year, date.today().month, date.today().day))

    def set_currency(self):
        self.payment_currency.setText(Currency.code(BankAccountController.search(self.account.currentText().lower(), 'c')[0].currency).upper())

    def update_payments(self):
        self.payments.setRowCount(0)
        for pym in PaymentController.search_by(self.model.id, 'project'):
            r = self.payments.rowCount()
            self.payments.setRowCount(r + 1)
            self.set_payment(r, pym)

    def set_payment(self, r, pym):
            nm = QTableWidgetItem(PaymentModel.encode(pym.id))
            nm.setTextAlignment(Qt.AlignCenter)
            self.payments.setItem(r, 0, nm)

            nm = QTableWidgetItem(BankAccountController.get(pym.account).code)
            nm.setTextAlignment(Qt.AlignCenter)
            self.payments.setItem(r, 1, nm)

            typ_el = QTableWidgetItem(date.strftime(pym.date, "%A %d %B %Y"))
            typ_el.setTextAlignment(Qt.AlignCenter)
            self.payments.setItem(r, 2, typ_el)

            amt_el = QTableWidgetItem(f"{pym.amount:,.2f}")
            amt_el.setTextAlignment(Qt.AlignCenter)
            self.payments.setItem(r, 3, amt_el)

            cur_el = QTableWidgetItem(Currency.code(pym.currency).upper())
            cur_el.setTextAlignment(Qt.AlignCenter)
            self.payments.setItem(r, 4, cur_el)

            wid = QWidget()
            wid.setStyleSheet("border: none;")
            lay = QBoxLayout(QBoxLayout.LeftToRight)
            lay.setContentsMargins(0, 0, 0, 0)
            lay.setSpacing(5)
            
            rb = TableView.button(DELETE_ICON)
            rb.setToolTip("remove payment")
            rb.setFixedSize(30, 30)
            rb.clicked.connect(lambda: self.remove_payment(r))
            lay.addWidget(rb, Qt.AlignCenter)        
            wid.setLayout(lay)
            self.payments.setCellWidget(r, 5, wid)

    def remove_payment(self, r):
        cid = PaymentModel.decode(self.payments.item(r, 0).text())

        PaymentController.delete(cid)
        self.update_payments()

    def keyPressEvent(self, event:QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return: self.add_project()
        if event.key() == Qt.Key_Escape: self.close()

    def add_payment(self):
        if self.validate_payment():
            PaymentController.insert(PaymentModel(self.model.id, self.pbac, self.pamnt, self.pcur, self.pdat))
            self.update_payments()

    def validate_payment(self):
        self.pbac = BankAccountController.search(self.account.currentText(), 'c')[0].id
        
        if self.amount.text() == "":
            self.error.setText("Specify the amount paid by the client!")
            return False
        self.pamnt = float(self.amount.text().replace(',', ''))
        self.pcur = Currency.decode(self.payment_currency.text().lower())
        qd = self.payment_date.date()
        self.pdat = date(qd.year(), qd.month(), qd.day())
            
        if self.pdat < self.model.start_date:
            self.error.setText("Payment date should be greater than the start date!")
            return False

        return True

    def edit_project(self):
        if self.validate():
            self.model.title = self.tit
            self.model.price = self.prc
            self.model.currency = Currency.decode(self.cur)
            self.model.start_date = self.sdt
            self.model.due_date = self.ddt
            self.model.delivery_date = self.edt
            self.model.state = ProjectState.decode(self.stt)
            self.model.description = self.dsc
            self.model.comment = self.cmt
            ProjectController.update(self.model)
            self.caller.populate()

            self.close()

    def read_values(self):
        self.tit = self.title.text().strip()
        self.prc = float(self.price.text().replace(',', ''))
        self.sdt = datetime.strptime(self.start_date.text(), "%d-%m-%Y").date()
        self.ddt = datetime.strptime(self.due_date.text(), "%d-%m-%Y").date()
        self.edt = datetime.strptime(self.end_date.text(), "%d-%m-%Y").date()
        self.stt = self.state.currentText().lower()
        self.cur = self.currency.currentText().lower()
        self.dsc = self.description.toPlainText()
        self.cmt = self.comment.toPlainText()
            
    def validate(self):
        self.error.setText("")
        self.read_values()

        if self.tit == "": 
            self.error.setText("Enter a title!")
            return False

        if self.prc == 0:
            self.error.setText("Set the project price!")
            return False

        if self.ddt < self.sdt or (self.stt != ProjectState.code(ProjectState.Ongoing) and self.edt < self.sdt):
            self.error.setText("Due/End date is prior to the start date!")
            return False

        return True
