from models.model import Model, Currency


class AccountType:
    Checking = 0
    Savings = 1

    def get():
        return [AccountType.Checking, AccountType.Savings]

    def code(s):
        if s == AccountType.Checking: return "checking"
        if s == AccountType.Savings: return "savings"

    def decode(s):
        if s == "checking": return AccountType.Checking
        if s == "savings": return AccountType.Savings


class BankAccountModel(Model):
    __cid:int = 0

    def __init__(self, name:str="", code:str="") -> None:
        super().__init__()
        self.id = self.mid

        self.name = name
        self.code = code
        self.type = AccountType.Checking
        self.currency = Currency.USD

    @property
    def mid(self) -> int:
        BankAccountModel.__cid += 1
        return BankAccountModel.__cid
    @mid.setter
    def mid(self, v:int):
        BankAccountModel.__cid = v - 1
        self.id = self.mid


    def encode(id: int=-1) -> str:
        return "BAC" + str(id).zfill(4)

    def decode(code:str):
        return int(code[3:])

    def to_json(self, incude_id=True):
        d = {}
        if incude_id:
            d['id'] = self.id
        d['name'] = self.name
        d['code'] = self.code
        d['type'] = AccountType.code(self.type)
        d['currency'] = Currency.code(self.currency)
        return d

    def from_json(item):
        clt = BankAccountModel(name=item['name'], code=item['code'])
        clt.mid = item['id']
        clt.type = AccountType.decode(item['type'])
        clt.currency = Currency.decode(item['currency'])

        return clt
