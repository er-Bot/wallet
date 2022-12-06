class Model:
    def __init__(self) -> None:
        pass

    @property
    def mid(self):
        raise NotImplemented("'mid' need to be implemented in a child class!")

    def to_json(self, include_id=True):
        raise NotImplemented("'to_json' need to be implemented in a child class!")

    def from_json(k, item):
        raise NotImplemented("'from_json' need to be implemented in a child class!")

    def encode(id:int):
        raise NotImplemented("'code' need to be implemented in a child class!")

    def decode(code:str):
        raise NotImplemented("'decode' need to be implemented in a child class!")

class Currency:
    USD = 0
    MAD = 1

    def get():
        return [Currency.USD, Currency.MAD]

    def code(s):
        if s == Currency.USD: return "usd"
        if s == Currency.MAD: return "mad"

    def decode(s):
        if s == "usd": return Currency.USD
        if s == "mad": return Currency.MAD
