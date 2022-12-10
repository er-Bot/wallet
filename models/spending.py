from models.model import Model, Currency
from datetime import date, datetime

class SpendingCategory:
    Housing = 0
    Transportation = 1
    Food = 2
    Utilities = 3
    Medical = 4
    Personal = 5
    Entertainment = 6

    def get():
        return [
            SpendingCategory.Housing,
            SpendingCategory.Transportation,
            SpendingCategory.Food,
            SpendingCategory.Utilities,
            SpendingCategory.Medical,
            SpendingCategory.Personal,
            SpendingCategory.Entertainment
        ]

    def code(s):
        if s == SpendingCategory.Housing: return "housing"
        if s == SpendingCategory.Transportation: return "transportation"
        if s == SpendingCategory.Food:  return "food"
        if s == SpendingCategory.Utilities:  return "utilities"
        if s == SpendingCategory.Medical:  return "medical"
        if s == SpendingCategory.Personal:  return "personal"
        if s == SpendingCategory.Entertainment:  return "entertainment"

    def decode(s):
        if s == "housing": return SpendingCategory.Housing
        if s == "transportation": return SpendingCategory.Transportation
        if s == "food":  return SpendingCategory.Food
        if s == "utilities":  return SpendingCategory.Utilities
        if s == "medical":  return SpendingCategory.Medical
        if s == "personal":  return SpendingCategory.Personal
        if s == "entertainment":  return SpendingCategory.Entertainment

class SpendingModel(Model):
    __cid:int = 0

    def __init__(self, bank_id:int=1, amount:float=0.0, date:date=date.today(), category=SpendingCategory.Housing) -> None:
        super().__init__()
        self.id = self.mid
        self.account = bank_id
        self.amount = amount
        self.date = date
        self.category = category
        self.description = ""

    @property
    def mid(self) -> int:
        SpendingModel.__cid += 1
        return SpendingModel.__cid
    @mid.setter
    def mid(self, v:int):
        SpendingModel.__cid = v - 1
        self.id = self.mid
        
    def encode(id: int=-1) -> str:
        return "SPD" + str(id).zfill(4)

    def decode(code:str):
        return int(code[3:])

    def to_json(self, incude_id=True):
        d = {}
        if incude_id:
            d['id'] = self.id
        d['account'] = self.account
        d['amount'] = self.amount
        d['description'] = self.description
        d['category'] = SpendingCategory.code(self.category)
        d['date'] = date.strftime(self.date, "%d-%m-%Y")
        return d

    def from_json(item):
        clt = SpendingModel(bank_id=item['account'], amount=item['amount'])
        clt.mid = item['id']
        clt.category = SpendingCategory.decode(item['category'])
        clt.date =  datetime.strptime(item['date'], "%d-%m-%Y").date()
        clt.description = item['description']
        return clt
