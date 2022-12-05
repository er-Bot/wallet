from db.db_manager import DBManager
from models import PaymentModel

class PaymentController:
    
    def all():
        return PaymentController.to_model(DBManager.payments.all())

    def get(id):
        return PaymentController.to_model(DBManager.payments.search(DBManager.query.id == id))[0]

    def insert(record:PaymentModel):
        DBManager.payments.insert(record.to_json())

    def update(record:PaymentModel):
        DBManager.payments.update(record.to_json(False), DBManager.query.id == record.id)

    def delete(cid):
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

    def exists(search, filter='', ignore=[]):
        clts = PaymentController.search(search, filter, ignore)
        
        return len(clts) != 0

    def to_model(clts) -> list[PaymentModel]:
        res = []
        for clt in clts:
            res.append(PaymentModel.from_json(clt))
        return res
