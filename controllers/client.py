from db.db_manager import DBManager
from models import ClientModel
from typing import List

class ClientController:
    
    def all():
        return ClientController.to_model(DBManager.clients.all())

    def get(rid):
        return ClientController.to_model(DBManager.clients.search(DBManager.query.id == rid))[0]

    def insert(client:ClientModel):
        DBManager.clients.insert(client.to_json())

    def update(client:ClientModel):
        DBManager.clients.update(client.to_json(False), DBManager.query.id == client.id)

    def delete(cid):
        DBManager.clients.remove(DBManager.query.id == cid)

    def search(search, filter='numt', ignore=[]):
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
        
        clts = ClientController.to_model(DBManager.clients.search(q)) 

        return set(clts)

    def exists(search, filter='numt', ignore=[]):
        clts = ClientController.search(search, filter, ignore)
        
        return len(clts) != 0

    def to_model(clts) -> List[ClientModel]:
        res = []
        for clt in clts:
            res.append(ClientModel.from_json(clt))
        return res
