from db.db_manager import DBManager
from models import ProjectModel
from typing import List
from controllers.payment import PaymentController

class ProjectController:
    
    def all():
        return ProjectController.to_model(DBManager.projects.all())

    def get(rid):
        return ProjectController.to_model(DBManager.projects.search(DBManager.query.id == rid))[0]

    def insert(record:ProjectModel):
        DBManager.projects.insert(record.to_json())

    def update(record:ProjectModel):
        DBManager.projects.update(record.to_json(False), DBManager.query.id == record.id)

    def delete(cid):
        DBManager.projects.remove(DBManager.query.id == cid)
        for pym in PaymentController.search_by(cid, 'project'):
            PaymentController.delete(pym.id)

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
        
        clts = ProjectController.to_model(DBManager.projects.search(q)) 

        return set(clts)

    def search_by(search, filter=''):
        if filter == 'client':
            return ProjectController.to_model(DBManager.projects.search(DBManager.query.client == search))
        elif filter == 'id':
            return ProjectController.to_model(DBManager.projects.search(DBManager.query.id == search))


    def exists(search, filter='numt', ignore=[]):
        clts = ProjectController.search(search, filter, ignore)
        
        return len(clts) != 0

    def to_model(clts) -> List[ProjectModel]:
        res = []
        for clt in clts:
            res.append(ProjectModel.from_json(clt))
        return res

