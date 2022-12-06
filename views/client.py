import re
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui import *

from views.table_view import TableView
from views.yes_no_dialog import YesNoDialog
from controllers import *
from models import *
from db import DBManager
from datetime import date, datetime

class ClientView(TableView):
    def __init__(self, main):
        super(ClientView, self).__init__(main)
        
        # manage UI
        self.add_btn.setText("Add Client")

        self.title.setText("Clients")

        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Usernames", "Country", "Mails", "Phones", ""])

        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(1, 120)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 120)
        self.table.setColumnWidth(4, 180)
        self.table.setColumnWidth(5, 130)
        self.table.setColumnWidth(6, 120)

        self.search.setText('')
        self.populate()

    def populate(self, rid=None, filter=''):
        self.table.setRowCount(0)

        prompt = self.search.text().strip()
        
        if prompt == '':
            if rid != None:
                clts = [ClientController.get(rid)]
            else:
                clts = ClientController.all()
        else:
            clts = ClientController.search(prompt)

        for clt in clts:
            r = super().add_row()
            self.set_row_content(r, clt)

        self.toggle_empty()

    def set_row_content(self, r:int, clt:ClientModel):
        nm = QTableWidgetItem(ClientModel.encode(clt.id))
        nm.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 0, nm)

        nam_el = QTableWidgetItem(clt.name)
        nam_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 2, nam_el)

        usrs = "\n".join(clt.usernames)
        usr_el = QTableWidgetItem(usrs)
        usr_el.setTextAlignment(Qt.AlignCenter)
        usr_el.setToolTip(usrs)
        self.table.setItem(r, 1, usr_el)

        cntr_el = QTableWidgetItem(clt.country)
        cntr_el.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(r, 3, cntr_el)

        mls = "\n".join(clt.mails)
        ml_el = QTableWidgetItem(mls)
        ml_el.setToolTip(mls)
        self.table.setItem(r, 4, ml_el)

        phs = "\n".join(clt.phones)
        ph_el = QTableWidgetItem(phs)
        ph_el.setToolTip(phs)
        self.table.setItem(r, 5, ph_el)

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

        pb = TableView.button(ADD_ICON, light=True)
        pb.setToolTip("Add project")
        pb.clicked.connect(lambda: self.add_project(clt.id))

        ab = TableView.button(LIST_ICON, light=True)
        ab.setToolTip("List project")
        ab.clicked.connect(lambda: self.main.update_view('project', clt.id, filter='client'))

        lay.addWidget(ab, Qt.AlignCenter)        
        lay.addWidget(pb, Qt.AlignCenter)        
        lay.addWidget(eb, Qt.AlignCenter)        
        lay.addWidget(rb, Qt.AlignCenter)        
        wid.setLayout(lay)

        self.table.setCellWidget(r, self.table.columnCount() - 1, wid)

    def add_row(self):
        app_selection = AddEditClientView(self, ClientModel())
        app_selection.exec()
                
    def edit_row(self, r):
        idx = ClientModel.decode(self.table.item(r, 0).text())
        model = ClientController.get(idx)
        app_selection = AddEditClientView(self, model, r)
        app_selection.exec()

    def remove_row(self, r):
        cid = ClientModel.decode(self.table.item(r, 0).text())

        ynd = YesNoDialog(f"Are you sure to delete client [{ClientModel.encode(cid)}]?")
        ynd.exec()
        if ynd.resp == YesNoDialog.Yes:
            self.table.removeRow(r)
            ClientController.delete(cid)

        self.populate()

    def add_project(self, cid):
        app_selection = AddProjectView(ProjectModel(cid))
        app_selection.exec()

    # def list_projects(self, id):
    #     self.main.update_view("project", id)

    def toggle_empty(self):
        if self.table.rowCount() == 0:
            self.table.hide()
            self.empty.show()
            if ClientController.all() == []:
                self.empty.setText("Table is empty! Add elements to it")
            else:
                self.empty.setText("No element found for the current search!")
        else:
            self.table.show()
            self.empty.hide()
        
