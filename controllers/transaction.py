from db import DBManager
from models import TransactionModel
from typing import List

from controllers.bank_account import BankAccountController, BankAccountModel
from models import TransactionModel

class TransactionController:
    
    def all():
        return TransactionController.to_model(DBManager.transactions.all())

    def get(id):
        return TransactionController.to_model(DBManager.transactions.search(DBManager.query.id == id))[0]

    def insert(record:TransactionModel):
        deb = BankAccountController.get(record.debtor)
        deb.amount -= record.sent
        BankAccountController.update(deb)

        crd = BankAccountController.get(record.creditor)
        crd.amount += record.received
        BankAccountController.update(crd)

        DBManager.transactions.insert(record.to_json())

    def update(record:TransactionModel):
        sold = TransactionController.get(record.id).sent
        rold = TransactionController.get(record.id).received

        deb = BankAccountController.get(record.debtor)
        deb.amount -= (record.sent - sold)
        BankAccountController.update(deb)

        crd = BankAccountController.get(record.creditor)
        crd.amount += (record.received - rold)
        BankAccountController.update(crd)

        DBManager.transactions.update(record.to_json(False), DBManager.query.id == record.id)

    def delete(cid):
        record = TransactionController.get(cid)

        deb = BankAccountController.get(record.debtor)
        deb.amount += record.sent
        BankAccountController.update(deb)

        crd = BankAccountController.get(record.creditor)
        crd.amount -= record.received
        BankAccountController.update(crd)

        DBManager.transactions.remove(DBManager.query.id == cid)
        
    def search_by(search, filter=''):
        return []
        
    def to_model(clts) -> List[TransactionModel]:
        res = []
        for clt in clts:
            res.append(TransactionModel.from_json(clt))
        return res
