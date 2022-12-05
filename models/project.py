
from datetime import date, datetime
from typing import List
from models import Model, ClientModel

class ProjectState:
    Finished = 0
    Canceled = 1
    Ongoing = 2

    def code(s):
        if s == ProjectState.Finished: return "finished"
        if s == ProjectState.Canceled: return "cancelled"
        if s == ProjectState.Ongoing:  return "started"

    def decode(s):
        if s == "finished": return ProjectState.Finished
        if s == "cancelled": return ProjectState.Canceled
        if s == "started":  return ProjectState.Ongoing

class ProjectModel(Model):
    __pid:int = 0

    def __init__(self, cid:int=-1) -> None:
        super().__init__()

        self.id:int = self.mid
        self.title:str = ""
        self.client:int = cid

        self.start_date:date = date.today()
        self.due_date:date = date.today()
        self.end_date:date = None
        self.state = ProjectState.Ongoing

        self.price:float = 0
        self.payments : List[PaymentModel] = []

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
    
    def add_payment(self, payment:PaymentModel) -> None:
        self.payments.append(payment)
    
    def mark_done(self, date:date, state:ProjectState=ProjectState.Finished) -> None:
        if date >= self.start_date: 
            self.end_date = date
            self.state = state

    def code(id: int):
        return f"project_{id:05d}"

    def decode(code: str):
        return int(code.split('_')[1])

    def to_json(self):
        return {
            'client': ClientModel.code(self.client),
            'title': self.title,
            'start': date.strftime(self.start_date, "%d-%m-%Y"),
            'due': date.strftime(self.due_date, "%d-%m-%Y"),
            'end': date.strftime(self.end_date, "%d-%m-%Y"),
            'state': ProjectState.code(self.state),
            'price': self.price,
            'payments': [payment.to_json() for payment in self.payments],
            'description': self.description,
            'comment': self.comment,
        }

    def from_json(k, item):
        prj = ProjectModel()
        prj.mid = ProjectModel.decode(k)

        prj.client = ClientModel.decode(item['client'])
        prj.title = item['title']
        prj.start_date = datetime.strptime(item['start'], '%d-%m-%Y').date()
        prj.due_date = datetime.strptime(item['due'], '%d-%m-%Y').date()
        prj.end_date = datetime.strptime(item['end'], '%d-%m-%Y').date()
        prj.state = ProjectState.decode(item['state'])
        
        prj.price = item['price']
        for el in item['payments']: prj.add_payment(PaymentModel.from_json(0, el))
        
        prj.description = item['description'] 
        prj.comment =item['comment']


        return prj