class AddEditClientView(QDialog, UI_AddEditClient):
    def __init__(self, caller:ClientView, model:ClientModel, row:int=-1) -> None:
        super(AddEditClientView, self).__init__()
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
        self.save_btn.clicked.connect(self.add_client)

        for cntr in DBManager.countries.all():
            self.country.addItem(cntr['name'])

        self.country.setEditable(True)
        self.country.setInsertPolicy(QComboBox.NoInsert) 
        
        self.name.setText(model.name)
        self.username.setText('; '.join(model.usernames))
        self.email.setText('; '.join(model.mails))
        self.phone.setText('; '.join(model.phones))

        self.logo.setText(f"Client #{ClientModel.encode(model.id)}")
        self.country.setCurrentText(model.country)

    def keyPressEvent(self, event:QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return: self.add_project()
        if event.key() == Qt.Key_Escape: self.close()

    def add_client(self):
        if self.validate():
            self.model.name = self.nam
            self.model.country = self.ctr
            self.model.usernames = []
            for us in self.usr.split(';'): 
                self.model.add_username(us)
            self.model.mails = []
            for ml in self.mal.split(';'): 
                self.model.add_mail(ml)
            self.model.phones = []
            for tl in self.tel.split(';'): 
                self.model.add_phone(tl)
            
            if self.row == -1:
                ClientController.insert(self.model)
            else:
                ClientController.update(self.model)
            self.caller.populate()

            self.close()

    def read_values(self):
        self.usr = self.username.text().strip()
        self.nam = self.name.text().strip()
        self.mal = self.email.text().strip()
        self.tel = self.phone.text().strip()
        self.ctr = self.country.currentText()

    def validate(self):
        self.error.setText("")
        self.read_values()

        if self.usr == "" and self.nam == "": 
            self.error.setText("One of 'usernames' and 'name' should not be empty!")
            return False

        if self.nam != "":
            if ClientController.exists(self.nam, filter='n', ignore=[self.model.id]):
                self.error.setText(f"'name': '{self.nam}' already exist!")
                return False

        if self.usr != "":
            for us in self.usr.split(";"):
                if ClientController.exists(us, 'u', [self.model.id]):
                    self.error.setText(f"One of the usernames: '{us}' already exist!")
                    return False

        if self.mal != "":
            for ml in self.mal.split(";"):
                if not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", ml.strip()):
                    self.error.setText("'{ml} is not a mail address!")
                    return False
                if ClientController.exists(ml, 'm', [self.model.id]):
                    self.error.setText(f"One of the mails: '{ml}' already exist!")
                    return False

        if self.tel != "":
            for tl in self.tel.split(";"):
                if ClientController.exists(tl, 't', [self.model.id]):
                    self.error.setText(f"One of the phones numbers: '{tl}' already exist!")
                    return False

        if self.ctr == 0: 
            self.error.setText("'country' most not empty!")
            return False

        return True

class AddProjectView(QDialog, UI_AddProjet):
    def __init__(self, model:ProjectModel) -> None:
        super(AddProjectView, self).__init__()
        self.model = model
 
       # Set ui
        self.setupUi(self) 
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
 
        self.error.setText("")
        with open(STYLE_SHEET) as sc:
            self.setStyleSheet(sc.read())
        
        for cur in Currency.get():
            self.currency.addItem(Currency.code(cur).upper())
        
        self.start_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.due_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        
        self.price.setValidator(QDoubleValidator(decimals=2))
        
        self.cancel_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.add_project)

        # Populate fields
        self.logo.setText(f"Project #{model.id:05d}")
        self.title.setText(model.title)
        self.start_date.setDate(QDate(model.start_date.year, model.start_date.month, model.start_date.day))
        self.due_date.setDate(QDate(model.due_date.year, model.due_date.month, model.due_date.day))
        self.price.setText(f"{model.price:,.2f}")
        self.description.setPlainText(model.description)

    def keyPressEvent(self, event:QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return: self.add_project()
        if event.key() == Qt.Key_Escape: self.close()
        
    def add_project(self):
        if self.validate():
            self.model.title = self.tit
            self.model.start_date = self.sdt
            self.model.due_date = self.ddt
            self.model.price = self.prc
            self.model.currency = self.cur
            self.model.description = self.dsc
            
            ProjectController.insert(self.model)

            self.close()

    def validate(self):
        self.error.setText("")
        
        self.tit = self.title.text().strip()
        if self.tit == "": 
            self.error.setText("Enter a title!")
            return False
        
        self.sdt = datetime.strptime(self.start_date.text(), "%d-%m-%Y").date()
        self.ddt = datetime.strptime(self.due_date.text(), "%d-%m-%Y").date()
        
        self.prc = float(self.price.text().replace(',', ''))
        if self.prc == 0:
            self.error.setText("Set the project price!")
            return False

        self.cur = Currency.decode(self.currency.currentText().lower())
        self.dsc = self.description.toPlainText()

        if self.ddt < self.sdt:
            self.error.setText("Due date is prior to the start date!")
            return False

        return True

    def code_client(self, cid, client):
        return  f"CLT{cid:04d}: {client.name if client.name != '' else client.usernames[0]}"   

    def decode_client(self, s:str):
        return int(s.split(':')[0][3:])

    def populate_clients(self):
        self.client.clear()
        for cid, client in ClientController.get_all().items():
            self.client.addItem(self.code_client(cid, client))

