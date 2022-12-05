from db.db_manager import DBManager
from models import BankAccountModel

class BankAccountController:
    
    def all():
        return BankAccountController.to_model(DBManager.bank_accounts.all())

    def get(id):
        return BankAccountController.to_model(DBManager.bank_accounts.search(DBManager.query.id == id))[0]

    def insert(record:BankAccountModel):
        DBManager.bank_accounts.insert(record.to_json())

    def update(record:BankAccountModel):
        DBManager.bank_accounts.update(record.to_json(False), DBManager.query.id == record.id)

    def delete(cid):
        DBManager.bank_accounts.remove(DBManager.query.id == cid)

    def search(search, filter='ntcr', ignore=[]):
        clts = set()

        q = DBManager.query.id == -1
        if 'n' in filter:
            q = q | DBManager.query.name.test(DBManager.has, search)
        if 't' in filter:
            q = q | DBManager.query.type.test(DBManager.has, search)
        if 'c' in filter:
            q = q | DBManager.query.code.test(DBManager.has, search)
        if 'r' in filter:
            q = q | DBManager.query.currency.test(DBManager.has, search)
        q = (q) & ~(DBManager.query.id.one_of(ignore))
        
        clts = BankAccountController.to_model(DBManager.bank_accounts.search(q)) 

        return set(clts)

    def exists(search, filter='ntcr', ignore=[]):
        clts = BankAccountController.search(search, filter, ignore)
        return len(clts) != 0

    def to_model(clts) -> list[BankAccountModel]:
        res = []
        for clt in clts:
            res.append(BankAccountModel.from_json(clt))
        return res
