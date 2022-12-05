from models.model import Model

class Currency:
    USD = 0
    MAD = 0

    def code(s):
        if s == Currency.USD: return "usd"
        if s == Currency.MAD: return "mad"

    def decode(s):
        if s == "usd": return Currency.USD
        if s == "mad": return Currency.MAD

class BankAccountModel(Model):
    __cid:int = 0

    def __init__(self, name:str="") -> None:
        super().__init__()
        self.id = self.mid

        self.name = name
        self.type = type
        self.currency = Currency.USD
        self.amount = 0.0

    @property
    def mid(self) -> int:
        BankAccountModel.__cid += 1
        return BankAccountModel.__cid
    @mid.setter
    def mid(self, v:int):
        BankAccountModel.__cid = v - 1
        self.id = self.mid


    def code(id: int=-1) -> str:
        return "BAC" + str(id).zfill(4)

    def decode(code:str):
        return int(code[3:])

    def to_json(self, incude_id=True):
        d = {}
        if incude_id:
            d['id'] = self.id
        d['name'] = self.name
        d['type'] = self.type
        d['currency'] = self.currency
        d['amount'] = self.amount
        return d

    def from_json(item):
        clt = BankAccountModel(name=item['name'])
        clt.mid = item['id']
        clt.type = item['type']
        clt.currency = item['currency']
        clt.amount = item['amount']

        return clt
