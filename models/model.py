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

    def code(id:int):
        raise NotImplemented("'code' need to be implemented in a child class!")

    def decode(code:str):
        raise NotImplemented("'decode' need to be implemented in a child class!")
