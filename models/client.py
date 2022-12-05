from models.model import Model

class ClientModel(Model):
    __cid:int = 0

    def __init__(self, name:str="", username:str="", country:str="", mail:str="", phone:str="") -> None:
        super().__init__()
        self.id = self.mid
        self.name = name
        self.usernames = []
        self.phones = []
        self.mails = []
        self.country = country

        self.add_username(username)
        self.add_mail(mail)
        self.add_phone(phone)

    @property
    def mid(self) -> int:
        ClientModel.__cid += 1
        return ClientModel.__cid
    @mid.setter
    def mid(self, v:int):
        ClientModel.__cid = v - 1
        self.id = self.mid
        

    def add_username(self, usr:str) -> None:
        usr = usr.strip()
        if usr != '' and usr not in self.usernames: self.usernames.append(usr)
    
    def add_mail(self, mail:str) -> None:
        mail = mail.strip()
        if mail != '' and mail not in self.mails: self.mails.append(mail)
    
    def add_phone(self, tel:str) -> None:
        tel = tel.strip()
        if tel != '' and tel not in self.phones: self.phones.append(tel)

    def code(id: int=-1) -> str:
        return "CLT" + str(id).zfill(4)

    def decode(code:str):
        return int(code[3:])

    def to_json(self, incude_id=True):
        d = {}
        if incude_id:
            d['id'] = self.id
        d['name'] = self.name
        d['country'] = self.country
        d['usernames'] = self.usernames
        d['mails'] = self.mails
        d['phones'] = self.phones
        return d

    def from_json(item):
        clt = ClientModel(name=item['name'], country=item['country'])
        clt.mid = item['id']
        for el in item['usernames']: clt.add_username(el)
        for el in item['mails']: clt.add_mail(el)
        for el in item['phones']: clt.add_phone(el)
        return clt
