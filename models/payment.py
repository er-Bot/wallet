from models.model import Model, Currency
from datetime import date, datetime

class PaymentModel(Model):
    __cid:int = 0

    def __init__(self, project_id:int, bank_id:int, amount:float=0.0, currency:Currency=Currency.USD, date:date=date.today()) -> None:
        super().__init__()
        self.id = self.mid
        self.project = project_id
        self.account = bank_id
        self.amount = amount
        self.currency = currency
        self.date = date

    @property
    def mid(self) -> int:
        PaymentModel.__cid += 1
        return PaymentModel.__cid
    @mid.setter
    def mid(self, v:int):
        PaymentModel.__cid = v - 1
        self.id = self.mid
        
    def encode(id: int=-1) -> str:
        return "PYM" + str(id).zfill(4)

    def decode(code:str):
        return int(code[3:])

    def to_json(self, incude_id=True):
        d = {}
        if incude_id:
            d['id'] = self.id
        d['project'] = self.project
        d['account'] = self.account
        d['amount'] = self.amount
        d['currency'] = Currency.code(self.currency)
        d['date'] = date.strftime(self.date, "%d-%m-%Y")
        return d

    def from_json(item):
        clt = PaymentModel(project_id=item['project'], bank_id=item['account'], amount=item['amount'])
        clt.mid = item['id']
        clt.currency = Currency.decode(item['currency'])
        clt.date =  datetime.strptime(item['date'], "%d-%m-%Y").date()
        return clt
        