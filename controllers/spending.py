from db import DBManager
from models import SpendingModel
from typing import List

from controllers.bank_account import BankAccountController, BankAccountModel

class SpendingController:
    
    def all():
        return SpendingController.to_model(DBManager.spendings.all())

    def get(id):
        return SpendingController.to_model(DBManager.spendings.search(DBManager.query.id == id))[0]

    def insert(record:SpendingModel):
        DBManager.spendings.insert(record.to_json())
        bac = BankAccountController.get(record.account)
        bac.amount -= record.amount
        BankAccountController.update(bac)

    def update(record:SpendingModel):
        old = SpendingController.get(record.id).amount
        DBManager.spendings.update(record.to_json(False), DBManager.query.id == record.id)
        bac = BankAccountController.get(record.account)
        bac.amount -= (record.amount - old)
        BankAccountController.update(bac)

    def delete(cid):
        old = SpendingController.get(cid)
        bac = BankAccountController.get(old.account)
        bac.amount += old.amount
        BankAccountController.update(bac)
        DBManager.spendings.remove(DBManager.query.id == cid)
        
    def search(search, filter='dc', ignore=[]):
        clts = set()

        q = DBManager.query.id == -1
        if 'd' in filter:
            q = q | DBManager.query.description.test(DBManager.has, search)
        if 'c' in filter:
            q = q | DBManager.query.category.test(DBManager.has, search)
        q = (q) & ~(DBManager.query.id.one_of(ignore))
        
        clts = SpendingController.to_model(DBManager.spendings.search(q)) 

        return set(clts)

    def search_by(search, filter=''):
        if filter == 'account':
            return SpendingController.to_model(DBManager.spendings.search(DBManager.query.account == search))
        if filter == 'id':
            return SpendingController.to_model(DBManager.spendings.search(DBManager.query.id == search))
        return []
        
    def exists(search, filter='', ignore=[]):
        clts = SpendingController.search(search, filter, ignore)
        
        return len(clts) != 0

    def to_model(clts) -> List[SpendingModel]:
        res = []
        for clt in clts:
            res.append(SpendingModel.from_json(clt))
        return res
