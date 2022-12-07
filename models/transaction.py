from models.model import Model, Currency
from datetime import date, datetime

class TransactionModel(Model):
    __cid:int = 0

    def __init__(self, debtor_id:int=-1, creditor_id:int=-1, sent_amount:float=0.0, recv_amount:float=0.0, date:date=date.today()) -> None:
        super().__init__()
        self.id = self.mid
        self.debtor = debtor_id
        self.creditor = creditor_id
        self.sent = sent_amount
        self.received = recv_amount
        self.date = date

    @property
    def mid(self) -> int:
        TransactionModel.__cid += 1
        return TransactionModel.__cid
    @mid.setter
    def mid(self, v:int):
        TransactionModel.__cid = v - 1
        self.id = self.mid
        
    def encode(id: int=-1) -> str:
        return "TRN" + str(id).zfill(4)

    def decode(code:str):
        return int(code[3:])

    def to_json(self, incude_id=True):
        d = {}
        if incude_id:
            d['id'] = self.id
        d['debtor'] = self.debtor
        d['creditor'] = self.creditor
        d['sent-amount'] = self.sent
        d['received-amount'] = self.received
        d['date'] = date.strftime(self.date, "%d-%m-%Y")
        return d

    def from_json(item):
        clt = TransactionModel(debtor_id=item['debtor'], creditor_id=item['creditor'], sent_amount=item['sent-amount'], recv_amount=item['received-amount'])
        clt.mid = item['id']
        clt.date =  datetime.strptime(item['date'], "%d-%m-%Y").date()
        return clt
        