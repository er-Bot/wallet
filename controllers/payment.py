from db import DBManager
from models import PaymentModel
from typing import List

from controllers.bank_account import BankAccountController, BankAccountModel

class PaymentController:
    
    def all():
        return PaymentController.to_model(DBManager.payments.all())

    def get(id):
        return PaymentController.to_model(DBManager.payments.search(DBManager.query.id == id))[0]

    def insert(record:PaymentModel):
        DBManager.payments.insert(record.to_json())
        bac = BankAccountController.get(record.account)
        if bac.code == "FVRR":
            bac.amount += record.amount * .8
        else:
            bac.amount += record.amount
        BankAccountController.update(bac)

    def update(record:PaymentModel):
        old = PaymentController.get(record.id).amount
        DBManager.payments.update(record.to_json(False), DBManager.query.id == record.id)
        bac = BankAccountController.get(record.account)
        if bac.code == "FVRR":
            bac.amount += (record.amount - old) * .8
        else:
            bac.amount += (record.amount - old)
        BankAccountController.update(bac)

    def delete(cid):
        old = PaymentController.get(cid)
        bac = BankAccountController.get(old.account)
        if bac.code == "FVRR":
            bac.amount -= old.amount * .8
        else:
            bac.amount -= old.amount
        BankAccountController.update(bac)
        DBManager.payments.remove(DBManager.query.id == cid)
        

    def search(search, filter='', ignore=[]):
        clts = set()

        q = DBManager.query.id == -1
        if 'n' in filter:
            q = q | DBManager.query.name.test(DBManager.has, search)
        if 'u' in filter:
            q = q | DBManager.query.usernames.test(DBManager.list_has, search)
        if 'm' in filter:
            q = q | DBManager.query.mails.test(DBManager.list_has, search)
        if 't' in filter:
            q = q | DBManager.query.phones.test(DBManager.list_has, search)
        q = (q) & ~(DBManager.query.id.one_of(ignore))
        
        clts = PaymentController.to_model(DBManager.payments.search(q)) 

        return set(clts)

    def search_by(search, filter=''):
        if filter == 'account':
            return PaymentController.to_model(DBManager.payments.search(DBManager.query.account == search))
        if filter == 'id':
            return PaymentController.to_model(DBManager.payments.search(DBManager.query.id == search))
        if filter == 'project':
            return PaymentController.to_model(DBManager.payments.search(DBManager.query.project == search))
        return []
        
    def exists(search, filter='', ignore=[]):
        clts = PaymentController.search(search, filter, ignore)
        
        return len(clts) != 0

    def to_model(clts) -> List[PaymentModel]:
        res = []
        for clt in clts:
            res.append(PaymentModel.from_json(clt))
        return res
