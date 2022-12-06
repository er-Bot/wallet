
from datetime import date, datetime
from models.model import Model, Currency
from models.client import ClientModel

class ProjectState:
    Finished = 0
    Canceled = 1
    Ongoing = 2

    def code(s):
        if s == ProjectState.Finished: return "finished"
        if s == ProjectState.Canceled: return "cancelled"
        if s == ProjectState.Ongoing:  return "ongoing"

    def decode(s):
        if s == "finished": return ProjectState.Finished
        if s == "cancelled": return ProjectState.Canceled
        if s == "ongoing":  return ProjectState.Ongoing

class ProjectModel(Model):
    __pid:int = 0

    def __init__(self, cid:int=-1) -> None:
        super().__init__()

        self.id:int = self.mid
        self.title:str = ""
        self.client:int = cid

        self.start_date:date = date.today()
        self.due_date:date = date.today()
        self.delivery_date:date = None

        self.state = ProjectState.Ongoing
        self.price:float = 0
        self.currency = Currency.USD

        self.description:str = ""
        self.comment:str = ""        
        
    @property
    def mid(self) -> int:
        ProjectModel.__pid += 1
        return ProjectModel.__pid
    @mid.setter
    def mid(self, v:int):
        ProjectModel.__pid = v - 1
        self.id = self.mid
        
    def mark_done(self, date:date, state:ProjectState=ProjectState.Finished) -> None:
        if date >= self.start_date: 
            self.end_date = date
            self.state = state

    def encode(id: int=-1) -> str:
        return "PRJ" + str(id).zfill(4)

    def decode(code:str):
        return int(code[3:])

    def to_json(self, incude_id=True):
        d = {}
        if incude_id:
            d['id'] = self.id
        d['client'] = self.client
        d['title'] = self.title
        d['description'] = self.description
        d['comment'] = self.comment
        d['start-date'] = self.start_date
        d['due-date'] = self.due_date
        d['delivery-date'] = self.delivery_date
        d['price'] = self.price
        d['currency'] = self.currency
        d['state'] = self.state
        return d

    def from_json(item):
        clt = ProjectModel(cid=item['client'])
        clt.mid = item['id']
        clt.title = item['title']
        clt.description = item['description']
        clt.comment = item['comment']
        clt.start_date = datetime.strptime(item['start-date'], "%d-%m-%Y").date()
        clt.due_date = datetime.strptime(item['due-date'], "%d-%m-%Y").date()
        clt.delivery_date = datetime.strptime(item['delivery-date'], "%d-%m-%Y").date()
        clt.price = item['price']
        clt.currency = Currency.decode(item['currency'])
        clt.state = ProjectState.decode(item['state'])
        return clt
